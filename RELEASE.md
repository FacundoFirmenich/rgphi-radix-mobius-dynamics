# Release and archival policy

The repository is currently in a **public pre-DOI release-candidate phase**.

A public GitHub repository is not, by itself, the archival release.

## 1. Pre-DOI freeze criteria

Do not mint the Zenodo DOI until all of the following are true:

- [ ] README is publication-grade academic English.
- [ ] Public scientific documentation is publication-grade academic English.
- [ ] SCIENTIFIC_STATUS.md matches the manuscript and code.
- [ ] Open results are explicitly separated from proved results.
- [ ] paper/main.tex and paper/main.pdf are frozen for the archival snapshot.
- [ ] paper/claim-evidence-matrix.csv has no unresolved headline claim.
- [ ] pytest passes.
- [ ] ruff check src tests passes.
- [ ] rgphi verify passes.
- [ ] GitHub CI is green on Python 3.11 and 3.12.
- [ ] GitHub paper-build workflow is green.
- [ ] CITATION.cff, CodeMeta, RO-Crate, and .zenodo.json agree on title, authorship, version, and license.
- [ ] VERSION and pyproject.toml agree.
- [ ] MANIFEST.json and SHA256SUMS.txt are regenerated from the frozen tree.
- [ ] literature-priority language has been reviewed for overclaiming.
- [ ] no temporary, Spanish-only, or internal-process document is presented as canonical public documentation.

## 2. Versioning

During repository maturation use release-candidate versions:

\[
1.0.0\text{-rc}.N.
\]

The first Zenodo archival release should be tagged:

\[
\boxed{v1.0.0}
\]

only after the freeze criteria pass.

## 3. Final pre-release commands

~~~bash
ruff check src tests
pytest
rgphi verify

cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd ..

python tools/update_manifest.py
~~~

Review the resulting manifest and checksums before tagging.

## 4. Archival sequence

1. Freeze the repository on main.
2. Create annotated tag v1.0.0.
3. Create the GitHub release from that exact tag.
4. Archive the release through the connected Zenodo repository.
5. Inspect the Zenodo metadata before publication.
6. Mint the DOI.
7. Add the DOI to README, CITATION.cff, CodeMeta, and the manuscript data/code availability statement in a post-archive metadata commit or the next patch release.
8. Submit the manuscript source to arXiv and cross-link the identifiers.

## 5. DOI object policy

The Zenodo DOI identifies the **software/data/research compendium release**.

The manuscript will have its own arXiv identifier and, if accepted by a journal, a later publisher DOI.

These identifiers should be cross-linked rather than conflated.

## 6. Release integrity

No release should be created from an unverified intermediate tree.

The archival release notes must explicitly report:

- Git commit SHA;
- release tag;
- test status;
- paper-build status;
- evidence boundary;
- open value of \(\tau_5\).
