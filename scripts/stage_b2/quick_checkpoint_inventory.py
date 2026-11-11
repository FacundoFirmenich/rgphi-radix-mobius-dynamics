#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, sys

EXPECTED_BUCKETS = 128
EXPECTED_BYTES = 19_700_805_368
EXPECTED_STATES = 2_462_600_671
EXPECTED_MANIFEST_SHA = "dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def main(root: str, manifest: str, output: str) -> int:
    root = Path(root)
    manifest = Path(manifest)
    rows = []
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        digest, name = line.split(maxsplit=1)
        name = name.strip().lstrip("*")
        m = re.search(r"b(\d{4})\.bin$", name)
        if not m:
            raise ValueError(name)
        rows.append((int(m.group(1)), digest, Path(name).name))
    rows.sort()
    errors = []
    if sha256(manifest) != EXPECTED_MANIFEST_SHA:
        errors.append("manifest_sha_mismatch")
    if len(rows) != EXPECTED_BUCKETS:
        errors.append(f"manifest_rows={len(rows)}")
    files = []
    total_bytes = 0
    for bucket, expected_sha, basename in rows:
        p = root / basename
        if not p.exists():
            errors.append(f"missing:{basename}")
            continue
        size = p.stat().st_size
        total_bytes += size
        files.append({"bucket": bucket, "name": basename, "bytes": size, "expected_sha256": expected_sha})
    if total_bytes != EXPECTED_BYTES:
        errors.append(f"total_bytes={total_bytes}")
    result = {
        "status": "INVENTORY_READY" if not errors else "BLOCKED",
        "root": str(root),
        "files_present": len(files),
        "total_bytes": total_bytes,
        "expected_states": EXPECTED_STATES,
        "errors": errors,
        "files": files,
    }
    Path(output).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "files_present", "total_bytes", "errors")}, indent=2))
    return 0 if not errors else 3

if __name__ == "__main__":
    raise SystemExit(main(*sys.argv[1:4]))
