#!/usr/bin/env python3
"""Independent compact checker for RGΦ GLOBAL-TRAP-CUT-088 Stage A."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "stage_a"
STAGE_B2 = ROOT / "data" / "stage_b2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    receipt = json.loads((DATA / "STAGE_A_COMPACT_RECEIPT.json").read_text())
    assert receipt["status"] == "PASS_WITH_BOUNDARY"
    assert receipt["tau5_interval"] == [186, 212]

    with (DATA / "RGPHI_FIRST_DIVERGENCE_PARTITION_0_88.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 89
    classes = Counter(row["class"] for row in rows)
    assert classes == Counter({
        "UNRESOLVED_BULK_D10000": 59,
        "INADMISSIBLE": 23,
        "TERMINAL": 4,
        "FINITE_TRAP_BASIN": 3,
    })

    with (DATA / "RGPHI_EXACT_FIRST_DIVERGENCE_TRAPS.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        traps = list(csv.DictReader(stream))
    assert {(row["depth"], row["source"], row["certified_value"]) for row in traps} == {
        ("9", "5/16", "infinity"),
        ("7", "4/9", "infinity"),
        ("4", "1/14", "infinity"),
    }

    with (DATA / "RGPHI_TRAP_ATLAS_SCALING_D500_D10000.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        scale = list(csv.DictReader(stream))
    assert [int(row["D"]) for row in scale] == [500, 2500, 5000, 10000]
    assert [int(row["safe_states"]) for row in scale] == [1624, 5933, 10418, 18472]
    assert int(scale[-1]["states"]) == 30397464
    assert int(scale[-1]["edges"]) == 43771910
    assert int(scale[-1]["SCCs"]) == 9009037
    assert int(scale[-1]["closed_mod_terminal_SCCs"]) == 467

    summary = json.loads((DATA / "D10000_closed_scc_summary.json").read_text())
    assert summary["closed_scc_count"] == 467
    assert summary["max_closed_scc_size"] == 12
    assert sum(int(k) * int(v) for k, v in summary["closed_scc_size_distribution"].items()) == 1801

    with (DATA / "RGPHI_EARLIEST_CROSSCHECK_T120.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        cross = list(csv.DictReader(stream))
    assert int(cross[-1]["time"]) == 120
    assert int(cross[-1]["new"]) == 414800
    assert int(cross[-1]["seen"]) == 4141395

    with (DATA / "RGPHI_HYBRID_LEVEL_ENVELOPE_171_185.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        hybrid = list(csv.DictReader(stream))
    assert int(hybrid[0]["time"]) == 171
    assert int(hybrid[-1]["time"]) == 185
    assert int(hybrid[-1]["frontier_states"]) == 2462600671
    assert sum(int(row["hits"]) for row in hybrid) == 0
    assert max(int(row["max_q_num"]) / int(row["max_q_den"]) for row in hybrid) == 482677

    merkle = (DATA / "RGPHI_FRONTIER185_MERKLE_ROOT.sha256").read_text().split()[0]
    canonical_manifest = STAGE_B2 / "RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt"
    assert merkle == sha256(canonical_manifest)
    assert merkle == "dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7"
    assert len(canonical_manifest.read_text().splitlines()) == 128

    print("PASS_STAGE_A_COMPACT_EVIDENCE")
    print("tau5_interval=186..212")
    print("first_divergences=89: 30 structural, 59 residual")
    print("trap_atlas_D10000=30397464 states, 467 closed SCCs, 18472 safe states")
    print("exact_no_hit_through=185")


if __name__ == "__main__":
    main()
