#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import csv
import gzip
import json

R = Path(__file__).resolve().parent
summary = json.loads((R / "SUMMARY_014.json").read_text())
assert summary["closed_symbolically"]["hamiltonian_TTSSS"] == "IMPOSSIBLE_SCALE_ARGUMENT"
assert summary["closed_symbolically"]["four_cycle_TTSS_plus_one"] == "IMPOSSIBLE_CORE_SCALE_ARGUMENT"
assert summary["canonical_candidate_classes"] == 560

for name, expected in [
    ("HAMILTONIAN_TSTSS_CLASSES.csv.gz", 228),
    ("FOUR_CORE_TSTS_PLUS_ONE_CLASSES.csv.gz", 332),
]:
    with gzip.open(R / name, "rt", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == expected
    assert len({row["canonical_key"] for row in rows}) == expected
    for row in rows:
        p = [Fraction(x) for x in row["p_witness"].split(";")]
        q = [Fraction(x) for x in row["q_witness"].split(";")]
        delta = Fraction(row["exact_margin"])
        assert delta > 0 and sum(q) == 1
        assert all(x >= delta for x in p)
        assert all(q[i] - p[i] >= delta and 2 * p[i] - q[i] >= delta for i in range(5))

print("PASS")
print("hamiltonian_TTSSS=SYMBOLICALLY_IMPOSSIBLE")
print("four_core_TTSS_plus_one=SYMBOLICALLY_IMPOSSIBLE")
print("hamiltonian_TSTSS_classes=228")
print("four_core_TSTS_plus_one_classes=332")
print("five_state_rigidity=OPEN_PARTIAL")
