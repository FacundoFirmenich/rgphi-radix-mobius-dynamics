#!/usr/bin/env python3
"""Run the exact Stage-B2 smoke twice and compare semantic manifests."""
from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE / "_determinism"
REC = struct.Struct("<Q")
BUCKETS = 128
STATES = {(586, 805), (528, 857), (1229, 2269), (1073, 1333), (534, 1567)}


def pack(a: int, b: int) -> int:
    return (a << 32) | b


def mix64(x: int) -> int:
    mask = (1 << 64) - 1
    x = (x + 0x9E3779B97F4A7C15) & mask
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & mask
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & mask
    return x ^ (x >> 31)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_checkpoint() -> tuple[Path, Path]:
    checkpoint = ROOT / "checkpoint"
    current = checkpoint / "cur"
    current.mkdir(parents=True)
    buckets: list[list[int]] = [[] for _ in range(BUCKETS)]
    for a, b in STATES:
        buckets[mix64(pack(a, b)) & 127].append(pack(a, b))
    lines = []
    for index, values in enumerate(buckets):
        path = current / f"b{index:04d}.bin"
        path.write_bytes(b"".join(REC.pack(value) for value in sorted(values)))
        lines.append(f"{sha256(path)}  cur/{path.name}")
    manifest = ROOT / "hashes.txt"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return checkpoint, manifest


def execute(checkpoint: Path, manifest: Path, name: str) -> list[str]:
    work = ROOT / name
    command = [
        sys.executable,
        str(HERE / "run_stage_b2.py"),
        "--checkpoint-root", str(checkpoint),
        "--hash-manifest", str(manifest),
        "--work-root", str(work),
        "--start-time", "83",
        "--end-time", "90",
        "--jobs", "2",
        "--merge-jobs", "2",
        "--minimum-free-gb", "0",
        "--allow-noncanonical",
        "--full-checkpoint-audit",
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
    return [sha256(work / f"level_{time:03d}" / "manifest.json") for time in range(84, 91)]


def main() -> None:
    if ROOT.exists():
        shutil.rmtree(ROOT)
    ROOT.mkdir()
    checkpoint, manifest = build_checkpoint()
    left = execute(checkpoint, manifest, "run-a")
    right = execute(checkpoint, manifest, "run-b")
    assert left == right
    print(json.dumps({"status": "PASS", "semantic_manifest_hashes": left}, indent=2))


if __name__ == "__main__":
    main()
