#!/usr/bin/env python3
"""Independent fail-closed rotational word-coverage check for Turno 007."""
from itertools import combinations
from pathlib import Path
import csv

def canonical_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))

words = {
    "".join("T" if i in subset else "S" for i in range(6))
    for subset in combinations(range(6), 3)
}
all_orbits = {canonical_rotation(w) for w in words}
assert len(words) == 20 and len(all_orbits) == 4
with Path(__file__).with_name("N6_LOLLIPOP_REDUCTION.csv").open(newline="") as f:
    rows = list(csv.DictReader(f))
covered = {canonical_rotation(r["word"]) for r in rows}
missing = sorted(all_orbits - covered)
print("T007_BALANCED_ROTATIONAL_ORBITS=" + str(len(all_orbits)))
print("T007_COVERED_ROTATIONAL_ORBITS=" + str(len(covered)))
print("T007_MISSING_ROTATIONAL_ORBITS=" + ",".join(missing))
if missing:
    raise SystemExit(
        "AUDIT_HOLD_T007: TSTSTS-forced inference lacks a documented "
        "highness adjudication or proven equivalence for the missing orbit."
    )
print("PASS_T007_ORBIT_COVERAGE")
