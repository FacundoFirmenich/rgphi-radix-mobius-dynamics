#!/usr/bin/env python3
"""Independent Burnside/orbit audit of Turno-006 six-state balanced words.

A directed labelled cycle is quotiented by cyclic rotations, not by
reflection, unless an additional equivalence theorem is provided.
This audit is intentionally fail-closed against the existing table.
"""
from itertools import combinations
from pathlib import Path
import csv

def rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}

def necklace(w):
    return min(rotations(w))

def bracelet(w):
    return min(rotations(w) | rotations(w[::-1]))

words = {
    "".join("T" if i in indices else "S" for i in range(6))
    for indices in combinations(range(6), 3)
}
necklaces = {necklace(w) for w in words}
bracelets = {bracelet(w) for w in words}
orbit_sizes = sorted(len(rotations(w)) for w in necklaces)

assert len(words) == 20
assert len(necklaces) == 4, necklaces
assert orbit_sizes == [2, 6, 6, 6], orbit_sizes
assert len(bracelets) == 3, bracelets
assert sum(orbit_sizes) == 20
assert necklace("TTSTSS") != necklace("TTSSTS")
assert bracelet("TTSTSS") == bracelet("TTSSTS")

table = Path(__file__).with_name("SIX_STATE_SKELETON_COUNTS.csv")
with table.open(newline="") as f:
    existing = [r["word"] for r in csv.DictReader(f)]
listed_necklaces = {necklace(w) for w in existing}
missing = sorted(necklaces - listed_necklaces)
extra = sorted(listed_necklaces - necklaces)
print("EXACT_BALANCED_WORDS=20")
print("EXACT_ROTATIONAL_NECKLACES=4")
print("EXACT_DIHEDRAL_BRACELETS=3")
print("ROTATIONAL_ORBIT_SIZES=2,6,6,6")
print("MISSING_ROTATIONAL_CLASSES=" + ",".join(missing))
print("EXTRA_ROTATIONAL_CLASSES=" + ",".join(extra))
if missing or extra:
    raise SystemExit(
        "AUDIT_HOLD: Turno-006 declares three necklaces, but these are three "
        "dihedral bracelet classes; an oriented-cycle reversal quotient "
        "requires its own exact justification."
    )
print("PASS_ROTATIONAL_CATALOGUE_COMPLETE")
