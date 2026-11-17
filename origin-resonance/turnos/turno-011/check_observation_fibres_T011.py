#!/usr/bin/env python3
"""Turno 011: exact finite checks of the stated cell-fibre cardinalities.
Not an empirical simulation or an independent proof of the asymptotic theorem.
"""
from itertools import product
from math import gcd

def binary_key_bits(cardinality: int) -> int:
    if cardinality < 1:
        raise ValueError("nonempty observation fibre required")
    return (cardinality - 1).bit_length()

for N in range(1, 9):
    all_labels = set(product((-1, 0, 1), repeat=N))
    coherent = {tuple([sigma] * N) for sigma in (-1, 0, 1)}
    assert len(all_labels) == 3 ** N
    assert len(coherent) == 3
    assert binary_key_bits(len(all_labels)) == (3 ** N - 1).bit_length()
    assert binary_key_bits(len(coherent)) == 2
    assert binary_key_bits(len(all_labels)) >= N  # extensive lower bound

for n in range(40):
    c = 40 * 10 ** n
    assert gcd(gcd(c - 3, c), c + 3) == 1
    assert (c - 3) + (c + 3) == 2 * c

print("PASS_T011_ENDPOINT_FIBRES_N1_TO_N8")
print("PASS_T011_PRIMITIVE_SHADOW_N0_TO_N39")
print("JURISDICTION=CONDITIONAL_ENDPOINTS_OBSERVER")
print("FST11_EXTERNAL_CORPUS=NOT_REPRODUCED")
