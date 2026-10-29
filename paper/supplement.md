# Supplement to Paper I — Exact evidence and reproducibility

## S1. Scope

This supplement supports the manuscript **Nonnested extremal targets in a rational radix–Möbius semigroup**. It contains the exact layer-maxima ledger, exact continuation profiles, threshold atlas, terminal-set audit, and replay code used by the main theorems.

## S2. Exact terminal set

The terminal set has 23 states:

\[
\{0,1,1/2,1/3,2/3,3/4,4/5,5/6,7/8,7/9,7/10,
2/11,4/11,7/11,9/11,11/20,7/12,2/13,5/13,6/13,7/13,8/13,11/13\}.
\]

For each state, every admissible `T` or `S` child remains in the same set. This is checked exactly before the set is removed from the reachability graph.

## S3. Global first-hit ledger

`rgphi010_exact_bfs_0_162.csv` records, for every depth from 0 to 162:

- exact frontier cardinality;
- maximum denominator;
- exact maximum height as a reduced fraction;
- target-hit count;
- raw-child count where available.

At depth 162 the exact frontier has 329,106,757 states. The record-height ladder determines the complete finite-horizon piecewise-constant function `tau_m(kappa)` for `m=1,...,4`.

## S4. Threshold theorem

For a record layer `d`, let

\[
M_{<d}=\max_{j<d}M_j,
\qquad
M_d=\max_{x\in L_d}q(x).
\]

Because the target inequality is strict,

\[
\tau_m(\kappa)=d
\quad\Longleftrightarrow\quad
\kappa\in[M_{<d}/10^m,M_d/10^m).
\]

The exact benchmark intervals are:

| m | tau | lower inclusive | upper exclusive |
|---:|---:|---:|---:|
| 1 | 45 | 9.3 | 12.9 |
| 2 | 85 | 9.03 | 12.03 |
| 3 | 120 | 10.019 | 11.643 |
| 4 | 162 | 10.6197 | 12.4853 |

Their simultaneous intersection is

\[
[10.6197,11.643).
\]

## S5. Continuation searches

The exact first continuation hits are:

| source | source time | target | first arrival | endpoint | distinct states |
|---|---:|---:|---:|---|---:|
| 128/129 | 45 | m2 | 87 | 1100/1101 | 55,144 |
| 1202/1203 | 85 | m3 | 139 | 13542/13543 | 3,955,616 |
| 11156/11157 | 120 | m4 | 168 | 122088/122089 | 30,380,076 |

The continuation-stability intervals are:

\[
[10.33,11.01),
\quad
[8.827,13.543),
\quad
[4.4853,12.2089).
\]

Intersecting these with the corresponding global first-hit intervals gives the common nonnesting interval

\[
[10.6197,11.01).
\]

The other two depth-three first-hit states satisfy:

- `11532/11533`: maximum height through time 162 is 44,400;
- `11642/11643`: maximum height through time 162 is 28,408.

They therefore cannot reach the depth-four target anywhere in the common interval.

## S6. Exact arithmetic

States are stored as primitive integer pairs. Target comparison uses integer cross-products. No floating-point number decides reachability or target membership. Decimal values in reports are display-only renderings of exact rational endpoints.

## S7. Evidence files

- `RGPHI_THRESHOLD_ATLAS_PIECEWISE_m1_m4.csv`
- `RGPHI_THRESHOLD_BENCHMARK_ROBUSTNESS.csv`
- `RGPHI_NONNESTING_ROBUSTNESS.csv`
- `RGPHI_OTHER_M3_OPTIMA_NOHIT_ROBUSTNESS.csv`
- `RGPHI_THRESHOLD_ROBUSTNESS_RESULT.json`
- `rgphi_threshold_robustness.py`
- `rgphi_threshold_profile_bfs.cpp`
- five exact continuation-profile CSVs
- global exact profile `rgphi010_exact_bfs_0_162.csv`

## S8. Evidence boundary

The finite-horizon threshold atlas is exact through depth 162. It does not claim a global formula for all `kappa`, all bases, or all seeds. The main nonnesting theorem is exact on its stated interval and uses only the benchmark system.

## S9. Current depth-five status — non-dependent update

As of 28 October 2026, the rigorous depth-five interval is

\[
186 \le \tau_5 \le 212.
\]

This update does not change any theorem in Paper I: the manuscript depends only on the exact depth-one through depth-four chronology and its continuation searches. The active Stage B2 computation requires the verified 19.7 GB checkpoint at global time 185; the payload is not part of the lightweight submission package.

## S10. Formal layer recursion and reviewer replay

Let `L_0={x_0}\E` and recursively form `L_{n+1}` from every admissible exact
`T/S` child of `L_n`, remove the certified forward-invariant terminal set, reduce
every fraction primitively, and deduplicate exact rational pairs. Proposition
8.1 of the manuscript proves by induction that `L_n` is precisely the
nonterminal reachable set at time `n`. Thus first-hit absence and presence are
finite reachability statements, not heuristic properties of sampled paths.

Minimal compact verification:

```bash
python -m pip install -e '.[dev]'
rgphi verify
python scripts/paper_i/verify_receipt.py
```

Full exact replay of the five continuation searches:

```bash
scripts/paper_i/replay_exact.sh
```

The replay output must end in:

```text
PASS_PAPER_I_FULL_EXACT_REPLAY
```

## S11. Submission evidence boundary

The lightweight reviewer bundle contains the manuscript, supplement, claim
freeze, claim-evidence matrix, compact benchmark receipt, evidence boundary,
terminal-set audit, exact layer profile, robustness tables, continuation
profiles, replay scripts and independent checker. The complete depth-162 state
payload is intentionally not duplicated in ordinary Git. Before archival DOI
freeze it must either be deposited in an external research-data archive with a
cryptographic manifest or regenerated cleanly by an independent implementation.
This open archival item does not alter the exact finite theorems stated in the
manuscript, but it remains a submission-quality and long-term reproducibility
gate.

