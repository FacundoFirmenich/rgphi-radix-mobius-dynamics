# Repository guide

This guide explains what a reader should inspect for each scientific question.

## If you want the paper

Start with:

- paper/main.pdf
- paper/main.tex
- paper/supplement.md
- paper/claim-evidence-matrix.csv

The paper is intentionally narrower than the full project.

## If you want the exact dynamics

Read:

- src/rgphi/dynamics.py
- tests/test_dynamics.py
- docs/theorems/base-B-theorem-portfolio.md

The reference implementation uses fractions.Fraction for theorem-critical arithmetic.

## If you want the nonnesting result

Read:

- data/thresholds/exact-bfs-depth-0-162.csv
- data/thresholds/portal-continuation-costs.csv
- data/thresholds/greedy-failure.csv
- data/thresholds/nonnesting-robustness.csv
- docs/theorems/threshold-robustness-atlas.md
- tests/test_thresholds.py

## If you want the finite-trap result

Read:

- docs/theorems/trap-classification-theorem.md
- data/traps/C8-exact-audit.csv
- data/traps/trap-atlas-result-D500.json
- data/traps/closed-sccs-D500.csv
- data/traps/forward-closures-D500.csv
- src/rgphi/traps.py
- tests/test_traps.py

## If you want to understand the evidence boundary

Read:

- docs/SCIENTIFIC_STATUS.md
- docs/EVIDENCE_MODEL.md
- paper/claim-evidence-matrix.csv
- REPRODUCIBILITY.md

## If you want the literature context

Read:

- docs/literature/literature-priority-audit.md
- docs/literature/current-frontier-2024-2026.md
- docs/literature/claim-to-literature-map.csv
- paper/references.bib

The literature audit is a living risk analysis. It is not a substitute for referee review or specialist priority assessment.

## If you want to reproduce the repository

Use:

~~~bash
python -m pip install -e '.[dev]'
pytest
ruff check src tests
rgphi verify
~~~

For an independent implementation, follow docs/reproducibility/protocol.md rather than copying the reference functions line by line.

## If you want archival metadata

Inspect:

- CITATION.cff
- codemeta.json
- metadata/ro-crate-metadata.json
- metadata/SBOM.spdx.json
- .zenodo.json

These files are intentionally kept in pre-DOI state until archival freezing.
