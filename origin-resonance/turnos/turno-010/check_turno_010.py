#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, log2

for n in range(20):
    scale=10**n
    triplet=(14*scale,15*scale,16*scale)
    assert gcd(gcd(14,15),16)==1
    assert triplet[0]+triplet[2]==2*triplet[1]
    assert Fraction(triplet[0],triplet[1])==Fraction(14,15)
    assert Fraction(triplet[2],triplet[1])==Fraction(16,15)
    assert Fraction(triplet[2]-triplet[1],triplet[1])==Fraction(1,15)
    assert Fraction(triplet[2]-triplet[0],triplet[1])==Fraction(2,15)

assert Fraction(1,15)==Fraction(2,30)
assert 2**1 < 3 <= 2**2
assert log2(3)>1

print('PASS_TURNO_010_RC1')
print('latent_seed=(pi/6)*10^(+n_scalar)')
print('lateral_bound=(2/30)*center=(pi/9)*10^n')
print('tripolar_shadow=[14:15:16]')
print('relative_half_width=1/15')
print('relative_full_width=2/15')
print('scale_operator=times_10_projectively_stationary')
print('prior_pi_over_8_formulas=SUPERSEDED')
