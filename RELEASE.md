# Release procedure

1. Run `pytest`, `ruff check src tests`, and `rgphi verify`.
2. Compile `paper/main.tex` twice and inspect the rendered PDF.
3. Update `VERSION`, `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json`, and `codemeta.json`.
4. Regenerate `MANIFEST.json` and `SHA256SUMS.txt`.
5. Commit and tag `vX.Y.Z` (or the release candidate tag).
6. Push the tag to GitHub.
7. Enable the repository in Zenodo before creating the archival GitHub release.
8. Create the GitHub release from the tag; verify the Zenodo record and metadata.
9. Add the minted concept/version DOI to the README, CITATION.cff, CodeMeta, and the paper data-availability statement in the next version.
10. Submit the LaTeX source bundle to arXiv and cross-link identifiers after announcement.
