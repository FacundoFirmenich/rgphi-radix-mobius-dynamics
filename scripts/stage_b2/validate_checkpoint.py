#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math, re, struct
from pathlib import Path

EXPECTED_MANIFEST_SHA = "dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7"
EXPECTED_STATES = 2_462_600_671
EXPECTED_BYTES = 19_700_805_368
EXPECTED_BUCKETS = 128
REC = struct.Struct("<Q")

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()

def mix64(x:int)->int:
    mask=(1<<64)-1
    x=(x+0x9e3779b97f4a7c15)&mask
    x=((x^(x>>30))*0xbf58476d1ce4e5b9)&mask
    x=((x^(x>>27))*0x94d049bb133111eb)&mask
    return x^(x>>31)

def parse_hashes(path:Path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip(): continue
        h,name=line.split(maxsplit=1)
        name=name.strip().lstrip("*")
        m=re.search(r"b(\d{4})\.bin$",name)
        if not m: raise ValueError(f"unrecognized bucket path: {name}")
        rows.append((int(m.group(1)),h,name))
    rows.sort()
    return rows

def structural_check(path:Path,bucket:int)->int:
    count=0; prev=None
    with path.open("rb") as f:
        while True:
            z=f.read(8)
            if not z: break
            if len(z)!=8: raise ValueError(f"truncated record in {path}")
            (k,)=REC.unpack(z)
            if prev is not None and k<=prev:
                raise ValueError(f"bucket {bucket}: not strictly sorted/unique at record {count}")
            a=k>>32; b=k&0xffffffff
            if not (0<=a<b): raise ValueError(f"bucket {bucket}: invalid state {a}/{b}")
            if math.gcd(a,b)!=1: raise ValueError(f"bucket {bucket}: nonprimitive state {a}/{b}")
            if (mix64(k)&127)!=bucket:
                raise ValueError(f"bucket {bucket}: partition mismatch for {a}/{b}")
            prev=k; count+=1
    return count

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("checkpoint_root",type=Path,help="directory containing cur/b0000.bin ... or the bucket files directly")
    ap.add_argument("--hash-manifest",type=Path,required=True)
    ap.add_argument("--mode",choices=["hash","full"],default="hash")
    ap.add_argument("--output",type=Path)
    ap.add_argument("--expected-manifest-sha",default=EXPECTED_MANIFEST_SHA)
    ap.add_argument("--allow-noncanonical",action="store_true",help="for smoke tests only")
    ns=ap.parse_args()
    manifest_sha=sha256(ns.hash_manifest)
    rows=parse_hashes(ns.hash_manifest)
    errors=[]
    if len(rows)!=EXPECTED_BUCKETS: errors.append(f"bucket manifest has {len(rows)} rows, expected {EXPECTED_BUCKETS}")
    if not ns.allow_noncanonical and manifest_sha!=ns.expected_manifest_sha:
        errors.append(f"manifest SHA mismatch: {manifest_sha}")
    total_bytes=0; total_states=0; verified=[]
    for bucket,h,name in rows:
        candidates=[ns.checkpoint_root/name,ns.checkpoint_root/Path(name).name,ns.checkpoint_root/"cur"/Path(name).name]
        p=next((x for x in candidates if x.exists()),None)
        if p is None:
            errors.append(f"missing bucket {bucket:04d}: {Path(name).name}")
            continue
        size=p.stat().st_size; total_bytes+=size
        if size%8: errors.append(f"bucket {bucket:04d}: size {size} not multiple of 8")
        got=sha256(p)
        if got!=h: errors.append(f"bucket {bucket:04d}: SHA mismatch {got} != {h}")
        count=size//8
        if ns.mode=="full" and got==h:
            checked=structural_check(p,bucket)
            if checked!=count: errors.append(f"bucket {bucket:04d}: count mismatch")
        total_states+=count
        verified.append({"bucket":bucket,"path":str(p),"bytes":size,"count":count,"sha256":got})
    if not ns.allow_noncanonical:
        if total_bytes!=EXPECTED_BYTES: errors.append(f"total bytes {total_bytes}, expected {EXPECTED_BYTES}")
        if total_states!=EXPECTED_STATES: errors.append(f"total states {total_states}, expected {EXPECTED_STATES}")
    result={
        "gate":"RGPHI-GLOBAL-TRAP-CUT-088-STAGE-B2-CHECKPOINT-READINESS",
        "status":"READY" if not errors else "BLOCKED",
        "mode":ns.mode,
        "checkpoint_root":str(ns.checkpoint_root),
        "bucket_manifest":str(ns.hash_manifest),
        "bucket_manifest_sha256":manifest_sha,
        "verified_buckets":len(verified),
        "total_states":total_states,
        "total_bytes":total_bytes,
        "errors":errors,
    }
    text=json.dumps(result,indent=2)+"\n"
    if ns.output:
        ns.output.parent.mkdir(parents=True,exist_ok=True); ns.output.write_text(text)
    print(text,end="")
    return 0 if not errors else 3
if __name__=="__main__": raise SystemExit(main())
