# RGΦ-I / Paper III — RC2 provenance and reproducibility (2026-11-11)

This directory archives **reviewer and exact-audit evidence only** from the November 11 RC2 bilingual editorial integration. The article, supplement, bibliography, PDFs and graphical abstract remain outside this repository, in accordance with the RC2 source boundary.

## Verified source
- Library ZIP: `RGPHI_I_RC2_REVIEW_INTEGRATION_BILINGUAL_2026-11-11.zip`.
- ZIP SHA-256: `d3e4acee5ad65fbe52f5d16169194100f1ccc2ae25143d27f49cd262dada94b2`.
- ZIP integrity: 21/21 members readable; CRC test PASS.
- Original audit paths: `audit/RESPUESTA_INTEGRADA_A_REVISORES_RC2.md`, `audit/exact_fixed_base.py`, `audit/exact_census_B2_17.csv`, `audit/exact_census_B2_17.jsonl`, `audit/requirements_analysis.txt`.
- The five archived source files are byte-exact Git blobs from those source members, checked against independent local git-blob SHA-1 calculations.

## Replay and boundary
- Exact execution: `python audit/exact_fixed_base.py --n 5 --bases 2 3 ... 17`; 16/16 JSONL records, and 16/16 CSV records, matched the archived data.
- 82,387 candidate high states; four closed SCCs; zero nonpermutation closed SCCs with size at most five in the **finite checked window** of B=2..17.
- Independent overlap check with the existing B=2..40 audit: 16/16 base rows agree on candidate counts and closed-component counts. This is not a global theorem nor an independently certified proof of the divisor bound.
- The RC2 response retains unresolved audits of TTSS/TSTS combinatorial cases, external clean-room validation, five-state arithmetic classification and journal submission.
- `REPLAY_VERIFICATION.json` and `RC2_STATE.json` are new operational receipts, not original bundle members.

**No change** to `paper-iii/CURRENT_STATE.json`, the global claim ledger, theorem stack v1.13, or Gate 023. No `OPEN` / `OPEN_PARTIAL` promotions.
