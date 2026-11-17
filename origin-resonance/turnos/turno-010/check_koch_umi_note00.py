#!/usr/bin/env python3
from fractions import Fraction
from math import log

# A planar vector is represented as (x, y_coeff), meaning x + i*sqrt(3)*y_coeff.

def generator_vectors(sigma: int):
    if sigma not in (-1, 0, 1):
        raise ValueError("sigma must be -1, 0 or +1")
    if sigma == 0:
        return [(Fraction(1, 4), Fraction(0)) for _ in range(4)]
    return [
        (Fraction(1, 3), Fraction(0)),
        (Fraction(1, 6), Fraction(sigma, 6)),
        (Fraction(1, 6), Fraction(-sigma, 6)),
        (Fraction(1, 3), Fraction(0)),
    ]

for sigma in (-1, 0, 1):
    vv = generator_vectors(sigma)
    assert sum(v[0] for v in vv) == 1
    assert sum(v[1] for v in vv) == 0

# Standard active Koch dimension.
D = log(4) / log(3)
assert abs(4 * (1 / 3) ** D - 1) < 1e-14
assert 1 < D < 2

# Symbolic mixed local-dimension endpoints.
def mixed_dimension(p0: float) -> float:
    return log(4) / (p0 * log(4) + (1 - p0) * log(3))

assert abs(mixed_dimension(1.0) - 1.0) < 1e-14
assert abs(mixed_dimension(0.0) - D) < 1e-14
assert mixed_dimension(0.75) < mixed_dimension(0.25)

print("PASS_KOCH_UMI_NOTA00")
print("tripolar_generators=endpoints_preserved")
print("sigma0=latent_ratio_1/4")
print("sigma+-=active_ratio_1/3")
print("koch_dimension=log(4)/log(3)")
print("standard_koch=MONOFRACTAL")
print("branch_dependent_sigma=MULTIFRACTAL_CANDIDATE")
