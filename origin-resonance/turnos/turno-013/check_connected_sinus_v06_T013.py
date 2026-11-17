#!/usr/bin/env python3
"""Independent exact narrow audit of connected sinus-pi v0.6 source claims.

Jurisdiction: symbolic phase coders and free nonnegative depth recurrence;
NOT a theorem about the actual pi orbit, measurements, or original FST syntax.
"""
from fractions import Fraction as F
from itertools import product
from math import log, log2

MULTIPLIERS = (5, 9, 10, 12, 15)
DIGITS = (2, 3, 4, 5, 12, 15, 18, 19, 23, 24, 29, 31, 32, 35, 36,
          37, 38, 39, 43, 45, 49, 52, 57, 62, 63, 64, 65, 69, 71,
          72, 79, 82, 85, 95, 96, 97, 98)
assert len(DIGITS) == len(set(DIGITS)) == 37

def uniform_strict_bound(m):
    # Pi < 22/7 and x-sin(x) < x^3/6, no numerical pi sampling.
    return 10**10 * F(m, 500)**3 * F(22, 7)**3 / F(6*180**3)

def check_invariant_cantor():
    # A base-100 infinite tail supported on DIGITS lies in [2/99,98/99].
    margins = []
    for d in DIGITS:
        lo = F(99*d + min(DIGITS), 9900)
        hi = F(99*d + max(DIGITS), 9900)
        for m in MULTIPLIERS:
            q = (m*lo).__floor__()
            # The whole cell avoids an integer and the n-dependent threshold.
            margins.append(min(m*lo - q - uniform_strict_bound(m), q+1-m*hi))
    least = min(margins)
    assert least == F(89, 1131900), least
    assert least > 0
    # Disjoint base-100 similitudes: dim_H = log(37)/log(100).
    return least

def classify(advances, borrow_bits):
    assert len(borrow_bits) == len(advances)+1
    D = [0]
    for a in advances:
        D.append(D[-1] + 2 - a)
    candidates = {-v for v, b in zip(D, borrow_bits) if b == 0}
    if len(candidates) > 1:
        return 'INCONSISTENT'
    if candidates:
        initial = next(iter(candidates))
        J = [initial + delta for delta in D]
        if any(x < 0 or int(x > 0) != b for x, b in zip(J, borrow_bits)):
            return 'INCONSISTENT'
        return 'UNIQUE'
    return 'NOT_IDENTIFIABLE'

def check_depths():
    counts = {'UNIQUE': 0, 'INCONSISTENT': 0, 'NOT_IDENTIFIABLE': 0}
    # Check the closed-form classifier against direct feasible initial depths.
    for n in range(5):
        for advances in product(range(6), repeat=n):
            D = [0]
            for a in advances:
                D.append(D[-1] + 2 - a)
            Cmax = max(40, max(abs(x) for x in D) + 40)
            for bits in product((0,1), repeat=n+1):
                feasible = [c for c in range(Cmax+1)
                            if all(c+x >= 0 and int(c+x > 0) == b
                                   for x,b in zip(D,bits))]
                actual = 'INCONSISTENT' if not feasible else (
                    'NOT_IDENTIFIABLE' if all(bits) else 'UNIQUE')
                observed = classify(advances, bits)
                assert actual == observed, (advances,bits,actual,observed)
                counts[observed] += 1
    assert counts == {'UNIQUE':1555,'NOT_IDENTIFIABLE':1555,'INCONSISTENT':42132}
    return counts

def main():
    least = check_invariant_cantor()
    counts = check_depths()
    assert 343 == 18**2+18+1 == 7**3
    assert 343 == 9*36+19 == 10*36-17 and 343**2 % 36 == 1
    print('PASS_T013_CONNECTED_SINUS_V06_INDEPENDENT_NARROW')
    print('strict_Cantor_min_margin=', least)
    print('Cantor_Hausdorff_dim=', log(37)/log(100))
    print('uniform_phase_info_lower_bits_per_base100_step=', log2(100/13))
    print('independent_free_depth_contracts=',sum(counts.values()),counts)
    print('BOUNDARY: FST/UMI causal bridge, actual pi orbit, 3M atlas, CI and 48 tests NOT VERIFIED')

if __name__ == '__main__':
    main()
