#!/usr/bin/env python3
from __future__ import annotations
import argparse, concurrent.futures, csv, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

BUCKETS=128

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""): h.update(block)
    return h.hexdigest()

def run(cmd:list[str],log:Path|None=None)->None:
    if log:
        log.parent.mkdir(parents=True,exist_ok=True)
        with log.open("w") as f: subprocess.run(cmd,check=True,stdout=f,stderr=subprocess.STDOUT,text=True)
    else: subprocess.run(cmd,check=True)

def source_file(root:Path,bucket:int)->Path:
    name=f"b{bucket:04d}.bin"
    for p in (root/name,root/"cur"/name):
        if p.exists(): return p
    raise FileNotFoundError(name)

def compile_engine(src:Path,binary:Path)->None:
    binary.parent.mkdir(parents=True,exist_ok=True)
    run(["g++","-O3","-DNDEBUG","-std=c++20",str(src),"-o",str(binary),"-lcrypto"])

def aggregate_workers(worker_dir:Path):
    rows=[json.loads(p.read_text()) for p in sorted(worker_dir.glob("s[0-9][0-9][0-9][0-9].json"))]
    if len(rows)!=BUCKETS: raise RuntimeError(f"only {len(rows)} worker receipts present")
    sums={k:sum(int(r[k]) for r in rows) for k in [
        "source_states","raw_children","inadmissible","hits","terminal_pruned",
        "safe_pruned","viability_pruned","emitted_before_run_dedup","runs"]}
    sums["max_denominator"]=max(int(r["max_denominator"]) for r in rows)
    best=max(rows,key=lambda r:int(r["max_q_num"])/max(1,int(r["max_q_den"])))
    sums["max_q_num"]=int(best["max_q_num"]); sums["max_q_den"]=int(best["max_q_den"])
    return rows,sums

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--checkpoint-root",type=Path,required=True)
    ap.add_argument("--hash-manifest",type=Path,required=True)
    ap.add_argument("--work-root",type=Path,required=True)
    ap.add_argument("--start-time",type=int,default=185)
    ap.add_argument("--end-time",type=int,default=211)
    ap.add_argument("--jobs",type=int,default=max(1,min(8,os.cpu_count() or 1)))
    ap.add_argument("--merge-jobs",type=int,default=max(1,min(8,os.cpu_count() or 1)))
    ap.add_argument("--buffer-keys",type=int,default=65536)
    ap.add_argument("--fanin",type=int,default=64)
    ap.add_argument("--minimum-free-gb",type=float,default=100.0)
    ap.add_argument("--safe-bin",type=Path)
    ap.add_argument("--full-checkpoint-audit",action="store_true")
    ap.add_argument("--delete-previous-generated",action="store_true")
    ap.add_argument("--allow-noncanonical",action="store_true",help="smoke test only")
    ns=ap.parse_args()
    here=Path(__file__).resolve().parent
    validator=here/"validate_checkpoint.py"
    cpp=here/"rgphi_stage_b2_engine.cpp"
    binary=ns.work_root/"bin"/"rgphi_stage_b2_engine"
    ns.work_root.mkdir(parents=True,exist_ok=True)
    readiness=ns.work_root/"CHECKPOINT_READINESS.json"
    check=[sys.executable,str(validator),str(ns.checkpoint_root),"--hash-manifest",str(ns.hash_manifest),"--mode","full" if ns.full_checkpoint_audit else "hash","--output",str(readiness)]
    if ns.allow_noncanonical: check.append("--allow-noncanonical")
    run(check)
    free=shutil.disk_usage(ns.work_root).free/(1024**3)
    if free<ns.minimum_free_gb: raise RuntimeError(f"free space {free:.2f} GiB below required {ns.minimum_free_gb:.2f} GiB")
    compile_engine(cpp,binary)
    source_root=ns.checkpoint_root; initial_root=source_root
    ledger=[]
    for source_time in range(ns.start_time,ns.end_time):
        child_time=source_time+1
        tmp=ns.work_root/f"level_{child_time:03d}.tmp"
        final=ns.work_root/f"level_{child_time:03d}"
        if final.exists():
            manifest=json.loads((final/"manifest.json").read_text())
            runtime_path=final/"runtime.json"
            runtime=json.loads(runtime_path.read_text()) if runtime_path.exists() else {"seconds":0.0}
            ledger.append({"time":int(manifest["time"]),"states":int(manifest["states"]),"bytes":int(manifest["bytes"]),"manifest_sha256":sha256(final/"manifest.json"),"seconds":float(runtime.get("seconds",0.0)),"resumed":True})
            source_root=final
            continue
        if tmp.exists(): shutil.rmtree(tmp)
        runroot=tmp/"runs"; logs=tmp/"logs"; outdir=tmp/"buckets"
        runroot.mkdir(parents=True); logs.mkdir(); outdir.mkdir()
        started=time.time()
        def worker(i:int):
            cmd=[str(binary),"worker","--src",str(source_file(source_root,i)),"--src-bucket",str(i),"--run-root",str(runroot),"--source-time",str(source_time),"--buffer-keys",str(ns.buffer_keys)]
            if ns.safe_bin: cmd += ["--safe-bin",str(ns.safe_bin)]
            run(cmd,logs/f"worker_{i:04d}.log")
        with concurrent.futures.ThreadPoolExecutor(max_workers=ns.jobs) as ex:
            list(ex.map(worker,range(BUCKETS)))
        _,stats=aggregate_workers(runroot/"workers")
        hits=[]
        for p in sorted((runroot/"workers").glob("*_hits.csv")):
            with p.open() as f:
                hits.extend(list(csv.DictReader(f)))
        if hits:
            receipt={"status":"HIT","source_time":source_time,"child_time":child_time,"hits":hits,"worker_stats":stats,"seconds":time.time()-started}
            (tmp/"HIT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
            print(json.dumps(receipt,indent=2)); return 0
        def merge(i:int):
            d=runroot/f"d{i:04d}"; out=outdir/f"b{i:04d}.bin"
            run([str(binary),"merge","--run-dir",str(d),"--out",str(out),"--dst-bucket",str(i),"--fanin",str(ns.fanin),"--delete-inputs"],logs/f"merge_{i:04d}.log")
        with concurrent.futures.ThreadPoolExecutor(max_workers=ns.merge_jobs) as ex:
            list(ex.map(merge,range(BUCKETS)))
        buckets=[]; total=0; total_bytes=0
        for i in range(BUCKETS):
            p=outdir/f"b{i:04d}.bin"; meta=json.loads(Path(str(p)+".json").read_text())
            total += int(meta["count"]); total_bytes += int(meta["bytes"]); buckets.append(meta)
        elapsed=time.time()-started
        manifest={"gate":"RGPHI-GLOBAL-TRAP-CUT-088-STAGE-B2","source_time":source_time,"time":child_time,"states":total,"bytes":total_bytes,"buckets":buckets,"worker_stats":stats,"hits":0,"format":"little-endian uint64 key=(a<<32)|b; SplitMix64(key)&127"}
        mpath=tmp/"manifest.json"; mpath.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
        (tmp/"manifest.sha256").write_text(f"{sha256(mpath)}  manifest.json\n")
        (tmp/"runtime.json").write_text(json.dumps({"seconds":elapsed},indent=2)+"\n")
        for p in outdir.iterdir(): shutil.move(str(p),tmp/p.name)
        outdir.rmdir(); shutil.rmtree(runroot)
        os.sync(); tmp.rename(final)
        ledger.append({"time":child_time,"states":total,"bytes":total_bytes,"manifest_sha256":sha256(final/"manifest.json"),"seconds":elapsed})
        (ns.work_root/"STAGE_B2_LEDGER.json").write_text(json.dumps(ledger,indent=2)+"\n")
        if ns.delete_previous_generated and source_root!=initial_root and source_root.exists(): shutil.rmtree(source_root)
        source_root=final
        print(json.dumps(ledger[-1],indent=2),flush=True)
    canonical=(ns.start_time==185 and ns.end_time==211 and not ns.allow_noncanonical)
    if canonical:
        result={"status":"NO_HIT_THROUGH_211","tau5":212,"bellman_ladder":{"start":0,"end":212,"formula":"V5(x_t)=212-t"},"ledger":ledger}
    else:
        result={"status":f"COMPLETED_NO_HIT_THROUGH_{ns.end_time}","tau5_claim_changed":False,"ledger":ledger}
    (ns.work_root/"RGPHI_STAGE_B2_FINAL_RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
