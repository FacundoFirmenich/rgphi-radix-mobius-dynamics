# RGΦ Origin–Resonance | RC3 archived checker replay | 2026-11-12

Authority: `BRANCH_ONLY_NO_CANONICAL_PROMOTION`. Canonical Paper III `main` is read-only to this watch. Negative findings and post-hoc boundaries remain in force.

## New canonical input (provenance, not a new mathematical class)

- Previous inspected canonical head: `cfe70e9563e5179da06068bdc79760ca50f5b1fc`.
- New inspected canonical head: `14af5ab9d590902f3fd4656a66eef32d8ae663d8` (one commit, four added files).
- New provenance: `paper-iii/reviewer/rgphi-i-2026-11-11/rc3/CHECKER_ARCHIVE_PROVENANCE.md`, Git blob `7c5169fe4fd15decc193513bca7a839958db30d2`.
- Archived source checkers: `code/check_counterfamily.py` blob `04d97c3cc7aa5c451e5603fde30521f64748e5f2`; `code/check_projective_content.py` blob `a2ba560ef5ee02b8e7cdd6e1247195a73adaf400`; `code/trusted_checker.cpp` blob `a2e4a5f3aed0528cb44e41a7ec021239a39d5f5e`.
- The canonical provenance document identifies source ZIP `RGPHI_RC3_COMPLETE.zip` and SHA-256 `3069f8696b8f814c01c2dd51bdc7a55bfc342496d612855088de321890b47456`. That ZIP hash is **source-declared, not independently checked against the ZIP during this watch**.
- All three Git blob SHA-1 values were independently recomputed from the fetched exact source bytes, using the Git `blob <size>\0<bytes>` object-hash convention: all three matched.

## Direct execution checks in this watch

- Python `check_counterfamily.py`: **PASS**, 1,001 bases `B_k = 88011536665779 + 223336848698040 k`, `0 <= k <= 1000`, exact five-state `T,S` image maps, gcd content, strong connectivity, and CRT/fibre predicates.
- Python `check_projective_content.py`: **PASS**, exact projective four-edge cycle matrices, eigenvector content factor `Delta=3`, determinant `B_0^4`, trace `3+B_0^4/3`, and discriminant square.
- C++17 `trusted_checker.cpp`: compiled with `g++ -std=c++17 -O2` and **PASS** across 1,001 family members. This is a replay of archived code, not a clean-room proof.
- Separate branch-only implementation: `origin-resonance/checkers/check_rc3_archive_replay_resonance.py`. Its standalone local run **PASS** with exact rational arithmetic for all 1,001 family members, independently enumerated six labelled simple cycles, content receipts, and projective cycle spectral checks.

The canonical provenance also reports the original manuscript-consistency runner fails because four expected TeX paths are not included in the RC3 release. **FAIL/NOT_RUN** for that packaging-dependent check remains explicitly retained. The B=2..60 CSV audit is an internal consistency test, not an independent full-range re-enumeration.

## Unchanged prospectively frozen endpoints

- New exact six-state classes/catalogue: **none supplied**. OR-4 `DUAL_TRIAD` and `ALTERNATING_HEXAGON`: `NOT_TRIGGERED`.
- New minimal nonpermutation classes with `n >= 6`: **none supplied**. OR-5 `SHORT_DEFECT_CYCLE` and certified `FIVE_STATE_DEFECT_QUOTIENT`: `NOT_TRIGGERED`.
- OR-19 six-state strict-defect preregistration `{2,3,4,5,6,7}`: realized spectrum **NOT_ENUMERATED**; no imputed hit or absence.
- No newly discovered canonical cycles. The six previously recorded simple cycles of the exact five-state counterfamily remain five `Delta=1` cycles (log pitch `0`, alpha `0`) plus one length-four `TSTS` cycle (`Delta=3`, log pitch `log(3)`, alpha `log(3)/(4 log B_k)`). Source-checker replay strengthens **reproducibility of the existing receipt**, not the count of independent objects.
- The projective helical lift, golden conjugacy boundary, projective centrum involution, and dual one-ninth endpoint receive **no new object-level adjudication**. No identification with the wider hyperaccess concept is asserted.
- All nineteen elliptic curves remain covered by the existing uniform ledger without new rank/torsion or chamber-point evidence. F17 retains rank at least one, trivial torsion, chamber witness `[64233:11741:1138]` and obstruction `d=gcd(C,D)=23`; its coprime-integral multiples remain `OPEN`. F19 arithmetic admissibility remains `OPEN`. No post-hoc prime selection.
- RC3 bounded B=2..60 scope correction stands: 14 closed SCCs in 47 enumerated bases, plus six historical permutation SCCs in three of twelve shortcut bases, hence **at least 20** over the combined evidence, not an exhaustive 59-base SCC total. No new n=6 results.

**Boundary:** New durable evidence is a reproducible **checker archive** and a standalone branch-local replay, not a new preregistered endpoint result, peer review, or independent full-range census. The canonical theorem stack, Gate 023, and claim ledger are unchanged.

Sources:
- https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics/commit/14af5ab9d590902f3fd4656a66eef32d8ae663d8
- https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics/blob/main/paper-iii/reviewer/rgphi-i-2026-11-11/rc3/CHECKER_ARCHIVE_PROVENANCE.md
- `origin-resonance/ledgers/SURVEILLANCE_ENDPOINT_STATUS.json` and `ELLIPTIC_ALL_19_STATUS.csv` (unchanged).
