#!/usr/bin/env python3
"""Generate canonical repository manifest and SHA-256 ledger."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {'.git', 'dist', 'build', '.venv', '.pytest_cache', '.ruff_cache', '__pycache__'}
EXCLUDED_FILES = {'MANIFEST.json', 'SHA256SUMS.txt'}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def included_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        if path.suffix in {'.aux', '.log', '.out', '.fls'}:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def main() -> None:
    records = []
    for path in included_files():
        rel = path.relative_to(ROOT).as_posix()
        records.append({'path': rel, 'bytes': path.stat().st_size, 'sha256': sha256(path)})
    manifest = {
        'schema_version': '1.0',
        'project': 'RGPhi rational radix-Mobius dynamics research compendium',
        'version': (ROOT / 'VERSION').read_text(encoding='utf-8').strip(),
        'generated_date': '2026-10-27',
        'file_count': len(records),
        'files': records,
    }
    manifest_path = ROOT / 'MANIFEST.json'
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    checksum_paths = included_files() + [manifest_path]
    lines = [f'{sha256(path)}  {path.relative_to(ROOT).as_posix()}' for path in sorted(checksum_paths, key=lambda p: p.relative_to(ROOT).as_posix())]
    (ROOT / 'SHA256SUMS.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'file_count': len(records), 'manifest_sha256': sha256(manifest_path)}, indent=2))


if __name__ == '__main__':
    main()
