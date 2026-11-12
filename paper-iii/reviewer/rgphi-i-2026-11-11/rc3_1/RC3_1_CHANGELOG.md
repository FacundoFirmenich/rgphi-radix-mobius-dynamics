# RGΦ-I RC3.1 correction ledger

## Adjudication of the supplied 12-point replacement plan

| Item | Result |
|---|---|
| A.1 title/author | Already correct in LaTeX; reverified in PDF metadata and render |
| A.2 `TTSTS` -> `TSTS` | Already correct; checker now asserts the typo is absent |
| A.3 Theorem/Lemma reference | Source label was correct but `cleveref` loaded too early; package order and typed labels repaired globally |
| A.4 `x_1 fixed` | Already correct in source and render |
| A.5 representative table | Already present and correct in source and render |
| A.6 critical base `R` | Already correct; verified by Python/C++ replay and compiled render |
| A.7 Sienra spelling | Already correct in BibTeX; verified against arXiv:2504.01334 |
| A.8 Radix–Möbius consistency | Typeset form was correct; PDF metadata normalized to Unicode Möbius |
| B.1 author header | Source was correct; compiled running head verified |
| B.2 NONSQUARE heading | Source was correct; compiled heading verified |
| B.3 census 12/47 issue | Resolved by distinguishing mathematical exclusions from computational methods; 19 symbolic, 47 runs, 7 overlap, 12 budget-only |
| B.4 cross-consistency | Main, supplements, JSON summary and checker now agree |

## Census accounting

The suggested replacement `40 enumerations / 19 exclusions` would have contradicted the archived computation, because seven coprime-to-six bases were intentionally enumerated as regression checks. The corrected presentation keeps both true statements:

- disjoint mathematical partition: `19 symbolic + 40 remaining = 59`;
- actual computational methods: `47 exact runs + 12 budget-only = 59`;
- overlap: `7` exact runs lie inside the symbolic set.
