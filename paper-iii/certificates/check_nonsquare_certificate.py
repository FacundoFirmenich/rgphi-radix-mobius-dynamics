#!/usr/bin/env python3
from math import isqrt

MODULI = [68, 55, 71]
SQUARE_RESIDUES = {m: {(x * x) % m for x in range(m)} for m in MODULI}

for j in range(1, 38):
    value = 403 * j * j + 15314 * j + 190969
    assert isqrt(value) ** 2 != value
    assert any(value % m not in SQUARE_RESIDUES[m] for m in MODULI)

print("PASS")
print("j_range=1..37")
print("moduli=68,55,71")
