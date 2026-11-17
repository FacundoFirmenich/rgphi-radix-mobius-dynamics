# Turno 008 — independent pairwise generalized-CRT obstruction certificates

Authority: `ORIGIN_RESONANCE_ONLY`. No canonical Paper III claim is changed.

Source jurisdiction: the three tuples in `N6_FULL_DIVISIBILITY_CANDIDATES_Q5000.csv`, reported by the finite search `Q<=5000`. This independent replay **does not certify the exhaustiveness of that search** or global nonexistence.

Use the fixed six-state maps

- `T=(1,1,3,2,5,4)`
- `S=(5,2,1,4,3,0)`

and states `(P/(dQ), A/Q, A/D, C/D, C/E, P/E)`.
For each state `p_i/q_i`, derive the exact realization residues from canonical Theorem 019-B:

`B = g_i*p_{T(i)}*p_i^{-1} (mod q_i)`, with `g_i=q_i/q_{T(i)}`;

`B = h_i*(q_{S(i)}-p_{S(i)})*(q_i-p_i)^{-1} (mod p_i)`, with `h_i=p_i/p_{S(i)}`.

Here `g_0=d`, all other `g_i=1`, and all `h_i=1`. The replay checks primality-free integer coprimality, highness, all five necessary cycle divisibilities and the exact gcd of each residue with its modulus.

## Pairwise certificates

- `Q=201, d=5`: `T0: B=805 (mod 1005)`; `T2: B=53 (mod 351)`. The moduli have gcd `3`, but the residues reduce to `1` and `2`. **Incompatible**.
- `Q=2733, d=4`: `T0: B=8200 (mod 10932)`; `T2: B=3205 (mod 4122)`. The moduli have gcd `6`, but residues are `4` and `1`. **Incompatible**.
- `Q=4733, d=4`: `T0: B=14200 (mod 18932)`; `S1: B=2281 (mod 3912)`. The moduli have gcd `4`, but residues are `0` and `1`. **Incompatible**.

Each is independently sufficient to exclude its tuple as an exact integral-base realization; no prime selection or floating-point calculation is involved.

The executable `check_crt_pairwise_T008.py` was executed against the frozen candidate CSV with output:

```text
Q=201: T0 B=805 (mod 1005); T2 B=53 (mod 351); gcd=3; residues_mod_g=1,2; CRT_FAIL
Q=2733: T0 B=8200 (mod 10932); T2 B=3205 (mod 4122); gcd=6; residues_mod_g=4,1; CRT_FAIL
Q=4733: T0 B=14200 (mod 18932); S1 B=2281 (mod 3912); gcd=4; residues_mod_g=0,1; CRT_FAIL
PASS_T008_PAIRWISE_CRT finite_survivors=3 CRT_hits=0 global_exhaustiveness=NOT_TESTED
```

**Status**: `INDEPENDENT_CERTIFICATE_FOR_THREE_PUBLISHED_SURVIVORS`; `Q<=5000_SEARCH_COMPLETENESS=NOT_INDEPENDENTLY_AUDITED`; `GLOBAL_N6_REALIZATION=OPEN`.

The prospective Smith phase `d=4 -> Z/2Z` is a structural selection only. Both published `d=4` candidates fail generalized CRT; neither supplies an arithmetic realization.
