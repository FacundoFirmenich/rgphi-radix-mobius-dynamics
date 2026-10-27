#!/usr/bin/env python3
"""Build local archival and arXiv release artifacts."""
from __future__ import annotations

import hashlib
import json
import tarfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
PREFIX = f'rgphi-radix-mobius-dynamics-{VERSION}'
EXCLUDED = {'.git', 'dist', 'build', '.venv', '.pytest_cache', '.ruff_cache', '__pycache__'}


def included_files() -> list[Path]:
    paths = []
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED for part in rel.parts):
            continue
        if path.suffix in {'.aux', '.log', '.out', '.fls', '.fdb_latexmk'}:
            continue
        paths.append(path)
    return sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for old in DIST.iterdir():
        if old.is_file():
            old.unlink()

    source_zip = DIST / f'{PREFIX}.zip'
    with zipfile.ZipFile(source_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in included_files():
            zf.write(path, arcname=f'{PREFIX}/{path.relative_to(ROOT).as_posix()}')

    source_tar = DIST / f'{PREFIX}.tar.gz'
    with tarfile.open(source_tar, 'w:gz', compresslevel=9) as tf:
        for path in included_files():
            tf.add(path, arcname=f'{PREFIX}/{path.relative_to(ROOT).as_posix()}', recursive=False)

    arxiv_zip = DIST / 'RGPHI_PAPER_I_ARXIV_SOURCE_v1.zip'
    with zipfile.ZipFile(arxiv_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.write(ROOT / 'paper/main.tex', arcname='main.tex')
        zf.write(ROOT / 'paper/README.md', arcname='README.txt')
        zf.write(ROOT / 'LICENSE-DOCS.md', arcname='LICENSE-DOCS.md')

    paper_pdf = DIST / 'RGPHI_PAPER_I_v1.pdf'
    paper_pdf.write_bytes((ROOT / 'paper/main.pdf').read_bytes())

    records = []
    for path in sorted(DIST.iterdir()):
        if path.is_file():
            records.append({'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha256(path)})
    (DIST / 'RELEASE_ARTIFACTS.json').write_text(json.dumps({'version': VERSION, 'artifacts': records}, indent=2) + '\n', encoding='utf-8')
    checksum_paths = sorted(p for p in DIST.iterdir() if p.is_file() and p.name != 'SHA256SUMS.txt')
    (DIST / 'SHA256SUMS.txt').write_text('\n'.join(f'{sha256(p)}  {p.name}' for p in checksum_paths) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'dist': str(DIST), 'artifacts': records}, indent=2))


if __name__ == '__main__':
    main()
