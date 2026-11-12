# RGΦ-I RC3 — original checker archive and reproduction boundary

Source: `RGPHI_RC3_COMPLETE.zip` (Library, 2026-11-11), SHA-256 `3069f8696b8f814c01c2dd51bdc7a55bfc342496d612855088de321890b47456`. The three checker files in `code/` are unmodified originals from that ZIP.

| Archived checker | Git blob SHA-1 | Local independent invocation (2026-11-12) |
|---|---|---|
| `code/check_counterfamily.py` | `04d97c3cc7aa5c451e5603fde30521f64748e5f2` | PASS, 1,001 family members and CRT/fibre predicates |
| `code/check_projective_content.py` | `a2ba560ef5ee02b8e7cdd6e1247195a73adaf400` | PASS, exact projective-content/spectral-cycle identities |
| `code/trusted_checker.cpp` | `a2e4a5f3aed0528cb44e41a7ec021239a39d5f5e` | PASS after C++17 compilation, 1,001 family members |

The release's independent `audit/check_census_B2_60.py` also passes on the supplied CSV, but this is a consistency check of the source output, **not** a new clean-room recomputation for all bases. The original reference JSONL for B=2..17 has the same blob as `../rc2/source-archive/exact_census_B2_17.jsonl` and is not duplicated here.

Known upstream packaging limitation: the original manuscript consistency script references `en/main.tex`, `es/main.tex`, `supp_en/supplement.tex`, and `supp_es/supplement.tex`; those paths are absent from the unmodified RC3 release. Its direct run fails and is not counted as PASS in this archive.

Authority: this archival update does **not** modify the master Paper III theorem stack, current state, gates or canonical claim ledger. Canonical `v1.13` and Gate 023 remain unchanged; all `OPEN` and `OPEN_PARTIAL` claims retain their status. External peer review and independent full-range replay remain pending.
