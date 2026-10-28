# RGΦ repository freeze checklist — 28 October 2026

## Repository state

The canonical closure branch must contain both genealogies:

- the `main` canon and archived U5-HD-HM gates;
- the Stage-B2 exact-production work.

The merge must preserve `main` versions of `README.md` and `docs/SCIENTIFIC_STATUS.md`, use the Stage-B2 version of `docs/OPEN_PROBLEMS.md`, and add all Stage-B2 scripts/evidence.

## Required checks

- [ ] CI on Python 3.11 and 3.12.
- [ ] paper compilation.
- [ ] integrity ledger.
- [ ] research-object audit.
- [ ] Stage-B2 exact smoke comparison.
- [ ] all internal links.
- [ ] current interval is `186 <= tau_5 <= 212` everywhere.
- [ ] no claim of `tau_5=212`.
- [ ] raw 19.7 GB payload absence is explicit.
- [ ] U5-HD branches remain `EXPERIMENTAL_ISOLATED`.
- [ ] Paper I contains no Stage-B2-dependent headline claim.

## Archival actions still required

- deposit the exact checkpoint or a reproducible regeneration object;
- register Software Heritage snapshot;
- create Zenodo release only after metadata and assets agree;
- include artifact hashes and environment lock;
- obtain at least one clean-room reproduction before a strong computer-assisted publication claim.

## Fresh-session continuity

The session handoff and machine-readable state are canonical continuation artifacts. A new session should not infer state from conversation memory alone.
