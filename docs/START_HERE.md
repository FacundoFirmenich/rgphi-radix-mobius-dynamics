# Start here

RGΦ is a research compendium, not a single paper or software package. This page provides short reading paths for different audiences.

## Ten-minute orientation

1. Read the first three sections of the [repository README](../README.md).
2. Read [Scientific status](SCIENTIFIC_STATUS.md) for the proved/open/superseded boundary.
3. Inspect the [claim–evidence matrix](../paper/claim-evidence-matrix.csv).
4. Read the abstract and main theorem of [Paper I](../paper/main.pdf).

## For a dynamics or continued-fractions referee

1. [Paper I](../paper/main.pdf)
2. [Focused referee packet](validation/REFEREE_PACKET.md)
3. [Claim-by-claim literature positioning](literature/CLAIM_BY_CLAIM_POSITIONING.md)
4. [Adversarial internal referee report](validation/ADVERSARIAL_REFEREE_REPORT.md)
5. [External review scorecard](validation/REVIEW_SCORECARD.md)

Primary questions:

- Is the partial radix–Möbius system defined unambiguously?
- Is the exact nonnesting theorem mathematically meaningful?
- Is there an equivalent or substantially anticipatory theorem in Farey/projective/continued-fraction dynamics?
- Are the threshold endpoint conventions correct?

## For a number theorist or arithmetic dynamicist

1. [Base-B theorem portfolio](theorems/base-B-theorem-portfolio.md)
2. [Scientific status](SCIENTIFIC_STATUS.md)
3. [Finite-trap classification](theorems/trap-classification-theorem.md)
4. [Literature priority audit](literature/literature-priority-audit.md)
5. [Open problems](OPEN_PROBLEMS.md)

Primary questions:

- Are primitive-reduction and denominator arguments scoped correctly?
- Is the finite modular-trap mechanism structurally nontrivial?
- Which claims belong to standard arithmetic dynamics, numeration, or multiplicative-order theory?

## For an independent computational replicator

1. [External validation protocol](validation/EXTERNAL_VALIDATION_PROTOCOL.md)
2. [Machine-readable validation targets](../metadata/VALIDATION_TARGETS.json)
3. [Replication report template](validation/REPLICATION_REPORT_TEMPLATE.md)
4. [Reproducibility guide](../REPRODUCIBILITY.md)
5. [Reference package](../src/rgphi)

A clean-room implementation should use the mathematical specification, not copy the reference program architecture.

## For an archivist or research-software reviewer

1. [FAIR and archival richness](FAIR_AND_ARCHIVAL_RICHNESS.md)
2. [Artifact catalog](ARTIFACT_CATALOG.md)
3. [Research-object registry](../metadata/ARTIFACT_REGISTRY.json)
4. [DataCite draft](../metadata/DATACITE_METADATA_DRAFT.json)
5. [Release policy](../RELEASE.md)
6. [Pre-DOI archival checklist](../metadata/PRE_DOI_ARCHIVAL_CHECKLIST.md)

## For a software user

```bash
python -m pip install -e '.[dev]'
ruff check src tests
pytest
rgphi verify
```

Then inspect:

- `src/rgphi/dynamics.py`
- `src/rgphi/traps.py`
- `src/rgphi/verification.py`
- `tests/`

## For a full scientific review

Use this order:

1. [Integrated research closure](integrated-research-closure.md)
2. [Paper I](../paper/main.pdf)
3. [Evidence model](EVIDENCE_MODEL.md)
4. [Scientific status](SCIENTIFIC_STATUS.md)
5. [Literature audit](literature/literature-priority-audit.md)
6. [Validation protocol](validation/EXTERNAL_VALIDATION_PROTOCOL.md)
7. [Open problems](OPEN_PROBLEMS.md)

## Canonical status statement

The first four benchmark hitting times and their robustness intervals are exact finite-computational theorems. The global depth-five value remains open:

\[
179\le \tau_5\le 212.
\]

No document in the repository should be interpreted as claiming otherwise.
