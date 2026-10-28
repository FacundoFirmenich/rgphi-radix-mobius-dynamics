# Artifact catalog

This catalog identifies the principal scientific objects in the repository and their evidentiary roles.

| artifact | role | evidence class | canonical path |
|---|---|---|---|
| Paper I PDF | submission-oriented mathematical exposition | S/F | `paper/main.pdf` |
| Paper I source | canonical editable manuscript | S/F | `paper/main.tex` |
| Claim–evidence matrix | paper claim to evidence mapping | meta | `paper/claim-evidence-matrix.csv` |
| Scientific status | authoritative proved/open boundary | meta | `docs/SCIENTIFIC_STATUS.md` |
| Evidence model | evidence taxonomy and promotion rules | meta | `docs/EVIDENCE_MODEL.md` |
| Exact dynamics package | inspectable reference implementation | S/F | `src/rgphi/` |
| Regression tests | theorem-level executable checks | S/F | `tests/` |
| Threshold evidence | exact first-hit and robustness tables | F | `data/thresholds/` |
| Terminal-set audit | closure of the declared terminal convention | F | `data/certificates/terminal-set-audit.json` |
| C8 audit | exact forward-invariant trap evidence | F | `data/traps/C8-exact-audit.csv` |
| D≤500 trap atlas | finite graph census | F | `data/traps/trap-atlas-result-D500.json` |
| Large-search summaries | high-cost exact search records | C | `data/certificates/` |
| Literature matrix | source-level positioning evidence | meta | `docs/literature/literature-matrix.csv` |
| Validation targets | independent replication oracle | meta | `metadata/VALIDATION_TARGETS.json` |
| Artifact registry | machine-readable research-object index | meta | `metadata/ARTIFACT_REGISTRY.json` |
| Research-object audit | metadata/path consistency verifier | meta | `tools/validate_research_object.py` |

## Evidence classes

- **S:** symbolic theorem or derivation.
- **F:** complete finite exhaustive computation.
- **C:** large exact computer-assisted result.
- **O:** open statement, conjecture, or incomplete bound.
- **meta:** provenance, navigation, or evidence-control artifact.

## Canonical-versus-historical rule

Historical artifacts may remain in the repository for provenance. Scientific status is determined by `docs/SCIENTIFIC_STATUS.md`, not by file age or gate number.

## License split

- code: BSD 3-Clause;
- papers, documentation, and research data: CC BY 4.0.
