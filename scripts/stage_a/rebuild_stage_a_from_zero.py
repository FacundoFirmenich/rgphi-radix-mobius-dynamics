#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import math
import os
import shutil
import struct
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

BUCKETS = 128
Q_TARGET = 1_100_000
EXPECTED_SAFE_CSV_SHA = "276431f5e8330bef10f6e1cf656bca7c7b24821af060a8c8aedfad38fb24e27b"
EXPECTED_SAFE_STATES = 18_472
EXPECTED_T185_STATES = 2_462_600_671
EXPECTED_T185_BYTES = 19_700_805_368
EXPECTED_T185_MANIFEST_SHA = "dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7"
EXPECTED_EARLIEST_SHA = "bc73eca91efed5c13a932e9473b70f9c3d4616e91c06e93cc73c5eb4855831fe"
EXPECTED_HYBRID_SHA = "19a60a5ebc5b9b1c9c6be0faf7b6c77dc88e1591af96308628973108abb2b5cc"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def run(cmd: list[str], log: Path | None = None) -> None:
    if log:
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("w") as fh:
            subprocess.run(cmd, check=True, stdout=fh, stderr=subprocess.STDOUT, text=True)
    else:
        subprocess.run(cmd, check=True)


def atomic_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def splitmix64(x: int) -> int:
    x = (x + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
    return x ^ (x >> 31)


def pack(a: int, b: int) -> int:
    return (a << 32) | b


def unpack(k: int) -> tuple[int, int]:
    return k >> 32, k & 0xFFFFFFFF


def target(a: int, b: int) -> bool:
    return a < b and b > Q_TARGET * (b - a)


def viable(b: int, child_time: int) -> bool:
    remaining = 211 - child_time
    if remaining < 0:
        return False
    s = (remaining + 1) // 2
    return s >= 64 or (b << s) > Q_TARGET


TERMINALS = {
    pack(a, b)
    for a, b in [
        (2,11),(9,11),(0,1),(1,1),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),
        (7,8),(7,9),(7,10),(4,11),(7,11),(7,12),(2,13),(5,13),(6,13),
        (7,13),(8,13),(11,13),(11,20),
    ]
}


