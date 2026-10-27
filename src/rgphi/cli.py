"""Command-line interface for the RGΦ research compendium."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from pathlib import Path
import json

from .traps import build_atlas
from .verification import verify_repository


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def command_verify(args: argparse.Namespace) -> int:
    result = verify_repository(args.root)
    print(json.dumps(result, indent=2))
    return 0


def command_trap_atlas(args: argparse.Namespace) -> int:
    summary, _graph, closed, closures = build_atlas(
        denominator_bound=args.denominator_bound,
        base=args.base,
    )
    result = asdict(summary)
    result["closed_scc_sizes"] = sorted(len(item) for item in closed)
    result["closure_sizes"] = sorted(len(item) for item in closures)
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rgphi", description="Exact tools for RGΦ rational radix–Möbius dynamics")
    sub = parser.add_subparsers(dest="command", required=True)

    verify = sub.add_parser("verify", help="verify the canonical repository evidence")
    verify.add_argument("--root", type=Path, default=_repo_root())
    verify.set_defaults(func=command_verify)

    traps = sub.add_parser("trap-atlas", help="build an exact finite trap atlas")
    traps.add_argument("--base", type=int, default=10)
    traps.add_argument("--denominator-bound", type=int, default=500)
    traps.set_defaults(func=command_trap_atlas)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
