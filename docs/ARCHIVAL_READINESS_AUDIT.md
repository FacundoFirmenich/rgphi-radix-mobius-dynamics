# Archival readiness audit

**Current phase:** pre-DOI release candidate  
**Scoring target before archival freeze:** >= 9.2/10

## Scoring rubric

| dimension | weight | current status |
|---|---:|---|
| scientific claim consistency | 20% | excellent |
| English/public documentation | 15% | excellent |
| exact reproducibility / CI | 20% | excellent |
| manuscript build and visual integrity | 10% | excellent |
| metadata consistency | 10% | excellent |
| integrity ledger | 10% | automated; final frozen ledger pending |
| repository hygiene | 5% | one manual default-branch change pending |
| archival identifiers / preservation | 10% | deliberately pending |

## Current audit

### Scientific consistency — 10/10

- explicit proved/open boundary;
- \(\tau_5\) open;
- superseded witness labelled correctly;
- terminal set now machine-audited;
- trap claims scoped;
- context-semantics overclaim removed.

### Documentation — 9.6/10

Canonical public documents are in academic English and organized for an external reader.

### Reproducibility — 9.5/10

- Python 3.11 and 3.12 CI;
- exact rational reference package;
- theorem-level tests;
- independent scripts;
- reproducibility protocol;
- deterministic finite computations.

External clean-room replication is scored separately under external validation.

### Manuscript build — 9.7/10

- clean LaTeX build;
- no undefined references;
- rendered PDF inspected;
- source and evidence map public.

### Metadata — 9.5/10

CFF, CodeMeta, Zenodo draft metadata, arXiv metadata, ORCID, repository identity, and license split are aligned in release-candidate form.

### Integrity ledger — 9.2/10

A workflow generates MANIFEST.json and SHA256SUMS.txt from the exact current tree.

The final ledger must be regenerated and committed at the v1.0.0 freeze.

### Repository hygiene — 8.8/10

Zero unintended open PRs and no stale checked-in hash ledger.

Remaining manual action:

> GitHub Settings -> Branches -> Default branch -> main

The legacy branch can then be removed if desired.

### Archival preservation — 7/10 before deposition

Zenodo DOI and Software Heritage identifier intentionally do not yet exist.

This category becomes 10/10 after the frozen tag is archived and identifiers are cross-linked.

## Pre-DOI readiness score

Using the weighted rubric and treating unminted identifiers as intentionally pending:

\[
\boxed{9.25/10}
\]

for **pre-DOI technical readiness**.

The score does not imply that external mathematical validation is complete.

## Final archival freeze sequence

1. switch default branch to main;
2. close external validation and literature gates;
3. bump release metadata from 1.0.0-rc.1 to 1.0.0;
4. regenerate final PDF;
5. run all CI;
6. generate and commit final MANIFEST.json and SHA256SUMS.txt;
7. create tag v1.0.0;
8. create GitHub Release;
9. archive in Zenodo and inspect draft;
10. publish DOI;
11. archive in Software Heritage;
12. cross-link DOI/SWHID/arXiv.

Expected archival-readiness score after these steps:

\[
\boxed{9.8/10}.
\]
