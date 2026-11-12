# RGΦ-I RC3.1 — reviewer correction archive (2026-11-12)

This is an **embargo-safe historical reviewer archive** under Paper III's review provenance. It does not replace the Paper III master theorem stack, definitions, canonical claim ledger, or Gate 023; no OPEN or OPEN_PARTIAL claim is promoted.

Upstream release: `RGPHI_RC3_1_COMPLETE.zip`, SHA-256 `008132947a6710c755aa3f5bfcec2326564a0613bc5d62740d846669a6660fd2`. No article/supplement manuscript PDF or LaTeX is stored here.

## What changed from RC3

- The `cleveref` theorem/lemma reference typing was corrected in the manuscript's upstream source.
- The 59-base census accounting now distinguishes **19 symbolic exclusions + 40 remaining bases** from **47 exact enumerations + 12 budget-only bases**. Seven exact enumerations redundantly checked symbolic exclusions (`5,7,11,13,17,19,25`).
- This archive records the source changelog, exact census rows, corrected summary, expanded consistency checker and the upstream verification log.

## Reproduction and scope

Run `python3 certificates/check_census_B2_60.py` from this directory. It checks the archived 59-row CSV, count partitions, redundant enumerations, 2,210,941 candidate-state total, 14 closed SCCs and zero nonpermutation SCCs for `n<=5`.

The checker validates a **finite archived output and its internal consistency**. It does not recompute all 47 divisor universes independently, certify every proof or establish external peer review. In the locally available upstream release, the nonsquare, counterfamily Python/C++, projective-content, census and bilingual-manuscript consistency checkers returned PASS on 2026-11-12. The retained `VERIFY_OUTPUT.txt` is an upstream log, not evidence of a clean-room proof certification.

The earlier RC3 original checker archive in `../rc3/` is preserved byte-for-byte; its provenance and acknowledged limitations still apply. No separate research branches or Stage-A/B2 files are modified.
