# Pre-DOI archival checklist

**Purpose:** prevent premature Zenodo archival of an immature repository.

## Scientific freeze

- [ ] README accurately states the scientific object and current boundaries.
- [ ] SCIENTIFIC_STATUS.md agrees with paper/main.tex.
- [ ] \(\tau_5\) is explicitly open everywhere.
- [ ] 217-step result is labelled superseded globally.
- [ ] trap-atlas claims do not exceed denominator-bound evidence.
- [ ] hidden-state claims are not promoted beyond their evidence class.
- [ ] context semantics do not claim a global OMP/OML theorem.

## Language and presentation

- [ ] canonical public documentation is academic English;
- [ ] no internal conversational wording remains in canonical documents;
- [ ] no unexplained gate chronology is required to understand the project;
- [ ] equations render correctly on GitHub;
- [ ] repository navigation is clear to a new mathematical reader.

## Reproducibility

- [ ] Python 3.11 CI green;
- [ ] Python 3.12 CI green;
- [ ] paper build green;
- [ ] pytest green;
- [ ] ruff green;
- [ ] rgphi verify green;
- [ ] clean-room protocol documented.

## Metadata

- [ ] VERSION frozen;
- [ ] pyproject version matches VERSION;
- [ ] CITATION.cff matches authorship/title/version;
- [ ] .zenodo.json matches release metadata;
- [ ] codemeta.json matches release metadata;
- [ ] RO-Crate metadata reviewed;
- [ ] license split is explicit;
- [ ] ORCID verified.

## Literature

- [ ] open-web literature audit complete;
- [ ] MathSciNet/zbMATH follow-up completed or explicitly noted as pending;
- [ ] specialist priority review requested;
- [ ] manuscript novelty language is conservative and sourceable.

## Archive

Only after all applicable checks are complete:

1. tag v1.0.0;
2. create GitHub Release;
3. archive the exact tag in Zenodo;
4. inspect metadata before publishing;
5. mint DOI;
6. cross-link DOI and arXiv identifiers.