def empty_bucket_set(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for i in range(BUCKETS):
        (root / f"b{i:04d}.bin").touch()


def compile_tools(repo: Path, bin_dir: Path) -> tuple[Path, Path, Path]:
    bin_dir.mkdir(parents=True, exist_ok=True)
    engine = bin_dir / "rgphi_stage_b2_engine"
    seen_filter = bin_dir / "rgphi_seen_filter"
    trap = bin_dir / "trap_atlas_exact"
    run(["g++", "-O3", "-DNDEBUG", "-std=c++20",
         str(repo / "scripts/stage_b2/rgphi_stage_b2_engine.cpp"),
         "-o", str(engine), "-lcrypto"])
    run(["g++", "-O3", "-DNDEBUG", "-std=c++20",
         str(repo / "scripts/stage_a/rgphi_seen_filter.cpp"),
         "-o", str(seen_filter)])
    run(["g++", "-O3", "-DNDEBUG", "-std=c++20",
         str(repo / "scripts/stage_a/trap_atlas_exact.cpp"),
         "-o", str(trap)])
    return engine, seen_filter, trap


def prepare_safe_states(repo: Path, root: Path, trap_binary: Path) -> tuple[Path, set[int]]:
    cache = root / "cache" / "safe_D10000"
    cache.mkdir(parents=True, exist_ok=True)
    safe_csv = cache / "D10000_safe_states.csv"
    safe_bin = cache / "D10000_safe_states.bin"

    if not safe_csv.exists() or sha256(safe_csv) != EXPECTED_SAFE_CSV_SHA:
        dummy = cache / "empty_chain.csv"
        dummy.write_text("depth,target,parent,witness_action,x,alternate_action,y,alternate_state\n")
        out = cache / "trap_atlas_output.tmp"
        if out.exists():
            shutil.rmtree(out)
        out.mkdir()
        run([str(trap_binary), "10000", str(dummy), str(out)], cache / "trap_atlas_D10000.log")
        produced = out / "D2500_safe_states.csv"
        if not produced.exists():
            raise RuntimeError("trap atlas did not produce safe-state CSV")
        got = sha256(produced)
        if got != EXPECTED_SAFE_CSV_SHA:
            raise RuntimeError(f"D10000 safe-state SHA mismatch: {got}")
        shutil.move(str(produced), safe_csv)
        atomic_json(cache / "SAFE_ATLAS_RECEIPT.json", {
            "status": "PASS_BYTE_IDENTICAL_D10000_SAFE_STATES",
            "safe_states": EXPECTED_SAFE_STATES,
            "csv_sha256": got,
        })

    if sha256(safe_csv) != EXPECTED_SAFE_CSV_SHA:
        raise RuntimeError("cached D10000 safe-state CSV failed SHA")

    keys: list[int] = []
    with safe_csv.open(newline="") as fh:
        for row in csv.DictReader(fh):
            keys.append(pack(int(row["a"]), int(row["b"])))
    keys = sorted(set(keys))
    if len(keys) != EXPECTED_SAFE_STATES:
        raise RuntimeError(f"safe-state count mismatch: {len(keys)}")
    tmp = safe_bin.with_suffix(".bin.tmp")
    with tmp.open("wb") as fh:
        for k in keys:
            fh.write(struct.pack("<Q", k))
    os.replace(tmp, safe_bin)
    return safe_bin, set(keys)


def historical_rows(path: Path) -> dict[int, dict[str, str]]:
    with path.open(newline="") as fh:
        return {int(r["time"]): r for r in csv.DictReader(fh)}


def load_sources(partition: Path) -> dict[int, list[tuple[int, int]]]:
    by_time: dict[int, list[tuple[int, int]]] = defaultdict(list)
    n = 0
    with partition.open(newline="") as fh:
        for row in csv.DictReader(fh):
            if row["class"] != "UNRESOLVED_BULK_D10000":
                continue
            a, b = map(int, row["alternate_state"].split("/"))
            by_time[int(row["depth"])].append((a, b))
            n += 1
    if n != 59:
        raise RuntimeError(f"expected 59 residual sources, got {n}")
    return by_time


def source_file(root: Path, i: int) -> Path:
    p = root / f"b{i:04d}.bin"
    if not p.exists():
        raise FileNotFoundError(p)
    return p


def aggregate_worker_metrics(worker_dir: Path) -> dict[str, int]:
    rows = [json.loads(p.read_text()) for p in sorted(worker_dir.glob("s[0-9][0-9][0-9][0-9].json"))]
    if len(rows) != BUCKETS:
        raise RuntimeError(f"expected {BUCKETS} worker receipts, got {len(rows)}")
    keys = [
        "source_states","raw_children","inadmissible","hits","terminal_pruned",
        "safe_pruned","viability_pruned","emitted_before_run_dedup","runs",
    ]
    out = {k: sum(int(r[k]) for r in rows) for k in keys}
    return out


def add_injected_sources(
    run_root: Path,
    child_time: int,
    sources: list[tuple[int, int]],
    safe: set[int],
) -> int:
    by_bucket: dict[int, list[int]] = defaultdict(list)
    for a, b in sources:
        k = pack(a, b)
        if target(a, b):
            raise RuntimeError(f"residual source is already target at t={child_time}: {a}/{b}")
        if k in TERMINALS:
            raise RuntimeError(f"residual source is terminal at t={child_time}: {a}/{b}")
        if k in safe:
            raise RuntimeError(f"residual source is D10000-safe at t={child_time}: {a}/{b}")
        if not viable(b, child_time):
            raise RuntimeError(f"residual source is nonviable at t={child_time}: {a}/{b}")
        d = splitmix64(k) & (BUCKETS - 1)
        by_bucket[d].append(k)
    for d, vals in by_bucket.items():
        vals = sorted(set(vals))
        dd = run_root / f"d{d:04d}"
        dd.mkdir(parents=True, exist_ok=True)
        p = dd / f"inject_t{child_time:03d}.bin"
        with p.open("wb") as fh:
            for k in vals:
                fh.write(struct.pack("<Q", k))
    return len(sources)


def run_workers(
    engine: Path,
    source_root: Path,
    run_root: Path,
    source_time: int,
    safe_bin: Path,
    jobs: int,
    buffer_keys: int,
) -> dict[str, int]:
    run_root.mkdir(parents=True, exist_ok=True)
    logs = run_root.parent / "logs"
    logs.mkdir(parents=True, exist_ok=True)

    def one(i: int):
        run([
            str(engine), "worker",
            "--src", str(source_file(source_root, i)),
            "--src-bucket", str(i),
            "--run-root", str(run_root),
            "--source-time", str(source_time),
            "--buffer-keys", str(buffer_keys),
            "--safe-bin", str(safe_bin),
        ], logs / f"worker_{i:04d}.log")

    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(one, range(BUCKETS)))
    return aggregate_worker_metrics(run_root / "workers")


