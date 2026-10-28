#!/usr/bin/env python3
"""Check local Markdown links in the RGΦ repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def iter_markdown_files() -> list[Path]:
    roots = [ROOT / "README.md", ROOT / "RELEASE.md", ROOT / "REPRODUCIBILITY.md"]
    roots.extend((ROOT / "docs").rglob("*.md"))
    roots.extend((ROOT / "paper").rglob("*.md"))
    roots.extend((ROOT / "metadata").rglob("*.md"))
    return sorted({path for path in roots if path.is_file()})


def strip_fenced_code(text: str) -> str:
    kept: list[str] = []
    in_fence = False
    fence = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            continue
        if not in_fence:
            kept.append(line)
    return "\n".join(kept)


def local_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if not target:
        return None
    # Remove an optional Markdown title after a whitespace separator.
    if " " in target and not target.startswith("#"):
        target = target.split()[0]
    if target.startswith("#") or target.startswith("//") or SCHEME_RE.match(target):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target) or None


def check_all() -> list[dict[str, str | int]]:
    errors: list[dict[str, str | int]] = []
    for source in iter_markdown_files():
        text = strip_fenced_code(source.read_text(encoding="utf-8"))
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = local_target(match.group(1))
                if target is None:
                    continue
                candidate = (ROOT / target.lstrip("/")) if target.startswith("/") else (source.parent / target)
                candidate = candidate.resolve()
                try:
                    candidate.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append({"source": str(source.relative_to(ROOT)), "line": line_number, "target": target, "error": "escapes repository root"})
                    continue
                if not candidate.exists():
                    errors.append({"source": str(source.relative_to(ROOT)), "line": line_number, "target": target, "error": "missing local target"})
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    errors = check_all()
    report = {
        "status": "PASS" if not errors else "FAIL",
        "markdown_files_checked": len(iter_markdown_files()),
        "broken_links": errors,
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
