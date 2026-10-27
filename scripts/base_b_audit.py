#!/usr/bin/env python3
"""Exact audit for the base-B RGΦ generalization.

Checks:
  * seed-family conjugacy S_B(N/(N+r)) = N/(N + (Br mod N));
  * branch-matrix determinants are B;
  * exact Farey-defect transport Delta' = B Delta/(g k);
  * prime-budget valuation law for every prime p|B.

All arithmetic is integer/rational exact.
"""
from __future__ import annotations
from fractions import Fraction
from math import gcd
from random import Random
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "rgphi_base_b_audit_result.json"


def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def canonical_neighbor(a: int, b: int):
    g, x, _ = egcd(a, b)
    assert g == 1
    inv = x % b
    q = (-inv) % b
    p = (a * q + 1) // b
    assert a * q - b * p == -1
    return p, q


def matrix_T(B: int, d: int):
    return ((B, -d), (0, 1))


def matrix_S(B: int, d: int):
    return ((1, 0), (-(B - 1 + d), B))


def det(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def mv(M, v):
    return (
        M[0][0] * v[0] + M[0][1] * v[1],
        M[1][0] * v[0] + M[1][1] * v[1],
    )


def primitive(v):
    a, b = v
    g = gcd(abs(a), abs(b))
    assert g > 0
    a //= g
    b //= g
    return (a, b), g


def branch(B: int, state: tuple[int, int], action: str):
    a, b = state
    if action == "T":
        d = (B * a) // b
        M = matrix_T(B, d)
    else:
        if a == 0 or 2 * a < b:
            return None
        d = (B * (b - a)) // a
        M = matrix_S(B, d)
    raw = mv(M, state)
    nxt, g = primitive(raw)
    return M, d, nxt, g


def vp(n: int, p: int):
    n = abs(n)
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def prime_factors(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def T_B(B: int, x: Fraction):
    y = B * x
    return y - (y.numerator // y.denominator)


def H(x: Fraction):
    return Fraction(1, 1) / (1 + x)


def C(x: Fraction):
    return Fraction(1, 1) / x - 1


def S_B(B: int, x: Fraction):
    return H(T_B(B, C(x)))


def main():
    rng = Random(20261027)
    seed_checks = 0
    matrix_checks = 0
    defect_checks = 0
    valuation_checks = 0

    # Seed family and branch determinant, exhaustive modest grid.
    for B in range(2, 41):
        for N in range(2, 101):
            for r in range(1, N):
                x = Fraction(N, N + r)
                s = (B * r) % N
                expected = Fraction(N, N + s)
                assert S_B(B, x) == expected
                seed_checks += 1
        for d in range(B):
            assert det(matrix_T(B, d)) == B
            assert det(matrix_S(B, d)) == B
            matrix_checks += 2

    # Random exact Farey-shadow transport tests across bases and defects.
    for _ in range(250_000):
        B = rng.randint(2, 60)
        b = rng.randint(2, 2_000)
        a = rng.randint(1, b - 1)
        if gcd(a, b) != 1:
            continue
        action = "T" if rng.getrandbits(1) == 0 else "S"
        br = branch(B, (a, b), action)
        if br is None:
            continue
        M, _, nxt, g = br
        p0, q0 = canonical_neighbor(a, b)
        # B-smooth h, plus t primitive relative to h.
        h = 1
        for p in prime_factors(B):
            h *= p ** rng.randint(0, 4)
        t = rng.randint(0, 10_000)
        if gcd(t, h) != 1:
            continue
        shadow = (h * p0 + t * a, h * q0 + t * b)
        assert a * shadow[1] - b * shadow[0] == -h
        raw_shadow = mv(M, shadow)
        shadow_nxt, k = primitive(raw_shadow)
        delta_nxt = nxt[0] * shadow_nxt[1] - nxt[1] * shadow_nxt[0]
        assert delta_nxt * g * k == -B * h
        defect_checks += 1
        for p in prime_factors(B):
            lhs = vp(abs(delta_nxt), p)
            rhs = vp(h, p) + vp(B, p) - vp(g, p) - vp(k, p)
            assert lhs == rhs
            valuation_checks += 1

    result = {
        "status": "PASS",
        "date": "2026-10-27",
        "bases_tested_exhaustively": [2, 40],
        "seed_family_checks": seed_checks,
        "branch_matrix_determinant_checks": matrix_checks,
        "random_exact_defect_transport_checks": defect_checks,
        "prime_budget_valuation_checks": valuation_checks,
        "theorems_audited": [
            "S_B(N/(N+r)) = N/(N + (B r mod N))",
            "det M_T = det M_S = B",
            "Delta' = B Delta/(g k)",
            "v_p(h') = v_p(h)+v_p(B)-v_p(g)-v_p(k) for p|B",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
