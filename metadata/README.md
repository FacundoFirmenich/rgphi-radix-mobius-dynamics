# Metadata and research-object records

This directory contains machine-readable descriptions of the RGΦ research object.

## Core records

- `ARTIFACT_REGISTRY.json` — canonical artifact roles, evidence classes, media types, and licenses;
- `VALIDATION_TARGETS.json` — exact expected outputs for clean-room replication;
- `DATACITE_METADATA_DRAFT.json` — pre-DOI DataCite crosswalk;
- `datapackage.json` — Frictionless-style research-data package;
- `PROVENANCE.jsonld` — PROV-O / schema.org provenance graph;
- `CREDIT.json` — contributor roles using the CRediT taxonomy;
- `EXTERNAL_VALIDATION_LEDGER.json` — status of independent review and replication roles;
- `ro-crate-metadata.json` — RO-Crate metadata;
- `SBOM.spdx.json` — software bill of materials;
- `arxiv-metadata.json` — manuscript-deposit metadata;
- `PRE_DOI_ARCHIVAL_CHECKLIST.md` — freeze checklist.

## Identifier policy

The repository does not invent identifiers. DOI, SWHID, and container digest fields remain `PENDING` or absent until assigned by the relevant archive.

## Version policy

All version-bearing metadata must agree with:

- root `VERSION`;
- `pyproject.toml`;
- `CITATION.cff`;
- `.zenodo.json`;
- `codemeta.json`;
- DataCite and data-package drafts.

The research-object audit checks this consistency automatically.