def merge_candidates(
    engine: Path,
    run_root: Path,
    candidate_root: Path,
    merge_jobs: int,
    fanin: int,
) -> list[dict]:
    candidate_root.mkdir(parents=True, exist_ok=True)
    logs = candidate_root.parent / "merge_logs"
    logs.mkdir(parents=True, exist_ok=True)

    def one(i: int):
        p = candidate_root / f"b{i:04d}.bin"
        run([
            str(engine), "merge",
            "--run-dir", str(run_root / f"d{i:04d}"),
            "--out", str(p),
            "--dst-bucket", str(i),
            "--fanin", str(fanin),
            "--delete-inputs",
        ], logs / f"merge_{i:04d}.log")
        return json.loads(Path(str(p) + ".json").read_text())

    with concurrent.futures.ThreadPoolExecutor(max_workers=merge_jobs) as ex:
        return list(ex.map(one, range(BUCKETS)))


def compare_exact(label: str, got: dict, expected: dict, fields: list[str]) -> None:
    bad = []
    for f in fields:
        gv = int(got[f])
        ev = int(expected[f])
        if gv != ev:
            bad.append((f, gv, ev))
    if bad:
        raise RuntimeError(f"{label} historical mismatch: {bad}")


def stage_a_earliest(
    repo: Path,
    root: Path,
    engine: Path,
    seen_filter: Path,
    safe_bin: Path,
    safe_set: set[int],
    jobs: int,
    merge_jobs: int,
    buffer_keys: int,
    fanin: int,
    stop_time: int,
) -> Path:
    phase = root / "earliest"
    phase.mkdir(parents=True, exist_ok=True)
    ref_path = repo / "data/stage_a/RGPHI_GLOBAL_EARLIEST_ARRIVAL_1_171.csv"
    if sha256(ref_path) != EXPECTED_EARLIEST_SHA:
        raise RuntimeError("historical earliest-arrival CSV SHA mismatch")
    expected = historical_rows(ref_path)
    sources = load_sources(repo / "data/stage_a/RGPHI_FIRST_DIVERGENCE_PARTITION_0_88.csv")

    current_meta = phase / "CURRENT.json"
    if current_meta.exists():
        cur = json.loads(current_meta.read_text())
        t0 = int(cur["time"])
        state = phase / cur["state_dir"]
    else:
        state = phase / "state_t000"
        if state.exists():
            shutil.rmtree(state)
        empty_bucket_set(state / "frontier")
        empty_bucket_set(state / "seen")
        atomic_json(state / "metrics.json", {"time": 0, "new_frontier": 0, "cumulative_seen": 0})
        atomic_json(current_meta, {"time": 0, "state_dir": state.name})
        t0 = 0

    for t in range(t0 + 1, min(stop_time, 171) + 1):
        tmp = phase / f"tmp_t{t:03d}"
        out = phase / f"state_t{t:03d}"
        if out.exists():
            shutil.rmtree(out)
        if tmp.exists():
            shutil.rmtree(tmp)
        run_root = tmp / "runs"
        candidate = tmp / "candidate"
        started = time.time()
        if t > 1:
            wm = run_workers(
                engine, state / "frontier", run_root, t - 1, safe_bin,
                jobs, buffer_keys,
            )
        else:
            wm = {k: 0 for k in [
                "source_states","raw_children","inadmissible","hits","terminal_pruned",
                "safe_pruned","viability_pruned","emitted_before_run_dedup","runs",
            ]}
            run_root.mkdir(parents=True)
        source_candidates = add_injected_sources(run_root, t, sources.get(t, []), safe_set)
        merge_candidates(engine, run_root, candidate, merge_jobs, fanin)

        (out / "frontier").mkdir(parents=True)
        (out / "seen").mkdir(parents=True)
        (out / "bucket_metrics").mkdir(parents=True)
        def filt(i: int):
            mp = out / "bucket_metrics" / f"b{i:04d}.json"
            run([
                str(seen_filter),
                "--candidate", str(candidate / f"b{i:04d}.bin"),
                "--seen", str(state / "seen" / f"b{i:04d}.bin"),
                "--new", str(out / "frontier" / f"b{i:04d}.bin"),
                "--seen-out", str(out / "seen" / f"b{i:04d}.bin"),
                "--metrics", str(mp),
            ])
            return json.loads(mp.read_text())
        with concurrent.futures.ThreadPoolExecutor(max_workers=merge_jobs) as ex:
            bm = list(ex.map(filt, range(BUCKETS)))

        max_row = max(
            bm,
            key=lambda r: int(r["max_q_num"]) / max(1, int(r["max_q_den"])),
        )
        got = {
            "time": t,
            "new_frontier": sum(int(r["new_frontier"]) for r in bm),
            "cumulative_seen": sum(int(r["seen_output"]) for r in bm),
            "raw_generated": int(wm["raw_children"]),
            "source_candidates": source_candidates,
            "dominated": sum(int(r["overlap_seen"]) for r in bm),
            "pruned_viability": int(wm["viability_pruned"]),
            "pruned_safe": int(wm["safe_pruned"]),
            "pruned_terminal": int(wm["terminal_pruned"]),
            "max_den": max(int(r["max_denominator"]) for r in bm),
            "max_q_num": int(max_row["max_q_num"]),
            "max_q_den": int(max_row["max_q_den"]),
            "hits": int(wm["hits"]),
            "seconds_rebuild": time.time() - started,
        }
        exp = expected[t]
        compare_exact(f"t={t}", got, exp, [
            "new_frontier","cumulative_seen","raw_generated","source_candidates",
            "dominated","pruned_viability","pruned_safe","pruned_terminal",
            "max_den","max_q_num","max_q_den","hits",
        ])
        got["historical_match"] = True
        atomic_json(out / "metrics.json", got)
        atomic_json(current_meta, {"time": t, "state_dir": out.name})
        old = state
        state = out
        if old.name != "state_t000" and old.exists():
            shutil.rmtree(old)
        if tmp.exists():
            shutil.rmtree(tmp)
        print(json.dumps(got, indent=2), flush=True)

    return state


