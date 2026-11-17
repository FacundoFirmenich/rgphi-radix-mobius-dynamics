#!/usr/bin/env python3
"""Independent exact CRT-obstruction replay for the three Turno-008 Q<=5000 survivors.

Scope: checks only the published finite-survivor CSV, not completeness
of the upstream Q<=5000 enumeration or global nonexistence.
No canonical files are read or modified.
"""
from __future__ import annotations

import csv
from math import gcd
from pathlib import Path

DATA = Path(__file__).with_name("N6_FULL_DIVISIBILITY_CANDIDATES_Q5000.csv")
T = (1, 1, 3, 2, 5, 4)
S = (5, 2, 1, 4, 3, 0)
EXPECTED_Q = (201, 2733, 4733)


def replay(row: dict[str, str]) -> str:
    Q, A, D, C, E, P, d, k = (
        int(row[name]) for name in ("Q", "A", "D", "C", "E", "P", "d", "k")
    )
    assert d in (4, 5, 6, 7) and 0 < 2 * abs(k) < d
    assert P == d * A + k * Q
    assert gcd(d, Q) == gcd(d, k) == 1

    states = ((P, d * Q), (A, Q), (A, D), (C, D), (C, E), (P, E))
    assert len(set(states)) == 6
    assert all(0 < 2 * p < 2 * q and gcd(p, q) == 1 for p, q in states)
    assert all(2 * p > q for p, q in states)

    # Necessity of the exact divisibilities in the declared lollipop form.
    assert (D * D - Q * Q) % A == 0
    assert (C * C - A * A) % D == 0
    assert (E * E - D * D) % C == 0
    assert (P * P - C * C) % E == 0
    assert (E * E - d * d * Q * Q) % P == 0

    congruences: list[tuple[str, int, int, int]] = []
    for i, (p, q) in enumerate(states):
        pt, qt = states[T[i]]
        ps, qs = states[S[i]]
        assert q % qt == 0 and p % ps == 0
        gi, hi = q // qt, p // ps
        assert gi == (d if i == 0 else 1) and hi == 1
        # Paper III's universal exact-realization CRT residues.
        rT = (gi * pt * pow(p, -1, q)) % q
        rS = (hi * (qs - ps) * pow(q - p, -1, p)) % p
        assert gcd(rT, q) == gi and gcd(rS, p) == hi
        congruences.extend((("T", i, rT, q), ("S", i, rS, p)))

    # Two congruences B=r mod m, B=s mod n are compatible
    # iff r == s modulo gcd(m,n). Any failed pair is a no-go certificate.
    contradictions = []
    for idx, (typ1, i1, r1, m1) in enumerate(congruences):
        for typ2, i2, r2, m2 in congruences[idx + 1:]:
            g = gcd(m1, m2)
            if (r1 - r2) % g:
                contradictions.append((typ1, i1, r1, m1, typ2, i2, r2, m2, g))
    assert contradictions, f"Q={Q} has no pairwise CRT obstruction"
    assert row["CRT_compatible"].strip().upper() == "FALSE"
    a, i, r, m, b, j, s, n, g = contradictions[0]
    return (f"Q={Q}: {a}{i} B={r} (mod {m}); "
            f"{b}{j} B={s} (mod {n}); gcd={g}; "
            f"residues_mod_g={r % g},{s % g}; CRT_FAIL")


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert tuple(int(row["Q"]) for row in rows) == EXPECTED_Q
    for row in rows:
        print(replay(row))
    print(f"PASS_T008_PAIRWISE_CRT finite_survivors={len(rows)} CRT_hits=0 "
          "global_exhaustiveness=NOT_TESTED")


if __name__ == "__main__":
    main()
