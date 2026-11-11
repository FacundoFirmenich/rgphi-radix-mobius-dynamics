# Exact source audit backfill — Rounds 019/020

Archival-only synchronization of original code and exact audit CSVs from the Round 019 and Round 020 bundles. Historical bytes are preserved under the separate `source-archive/` directories without changing the current scientific canon.

Original ZIP SHA-256 (verified by recomputation):

- Round 019: `24c037c0bf1278496c6486d1bcb2e2fba36757af2dbafb8d564552da3623abb9`.
- Round 020: `b187a3079384a449215117f76185a6044cf34c68099c2e8a1454eb7d688dec52`.

The original internal checksum manifests passed 50/50 for Round 019 and 42/42 for Round 020. The Round 020 symbolic coprimality checker and exact n=17 point/finite-field checker were re-executed and both returned `PASS`. The larger source enumerations were not re-executed in this archival synchronization; their results retain historical source-only authority.

Round 021 theorem stack v1.12 and all `OPEN`/`OPEN_PARTIAL` boundaries remain unchanged.
