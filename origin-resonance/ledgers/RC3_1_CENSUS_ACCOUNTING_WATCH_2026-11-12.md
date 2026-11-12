# RGΦ Origin–Resonance — RC3.1 census-accounting watch (2026-11-12)

**Authority:** `BRANCH_ONLY_NO_CANONICAL_PROMOTION`. This is a dated resonance-only provenance and accounting receipt, **not** an amendment to any Paper III theorem, Gate 023, or canonical claims. Prior negative findings and post-hoc labels are retained. The earlier `SURVEILLANCE_ENDPOINT_STATUS.json` remains the historical RC3 snapshot; this receipt tracks the subsequent RC3.1 source revision without retroactively rewriting it.

## Canonical delta examined

- Previous inspected canonical head: `14af5ab9d590902f3fd4656a66eef32d8ae663d8`.
- New canonical head: `30c5a5242c8fdc1eab4e37ee807b7837780b2985` (exactly **one** forward commit; seven **added** files, no modified/deleted files).
- New source prefix: `paper-iii/reviewer/rgphi-i-2026-11-11/rc3_1/`.
- Source Git blob receipts: `certificates/exact_census_B2_60.csv` = `286f540cccf21bcda008454ebb69712da591aae4`; `certificates/EXACT_CENSUS_B2_60_SUMMARY.json` = `a36016d55f48952573fa5a69c606539a6d089df8`; `certificates/check_census_B2_60.py` = `9ba2ccc42a6255904afe3d4284ba1053da1dee23`.
- Other added records: `CENSUS_ACCOUNTING_RC3_1.md`, `RC3_1_CHANGELOG.md`, `README.md` and `VERIFY_OUTPUT.txt`. The Git archive omits the article/supplement PDF and LaTeX, so its stated upstream typesetting repairs are historical-source claims rather than independently replayed manuscript builds here.
- Source declares upstream ZIP `RGPHI_RC3_1_COMPLETE.zip`, SHA-256 `008132947a6710c755aa3f5bfcec2326564a0613bc5d62740d846669a6660fd2`; ZIP bytes were **not** obtained for an independent hash check.

## RC3.1 disambiguation — both counts are simultaneously valid

| Different denominators | Exact result | Authority |
|---|---|---|
| Mathematical partition of `B=2..60` | **19** coprime to 6 (symbolic nonpermutation obstruction) + **40** remaining = **59** | Disjoint classification |
| Actual methods used in archived computation | **47** exact divisor-universe runs + **12** cycle-budget-only cases = **59** | Disjoint method attribution |
| Intentional methodological overlap | **7** coprime bases additionally enumerated: `5,7,11,13,17,19,25` | Subset of 19; not a third category |
| Candidate states in 47 runs | **2,210,941** | Archived finite computation |
| Closed SCCs in 47 runs | **14**, all permutation | **Not** all 59 bases |
| Nonpermutation closed SCCs with `n<=5` | **0** across the source's bounded classification | Bounded negative, no `n>=6` inference |

The 12 budget-only bases are `23,29,31,35,37,41,43,47,49,53,55,59`. **Do not** call these 12 bases primes; they include composite 49 and 55. The 19 mathematically excluded bases are excluded from the **nonpermutation high-SCC target**, **not** from the existence of permutation closed SCCs.

### Historical cross-check retained as an explicit caveat

The pre-existing OR20 exact ledger documents **six** permutation closed SCCs omitted from the 47-run accounting: `B=29:1`, `B=31:3`, `B=37:2`. Together, the 14 RC3.1 counted SCCs and six separately witnessed SCCs imply **at least 20** in the combined records across `B=2..60`. It is **not** an exhaustive total for 59 bases; the other budget-only cases have not been enumerated for all permutation SCCs. The source's zero **nonpermutation** claim remains a distinct bounded statement. Earlier ledger `RC3_B2_60_BOUNDED_WATCH.csv` is retained unmodified, including blank rather than imputed-zero SCC counts on shortcuts.

## Verification and limitation

- This run retrieved all seven newly added canonical files and checked the full 59-row CSV against its JSON summary and the existing 59-row branch watch with an independent in-session program: **PASS** (19/40 mathematical split, 47/12 method split, seven overlaps, the state and SCC totals, all rows, and the historical skipped SCCs).
- Also checked the pre-existing **19** contiguous elliptic curve status rows and **six** exact five-state cycle receipts for structural continuity.
- An additional read-only Python cross-ledger checker was placed in `origin-resonance/checkers/check_rc3_1_accounting_resonance.py`. It pins the upstream canonical commit and blob SHA values, reads both branches with `git show`, and checks the archived accounting and frozen endpoints. **Its own Git-clone Python execution was not performed in this run**; no PASS claim is made for that executable.
- `VERIFY_OUTPUT.txt` reports upstream PASS for nonsquare, counterfamily Python/C++, projective content, RC3.1 census, and manuscript consistency. Those are **upstream logged** results, not independent certification by this watch; no full 47-universe clean-room re-enumeration was performed.

## Prospective endpoint registry (unchanged)

- **OR-4:** `DUAL_TRIAD` and `ALTERNATING_HEXAGON` = `NOT_TRIGGERED`; no new exact six-state class or complete six-state catalogue.
- **OR-5:** `SHORT_DEFECT_CYCLE` and certified five-state defect quotient = `NOT_TRIGGERED_FOR_N_GE_6`; no new minimal nonpermutation class with `n>=6`.
- **OR-19:** preregistered strict-defect spectrum `{2,3,4,5,6,7}`; realized spectrum = `NOT_ENUMERATED` (neither a hit nor falsation).
- **Cycle receipts:** no new canonical cycles. The existing six exact simple cycles comprise five `Delta=1` (pitch `0`, `alpha=0`) and the four-edge `TSTS` with `Delta=3`, pitch `log 3` and `alpha=log(3)/(4 log B_k)`. This is an object-level projective content receipt, **not** a theorem identifying general hyperaccess.
- **Structural endpoints:** projective helical lift, golden conjugacy boundary, projective centrum involution, and dual one-ninth endpoint: **no new independent object-level corroboration or falsation**.
- **Elliptic frontier:** all F1–F19 retain their previous rank/torsion and rational-chamber statuses. F17 keeps rank `>=1`, trivial torsion, witness `[64233:11741:1138]`, obstruction `d=gcd(C,D)=23`; no certified coprime-integral multiples. F19 arithmetic remains `OPEN`. No post-hoc prime selection.
- **Preserved boundaries:** negative and bounded results, `OPEN` statuses, preregistration, post-hoc labels, and read-only authority of `main` continue unchanged.

**Disposition:** material **resonance provenance/accounting update only**. New exact mathematical class: **none**. New preregistered endpoint evidence or falsation: **none**.

Sources: [canonical RC3.1 commit](https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics/commit/30c5a5242c8fdc1eab4e37ee807b7837780b2985), [RC3.1 source archive](https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics/tree/30c5a5242c8fdc1eab4e37ee807b7837780b2985/paper-iii/reviewer/rgphi-i-2026-11-11/rc3_1), pre-existing `OR20_FIXED_BASE_2_40_MONODROMY.csv`, `ELLIPTIC_ALL_19_STATUS.csv`, `CYCLE_CONTENT_RECEIPTS_5STATE.csv`.
