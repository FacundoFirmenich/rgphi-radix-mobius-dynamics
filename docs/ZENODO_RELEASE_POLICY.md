# Zenodo release policy

**Scope:** archival and citation policy for the RGΦ publication portfolio. This policy does not mint a DOI and does not authorize a scientific release by itself.

## One repository, one research object

Each paper-scale repository is archived independently. The GitHub repository is the live development object; each accepted release is an immutable archival version in Zenodo.

The repository must be public before Zenodo GitHub archiving is enabled. Zenodo integration is activated only when the first archival release candidate has passed the repository freeze checklist.

## Metadata sources

Every repository carries both:

- `CITATION.cff`, used by GitHub to display the preferred citation;
- `.zenodo.json`, used for Zenodo-specific metadata and cross-object relations.

When both are present, `.zenodo.json` is the metadata source for Zenodo ingestion. A repository checker must verify that title, creators, ORCID, version, release date, repository URL and license do not conflict across the two files.

Canonical creator identity:

- **Facundo Firmenich**
- ORCID: `0009-0002-6578-3811`
- Affiliation: `Centro de Estudios del Sur (CEDESUR), Universidad Nacional Arturo Jauretche`

Additional creators and contributors are included only when their roles and authorship satisfy the relevant contribution policy; no automated system is listed as an author.

## Versioning

Development commits do not mint DOIs. The minimum archival sequence is:

1. `v0.x.y` — optional public research-object releases when scientifically useful;
2. `v1.0.0` — first manuscript-associated archival release;
3. `v1.0.1`, `v1.1.0`, … — new immutable versions when files materially change;
4. a journal-linked release after acceptance, related to the article DOI without replacing either identifier.

Each Zenodo version receives its own persistent identifier and remains linked to previous and future versions. Citations in a paper should use the specific release DOI that reproduces the reported results.

## Release contents

A Zenodo software release should contain preservation-friendly, self-contained source material. Large datasets or checkpoints may be deposited as separate dataset records and linked using `related_identifiers`.

Required release contents:

- source code required to reproduce or check the central results;
- frozen manuscript source and compiled manuscript when applicable;
- claim–evidence ledger;
- machine-readable metrics;
- independent checker;
- environment lock or deterministic build description;
- SHA-256 inventory;
- known limitations and failed gates;
- explicit license files.

Prohibited release contents:

- credentials, tokens, private correspondence or native chat databases;
- unverifiable synthetic substitutes for missing scientific artefacts;
- duplicated multi-gigabyte outcomes already archived under another DOI;
- claims whose supporting gate remains open;
- generated caches, temporary binaries and mutable runtime state.

## Relationship metadata

Use `.zenodo.json` `related_identifiers` to express relations such as:

- software `isSupplementTo` an article;
- a paper repository `references` a dataset or another software release;
- a dataset `isSupplementTo` the corresponding paper;
- a new object `isDerivedFrom` a precisely identified prior release.

Relations must point to immutable DOIs or tagged releases whenever available, not to an unversioned default branch.

## Freeze checklist

A release tag may be created only when all items are true:

- scientific scope frozen;
- primary claims and exclusions frozen;
- version synchronized across metadata files;
- authorship and contributor roles reviewed;
- all tests and independent checkers pass;
- manuscript references exact tagged artefacts;
- file inventory and checksums regenerated after the last change;
- no oversized artefact is silently omitted;
- release notes identify negative results and open boundaries;
- the release is reproducible from a fresh checkout or the remaining external dependency is explicitly DOI-addressed.

## DOI timing

Do not enable automatic Zenodo archiving for exploratory repositories. Enable it immediately before the first intended archival GitHub release. After enabling, each GitHub release is treated as an archival event and must satisfy this policy.
