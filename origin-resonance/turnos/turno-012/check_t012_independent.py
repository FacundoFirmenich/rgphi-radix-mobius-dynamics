#!/usr/bin/env python3
"""Independent finite/analytic sanity checks for Origin-Resonance Turno 012.

Proof boundary: enumerates exact decimal words through length 6, checks exact
integer counting through L=1000, and checks an analytically declared limiting
entropy formula at high precision. Not a proof of the non-CFL/natural-boundary
assertions nor of the asymptotic fibre law from first principles.
"""

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations
from math import ceil, lcm

Q = 343


def primitive7(n: int) -> int:
    assert n != 0
    while n % 7 == 0:
        n //= 7
    return n


def fibre_histogram(ell: int) -> Counter:
    n = 10 ** ell
    counts = Counter()
    for word_value in range(n):
        k = 8 * n - 9 * word_value
        counts[primitive7(k)] += 1
    return Counter(counts.values())


def max_fibre(ell: int) -> int:
    # Exact integer inequality 343**j <= 10**ell; no floating-point floors.
    n = 10 ** ell
    powers = 0
    qpow = 1
    while qpow <= n:
        powers += 1
        qpow *= Q
    return powers


def nonnegative_integer_word(k: int) -> str:
    """Canonical minimal decimal word for positive K == 8 (mod 9)."""
    ell = 0
    while k > 8 * 10**ell:
        ell += 1
    v, rem = divmod(8 * 10**ell - k, 9)
    assert rem == 0 and 0 <= v < 10**ell
    return str(v).zfill(ell) if ell else ""


def valuation_free(n: int, primes: tuple[int, ...]) -> int:
    out = n
    for p in primes:
        while out % p == 0:
            out //= p
    return out


def main() -> None:
    a1000 = max_fibre(1000)
    s1000 = sum(max_fibre(ell) for ell in range(1001))
    assert a1000 == 395, a1000
    assert s1000 == 197913, s1000
    assert (a1000 - 1).bit_length() == 9
    assert (s1000 - 1).bit_length() == 18

    for ell in range(7):
        # Realize the extremal fibre H=8 via the asserted N0^2 construction.
        words = set()
        j, power = 0, 1
        while power <= 10**ell:
            root = nonnegative_integer_word(8 * power)
            word = "8" * (ell - len(root)) + root
            assert len(word) == ell
            v = int(word) if word else 0
            assert primitive7(8 * 10**ell - 9 * v) == 8
            assert word not in words
            words.add(word)
            j += 1
            power *= Q
        assert len(words) == max_fibre(ell)

    histogram = fibre_histogram(6)
    assert histogram == Counter({1: 994178, 2: 2899, 3: 8}), histogram
    assert sum(size * number for size, number in histogram.items()) == 1_000_000

    # Check finite signed K = 8 (mod 9) examples with overlapping erased-prime sets.
    prime_sets = [(2, 3, 5), (3, 7), (3, 11)]
    for z in range(-250, 251):
        k = 8 + 9*z
        stripped = [valuation_free(k, s) for s in prime_sets]
        recovered = (1 if k > 0 else -1) * lcm(*(abs(x) for x in stripped))
        assert recovered == k

    p_ambig = Fraction(685, 117649)
    assert p_ambig == 1 - Fraction(342 * 342, 343 * 343)
    with localcontext() as ctx:
        ctx.prec = 85
        ln2 = Decimal(2).ln()
        entropy = sum(
            (Decimal(f) * Decimal(342)**2 / Decimal(Q)**(f+1))
            * (Decimal(f).ln()/ln2)
            for f in range(2, 40)
        )
        fixed = sum(
            Decimal(f) * Decimal(342)**2 / Decimal(Q)**(f+1)
            * Decimal((f - 1).bit_length())
            for f in range(2, 40)
        )
        assert abs(entropy - Decimal('0.005837332402614633262')) < Decimal('1e-21')
        assert abs(fixed - Decimal('0.005847854308123188049')) < Decimal('1e-21')
        print('PASS_T012_INDEPENDENT_FINITE_AUDIT')
        print(f'extremal_label=8 Amax(1000)={a1000} bits=9 Smax(1000)={s1000} bits=18')
        print(f'ell=6 fibre_histogram={dict(sorted(histogram.items()))}')
        print(f'limiting_ambiguity_probability={p_ambig}')
        print(f'limiting_conditional_entropy_formula={entropy:.24f} bits')
        print(f'limiting_fixed_key_cost_formula={fixed:.24f} bits')
        print('scope=finite_exact_enumeration_and_high_precision_series_only')
        print('open=non_CFL,natural_boundary,nonuniform_sources,T013_complexity')


if __name__ == '__main__':
    main()