def scan_bucket_count_and_sha(root: Path) -> tuple[int, int, list[tuple[str, str, int]]]:
    rows = []
    states = 0
    total_bytes = 0
    for i in range(BUCKETS):
        p = root / f"b{i:04d}.bin"
        nbytes = p.stat().st_size
        if nbytes % 8:
            raise RuntimeError(f"misaligned bucket {p}")
        count = nbytes // 8
        states += count
        total_bytes += nbytes
        rows.append((sha256(p), f"cur/b{i:04d}.bin", count))
    return states, total_bytes, rows


def stage_a_envelope(
    repo: Path,
    root: Path,
    engine: Path,
    safe_bin: Path,
    source_frontier: Path,
    jobs: int,
    merge_jobs: int,
    buffer_keys: int,
    fanin: int,
    stop_time: int,
) -> Path:
    phase = root / "envelope"
    phase.mkdir(parents=True, exist_ok=True)
    ref = repo / "data/stage_a/RGPHI_HYBRID_LEVEL_ENVELOPE_171_185.csv"
    if sha256(ref) != EXPECTED_HYBRID_SHA:
        raise RuntimeError("historical hybrid CSV SHA mismatch")
    expected = historical_rows(ref)

    current_meta = phase / "CURRENT.json"
    if current_meta.exists():
        cur = json.loads(current_meta.read_text())
        t0 = int(cur["time"])
        source = phase / cur["level_dir"] / "cur"
    else:
        t0 = 171
        source = source_frontier
        atomic_json(current_meta, {"time": 171, "level_dir": "EXTERNAL_T171"})

    for child_time in range(t0 + 1, min(stop_time, 185) + 1):
        source_time = child_time - 1
        tmp = phase / f"level_{child_time:03d}.tmp"
        final = phase / f"level_{child_time:03d}"
        if final.exists():
            shutil.rmtree(final)
        if tmp.exists():
            shutil.rmtree(tmp)
        run_root = tmp / "runs"
        candidate = tmp / "cur"
        started = time.time()
        wm = run_workers(
            engine, source, run_root, source_time, safe_bin,
            jobs, buffer_keys,
        )
        metas = merge_candidates(engine, run_root, candidate, merge_jobs, fanin)
        states = sum(int(m["count"]) for m in metas)
        nbytes = sum(int(m["bytes"]) for m in metas)
        got = {
            "time": child_time,
            "frontier_states": states,
            "raw_generated": int(wm["raw_children"]),
            "pruned_viability": int(wm["viability_pruned"]),
            "pruned_safe": int(wm["safe_pruned"]),
            "pruned_terminal": int(wm["terminal_pruned"]),
            "hits": int(wm["hits"]),
            "bytes": nbytes,
            "seconds_rebuild": time.time() - started,
        }
        exp = expected[child_time]
        compare_exact(f"envelope t={child_time}", got, exp, [
            "frontier_states","raw_generated","pruned_viability",
            "pruned_safe","pruned_terminal","hits",
        ])
        if got["hits"]:
            raise RuntimeError(f"unexpected target hit at t={child_time}")
        got["historical_match"] = True
        atomic_json(tmp / "metrics.json", got)
        if run_root.exists():
            shutil.rmtree(run_root)
        os.sync()
        tmp.rename(final)
        atomic_json(current_meta, {"time": child_time, "level_dir": final.name})
        if source.parent.parent == phase and source.parent.name.startswith("level_"):
            old = source.parent
            if old.exists() and old != final:
                shutil.rmtree(old)
        source = final / "cur"
        print(json.dumps(got, indent=2), flush=True)

    return source.parent


