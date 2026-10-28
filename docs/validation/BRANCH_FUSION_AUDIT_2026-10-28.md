# RGΦ branch-fusion audit — 28 October 2026

## Decision

The public GitHub repository at commit `725c1ae4944a5ec913f0acb9c24a1e9f5a7b2223` remains the canonical principal line.

The Publication Deployment 001 line is retained as a secondary evidence-and-hardening branch. Its strongest nonredundant assets are integrated selectively; its duplicated archive structure and weaker packaging are not.

## Why the public repository is principal

The repository has the stronger research-object architecture:

- installable `rgphi` package and CLI;
- exact-arithmetic reference implementation;
- 13 theorem/repository tests under Python 3.11 and 3.12;
- lint, package build and canonical-evidence verification in CI;
- Paper I, supplement, references and claim–evidence matrix;
- trap atlas and threshold data;
- Stage B2 production tooling and 128 checkpoint hashes;
- explicit branch authority and experimental isolation;
- FAIR, RO-Crate, Zenodo, CodeMeta, SBOM and external-review infrastructure.

Its canonical scientific state is also correct: `tau_1..tau_4=45,85,120,162`, `186 <= tau_5 <= 212`, witness 212, Bellman ladder `89..212`, and exact search through time 185.

## Why Deployment 001 is secondary rather than discarded

Deployment 001 has four locally superior components:

1. **Paper I consistency.** Its manuscript and claim matrix use the current interval `[186,212]`; the public repository manuscript still contained the superseded `[179,212]` sentence despite the README and scientific-status files being current.
2. **Compact exact continuation receipts.** It includes the five complete layer profiles, replay engine, receipt and explicit evidence boundary behind the nonnesting theorem.
3. **Deterministic Stage B2 semantic manifests.** Wall-clock runtime is separated into `runtime.json`, so semantically identical reruns have identical `manifest.json` hashes.
4. **Sharper theorem-first governance.** It states a Myhill–Nerode-style minimal-state program, a trusted-checker contract, a Paper I claim freeze and an execution board.

## Reproduced checks

### Public GitHub line

GitHub Actions at the canonical commit completed successfully:

- Python 3.11 and 3.12 exact verification;
- `ruff check src tests`;
- 13 tests;
- `rgphi verify`;
- package build;
- integrity ledger;
- external-review bundle;
- Stage B2 exact smoke.

### Deployment 001 line

The compact receipt checker passed. The full exact continuation replay regenerated and byte-compared all five tables:

- `128/129 -> P2`: cost 42, endpoint `1100/1101`, 55,144 states;
- `1202/1203 -> P3`: cost 54, endpoint `13542/13543`, 3,955,616 states;
- `11156/11157 -> P4`: cost 48, endpoint `122088/122089`, 30,380,076 states;
- `11532/11533`: no `P4` hit within 42 actions, 11,442,439 states;
- `11642/11643`: no `P4` hit within 42 actions, 11,769,528 states.

The replay completed with `PASS_PAPER_I_FULL_EXACT_REPLAY`.

The Stage B2 smoke completed with 158 final states at time 90. Two independent reruns produced identical semantic-manifest hashes at every level.

## Comparative scorecard

| Dimension | Public GitHub | Deployment 001 | Winner |
|---|---:|---:|---|
| Canonical scientific authority | 9.5 | 8.4 | GitHub |
| Package/software architecture | 9.2 | 5.9 | GitHub |
| CI and hostile clean-room posture | 9.1 | 7.0 | GitHub |
| Publication architecture | 9.0 | 8.2 | GitHub |
| Compact Paper I continuation evidence | 7.4 | 9.5 | Deployment |
| Stage B2 semantic hash determinism | 7.0 | 9.3 | Deployment |
| Theorem-first execution specificity | 8.2 | 9.0 | Deployment |
| Duplication control / information architecture | 9.0 | 5.8 | GitHub |
| Overall research-object readiness | **9.0** | **7.7** | **GitHub** |

## Integration accepted

- corrected `paper/main.tex` and `paper/claim-evidence-matrix.csv`;
- synchronized Paper I PDF through CI;
- compact Paper I receipt, five exact profiles and C++ replay engine;
- independent compact checker and opt-in full replay script;
- Paper I receipt regression test;
- deterministic Stage B2 semantic manifests and determinism smoke;
- state-minimality theorem program;
- trusted-checker specification;
- claim freeze and theorem-first execution board;
- expanded referee questions for the computer-assisted proof boundary.

## Integration rejected

- duplicated historical superdocuments and nested bundles;
- the old `manuscripts/` and `certificates/` top-level architecture;
- the noninstallable `src` import convention from Deployment 001;
- full U5-HD archive duplication inside the mainline;
- any statement that upgrades local complementary-context evidence to a proved global orthomodular lattice;
- stale intervals or superseded gate narratives.

## Remaining blockers after fusion

- the 19.7 GB Stage B2 payload is still absent;
- the full depth-162 global layer is referenced but not compactly archived;
- independent clean-room replication remains open;
- the trap theorem is finite-atlas plus one exact kernel, not yet an infinite-family theorem;
- hidden-state sufficiency/minimality remains open;
- specialist MathSciNet/zbMATH and citation-chain closure remains required.

## Authority after fusion

1. machine-readable current canon and claims ledger;
2. primary exact certificates;
3. public GitHub repository and CI artifacts;
4. historical closure documents;
5. chat diagnostics.

The integrated repository is therefore a strict scientific and engineering improvement over either branch alone, without replacing the public mainline or erasing the secondary branch's stronger local evidence.
