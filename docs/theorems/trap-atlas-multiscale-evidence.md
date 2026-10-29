# Multiscale finite-trap atlas — exact evidence boundary

## Status

`COMPUTER_ASSISTED_LARGE / BOUNDED_EXHAUSTIVE`

This note extends the exact denominator-bound audit accompanying the modular
trap-classification theorem. It does not replace the theorem and does not claim
a global classification for unbounded denominators.

## Exact census

| D | states | edges | SCCs | closed modulo terminal | safe SCCs | safe states |
|---:|---:|---:|---:|---:|---:|---:|
| 500 | 76,094 | 109,254 | 23,176 | 153 | 1,502 | 1,624 |
| 2,500 | 1,899,856 | 2,735,455 | 565,564 | 248 | 5,483 | 5,933 |
| 5,000 | 7,600,436 | 10,944,352 | 2,255,011 | 314 | 9,672 | 10,418 |
| 10,000 | 30,397,464 | 43,771,910 | 9,009,037 | 467 | 17,094 | 18,472 |

At `D=10,000`, the 467 closed SCCs have maximum cardinality 12. The complete
size distribution and compact SCC listing are under `data/stage_a/`.

## Exact interpretation

For the fixed base-ten system and certified 23-state terminal set, every safe
state listed in the full Stage A release asset has all admissible children in
the safe set or terminal set. The compact repository checker validates counts,
SCC summaries, the first-divergence partition and the temporal envelope.

The audit proves that the 59 residual first-divergence sources are not captured
by any certified trap contained in the denominator-10,000 atlas. It does not
exclude:

- a finite trap containing a state of denominator above 10,000;
- an infinite nonescaping component;
- a later target hit after the current exact horizon.

## Reproducibility

- exact source: `scripts/stage_a/trap_atlas_exact.cpp`;
- compact checker: `scripts/stage_a/verify_stage_a_evidence.py`;
- full asset identity: `data/stage_a/ASSET_MANIFEST.md`;
- Stage A report: `docs/stage_a/RGPHI_GLOBAL_TRAP_CUT_088_STAGE_A_REPORT.md`.