def finalize_checkpoint(repo: Path, level185: Path, checkpoint_root: Path) -> None:
    if checkpoint_root.exists():
        shutil.rmtree(checkpoint_root)
    checkpoint_root.mkdir(parents=True)
    shutil.move(str(level185 / "cur"), checkpoint_root / "cur")
    states, nbytes, rows = scan_bucket_count_and_sha(checkpoint_root / "cur")
    manifest = checkpoint_root / "RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt"
    with manifest.open("w") as fh:
        for digest, name, _ in rows:
            fh.write(f"{digest}  {name}\n")
    manifest_sha = sha256(manifest)
    identity = {
        "time": 185,
        "states": states,
        "buckets": BUCKETS,
        "packed_state_bytes": 8,
        "total_bytes": nbytes,
        "partition": "SplitMix64 & 127; each bucket sorted unique uint64 packed (a<<32)|b",
        "bucket_hash_manifest": manifest.name,
        "bucket_manifest_sha256": manifest_sha,
        "rebuild": "from zero with historical per-level exact checks",
    }
    atomic_json(checkpoint_root / "RGPHI_FRONTIER185_CHECKPOINT_MANIFEST.json", identity)
    if states != EXPECTED_T185_STATES:
        raise RuntimeError(f"t185 state count mismatch: {states}")
    if nbytes != EXPECTED_T185_BYTES:
        raise RuntimeError(f"t185 byte count mismatch: {nbytes}")
    if manifest_sha != EXPECTED_T185_MANIFEST_SHA:
        raise RuntimeError(f"t185 manifest SHA mismatch: {manifest_sha}")
    atomic_json(checkpoint_root / "REBUILD_ACCEPTANCE.json", {
        "status": "PASS_BYTE_EXACT_STAGE_A_REBUILD",
        "states": states,
        "bytes": nbytes,
        "manifest_sha256": manifest_sha,
    })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--drive-root", type=Path, required=True)
    ap.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--jobs", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    ap.add_argument("--merge-jobs", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    ap.add_argument("--buffer-keys", type=int, default=65536)
    ap.add_argument("--fanin", type=int, default=64)
    ap.add_argument("--stop-time", type=int, default=185)
    ap.add_argument("--reset", action="store_true")
    ns = ap.parse_args()

    repo = ns.repo_root.resolve()
    root = ns.drive_root.resolve()
    rebuild = root / "stage_a_rebuild"
    if ns.reset and rebuild.exists():
        shutil.rmtree(rebuild)
    rebuild.mkdir(parents=True, exist_ok=True)

    engine, seen_filter, trap = compile_tools(repo, Path("/content/rgphi_rebuild_bin"))
    safe_bin, safe_set = prepare_safe_states(repo, rebuild, trap)

    earliest_state = stage_a_earliest(
        repo, rebuild, engine, seen_filter, safe_bin, safe_set,
        ns.jobs, ns.merge_jobs, ns.buffer_keys, ns.fanin, ns.stop_time,
    )
    if ns.stop_time <= 171:
        return 0

    level185 = stage_a_envelope(
        repo, rebuild, engine, safe_bin, earliest_state / "frontier",
        ns.jobs, ns.merge_jobs, ns.buffer_keys, ns.fanin, ns.stop_time,
    )
    if ns.stop_time < 185:
        return 0

    checkpoint_root = root / "checkpoint_t185_rebuilt"
    finalize_checkpoint(repo, level185, checkpoint_root)
    print(json.dumps({
        "status": "PASS_BYTE_EXACT_STAGE_A_REBUILD",
        "checkpoint_root": str(checkpoint_root),
        "manifest_sha256": EXPECTED_T185_MANIFEST_SHA,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
