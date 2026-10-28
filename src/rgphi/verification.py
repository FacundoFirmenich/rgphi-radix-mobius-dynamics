"""Repository-level exact verification."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json

from .dynamics import S, T, complement, seed_family_successor
from .thresholds import intersect, load_benchmark_intervals, load_nonnesting_intervals
from .traps import C8, audit_finite_trap, multiplicative_order


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _assert_canonical_text_sync(root: Path, canonical: dict[str, object]) -> None:
    tau5 = canonical["tau5"]
    if not isinstance(tau5, dict):
        raise TypeError("canonical tau5 record must be a mapping")
    lower = int(tau5["lower_bound"])
    upper = int(tau5["upper_bound"])

    paper = (root / "paper" / "main.tex").read_text(encoding="utf-8")
    expected_latex = rf"${lower}\le \tau_5\le{upper}$"
    if expected_latex not in paper:
        raise AssertionError(
            f"paper/main.tex is not synchronized with canonical tau5 interval {lower}..{upper}"
        )
    stale_latex = r"$179\le \tau_5\le212$"
    if stale_latex in paper and (lower, upper) != (179, 212):
        raise AssertionError("paper/main.tex retains the superseded 179..212 interval")

    status = (root / "docs" / "SCIENTIFIC_STATUS.md").read_text(encoding="utf-8")
    compact_status = "".join(status.split())
    expected_status = rf"{lower}\le\tau_5\le{upper}"
    if expected_status not in compact_status:
        raise AssertionError("docs/SCIENTIFIC_STATUS.md is not synchronized with CANONICAL_STATE")

    claim_rows = list(
        csv.DictReader(
            (root / "paper" / "claim-evidence-matrix.csv").open(
                encoding="utf-8", newline=""
            )
        )
    )
    p10 = next((row for row in claim_rows if row["claim_id"] == "P10"), None)
    if p10 is None:
        raise AssertionError("claim matrix is missing P10")
    if f"interval {lower}..{upper}" not in p10["evidence"]:
        raise AssertionError("P10 evidence interval is not synchronized with CANONICAL_STATE")


def verify_repository(root: str | Path) -> dict[str, object]:
    root = Path(root).resolve()
    threshold_dir = root / "data" / "thresholds"
    trap_dir = root / "data" / "traps"
    certificate_dir = root / "data" / "certificates"

    assert complement(Fraction(17, 20)) == T(complement(Fraction(17, 19)))
    assert S(Fraction(17, 19)) == Fraction(17, 20)
    assert T(S(Fraction(17, 19))) == Fraction(1, 2)
    assert S(T(Fraction(17, 19))) == Fraction(9, 14)

    checks = 0
    for base in range(2, 21):
        for N in range(2, 60):
            for r in range(1, N):
                seed_family_successor(N, r, base=base)
                checks += 1

    benchmark = load_benchmark_intervals(threshold_dir / "benchmark-robustness.csv")
    assert [(item.depth, item.first_time) for item in benchmark] == [
        (1, 45), (2, 85), (3, 120), (4, 162),
    ]
    common_chronology = intersect(benchmark)
    assert common_chronology == (Fraction(106197, 10000), Fraction(11643, 1000))

    nonnesting = load_nonnesting_intervals(threshold_dir / "nonnesting-robustness.csv")
    nonnesting_lower = max(row[1] for row in nonnesting)
    nonnesting_upper = min(row[2] for row in nonnesting)
    assert (nonnesting_lower, nonnesting_upper) == (
        Fraction(106197, 10000), Fraction(1101, 100),
    )

    c8 = audit_finite_trap(C8)
    assert c8["size"] == 8 and c8["max_q"] == "13"
    assert multiplicative_order(10, 13) == 6
    assert multiplicative_order(10, 11) == 2

    terminal_audit = json.loads(
        (certificate_dir / "terminal-set-audit.json").read_text(encoding="utf-8")
    )
    assert terminal_audit["terminal_state_count"] == 23
    assert terminal_audit["branch_checks"] == 46
    assert terminal_audit["admissible_escapes"] == 0
    assert terminal_audit["all_admissible_children_terminal"] is True

    trap_result = json.loads(
        (trap_dir / "trap-atlas-result-D500.json").read_text(encoding="utf-8")
    )
    assert trap_result["status"] == "PASS"
    assert trap_result["nonterminal_states_enumerated"] == 76094
    assert trap_result["closed_sccs_modulo_terminal_set"] == 153
    assert trap_result["exact_finite_forward_closures"] == 1502

    canonical = json.loads(
        (root / "metadata" / "CANONICAL_STATE.json").read_text(encoding="utf-8")
    )
    assert canonical["tau5"]["lower_bound"] == 186
    assert canonical["tau5"]["upper_bound"] == 212
    assert canonical["tau5"]["exact"] is None
    assert canonical["stage_b2"]["checkpoint_time"] == 185
    assert canonical["stage_b2"]["checkpoint_states"] == 2462600671
    assert canonical["stage_b2"]["checkpoint_buckets"] == 128
    assert canonical["stage_b2"]["checkpoint_bytes"] == 19700805368

    checkpoint = json.loads(
        (root / "data" / "stage_b2" / "RGPHI_FRONTIER185_CHECKPOINT_MANIFEST.json").read_text(encoding="utf-8")
    )
    assert checkpoint["time"] == canonical["stage_b2"]["checkpoint_time"]
    assert checkpoint["states"] == canonical["stage_b2"]["checkpoint_states"]
    assert checkpoint["buckets"] == canonical["stage_b2"]["checkpoint_buckets"]
    assert checkpoint["total_bytes"] == canonical["stage_b2"]["checkpoint_bytes"]
    assert checkpoint["bucket_manifest_sha256"] == canonical["stage_b2"]["checkpoint_manifest_sha256"]

    _assert_canonical_text_sync(root, canonical)

    required = [
        root / "paper" / "main.tex", root / "paper" / "main.pdf",
        root / "CITATION.cff", root / ".zenodo.json", root / "codemeta.json", root / "README.md",
    ]
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            raise FileNotFoundError(path)

    return {
        "status": "PASS",
        "seed_family_checks": checks,
        "benchmark_chronology_interval": [str(common_chronology[0]), str(common_chronology[1])],
        "robust_nonnesting_interval": [str(nonnesting_lower), str(nonnesting_upper)],
        "tau5_interval": [canonical["tau5"]["lower_bound"], canonical["tau5"]["upper_bound"]],
        "terminal_set_branch_checks": terminal_audit["branch_checks"],
        "C8_max_q": c8["max_q"],
        "paper_pdf_sha256": sha256(root / "paper" / "main.pdf"),
    }
