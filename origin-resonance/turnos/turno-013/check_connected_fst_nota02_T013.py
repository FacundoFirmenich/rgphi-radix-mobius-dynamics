#!/usr/bin/env python3
"""Independent finite/exact checks. This does not validate historical mantissa sweeps.

Authority: resonance-only audit. Source FST and canonical RGphi remain untouched.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import gcd, lcm
from itertools import combinations


def order_mod(a: int, m: int) -> int:
    """Small finite independent order check, avoids imported symbol libraries."""
    assert gcd(a, m) == 1
    v = a % m
    k = 1
    while v != 1:
        v = (v * a) % m
        k += 1
    return k


def carry_cells(ms: tuple[int, ...], digits: int):
    """Exactly enumerate phase-prefix cells in k and shared carry interval u."""
    modulus = 10**digits
    cuts = sorted({Fraction(i, m) for m in ms for i in range(m + 1)})
    labels = {}
    ambiguous = 0
    for k in range(modulus):
        for left, right in zip(cuts, cuts[1:]):
            u = (left + right) / 2
            b = tuple((m * k + (m*u).__floor__()) % modulus for m in ms)
            if b in labels and labels[b] != k:
                ambiguous += 1
            else:
                labels[b] = k
    return len(cuts)-1, len(labels), ambiguous


def main():
    assert 18**2 + 18 + 1 == 343 == 7**3
    assert 17+19 == 36 and 343 == 9*36+19 == 10*36-17
    assert pow(343, 2, 36) == 1
    assert all((343 * x) % 36 == x for x in range(0,36,2))
    assert all((343*x) % 36 == (x+18)%36 for x in range(1,36,2))

    with localcontext() as ctx:
        ctx.prec = 72
        Q = Decimal(343)
        H = sum((Q-1)**2 * Decimal(f) *
                (Decimal(f).ln()/Decimal(2).ln()) / Q**(f+1)
                for f in range(2,25))
        target = Decimal('0.005837332402614633262170598195')
        assert abs(H-target) < Decimal('1e-30'), (H, target)
        # Huffman conditional average under uniform posteriors.
        def LH(f):
            k = f.bit_length()-1
            return Decimal(k+2) - (Decimal(2)**(k+1)/Decimal(f))
        L = sum(Decimal(f)*(Q-1)**2/Q**(f+1)*LH(f)
                for f in range(1,25))
        assert abs(L-Decimal('0.005839403722087393457897486756')) < Decimal('1e-30')
        print('T013_entropy_exact_digits='+str(H)[:37])
        print('T013_huffman_exact_digits='+str(L)[:37])

    assert carry_cells((5,12),1)[2] > 0
    assert carry_cells((5,12),2) == (16, 1600, 0)
    assert carry_cells((5,12),3) == (16, 16000, 0)
    assert carry_cells((15,12,5),1) == (24, 240, 0)
    assert gcd(15,12,5) == 1
    assert gcd(15,12) != 1 and gcd(15,5) != 1

    expected = {1:1,2:10,3:20,4:40,5:80,6:80,7:80}
    for d, index in expected.items():
        modulus=10**d
        phi=4*10**(d-1)
        actual=phi//order_mod(343,modulus)
        assert actual==index, (d,actual,index)
    # LTE: v_5(343^4-1)=2, v_2(343^2-1)=4 imply index 80 d>=5.
    assert (343**4-1)%(5**2)==0 and (343**4-1)%(5**3)!=0
    assert (343**2-1)%(2**4)==0 and (343**2-1)%(2**5)!=0
    print('PASS_T013_CONNECTED_FST_NOTA02_FINITE_EXACT')
    print('FST_v05_two_family_prefix_d2_d3=UNIQUE')
    print('FST_v05_three_family_prefix_d1=UNIQUE')
    print('order343_unit_subgroup_index_d_ge_5=80_BY_LTE')
    print('historical_168_mantissa_negative=NOT_REEXECUTED')
    print('FST_v05_reported_40_tests=NOT_REEXECUTED_SOURCE_ABSENT')

if __name__=='__main__':
    main()
