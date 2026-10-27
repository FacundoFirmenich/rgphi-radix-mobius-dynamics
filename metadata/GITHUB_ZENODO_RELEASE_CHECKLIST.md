# GitHub → Zenodo archival checklist

**Current state:** repository exists and is public; archival DOI intentionally pending.

## Before enabling the archival release

- [ ] Complete metadata/PRE_DOI_ARCHIVAL_CHECKLIST.md.
- [ ] Confirm main contains the intended frozen tree.
- [ ] Confirm Exact verification workflow is green.
- [ ] Confirm Build paper workflow is green.
- [ ] Review README and SCIENTIFIC_STATUS.md.
- [ ] Review paper/main.pdf visually.
- [ ] Confirm VERSION, pyproject.toml, CITATION.cff, CodeMeta, and .zenodo.json are consistent.
- [ ] Regenerate MANIFEST.json and SHA256SUMS.txt after the final content freeze.

## Zenodo sequence

1. Connect the GitHub account to Zenodo.
2. Enable FacundoFirmenich/rgphi-radix-mobius-dynamics.
3. Freeze the repository and create tag v1.0.0.
4. Create the GitHub Release from that exact tag.
5. Inspect the Zenodo draft before publication.
6. Verify title, creator, ORCID, affiliation, version, licenses, description, and related GitHub identifier.
7. Publish the Zenodo record.
8. Record both the version DOI and concept DOI.
9. Cross-link the DOI in the next metadata commit.

## Important

Do **not** mint the DOI from an intermediate release candidate merely because the repository is public.

The archival object should represent a coherent, reviewable scientific snapshot.
