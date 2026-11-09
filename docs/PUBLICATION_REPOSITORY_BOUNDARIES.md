# Publication repository boundaries

**Status:** governance proposal for the publication portfolio; no scientific claim is changed by this document.

## Governing principle

Each paper-sized scientific object must have one canonical repository, one claim ledger, one reproducibility contract, one release history, and one eventual Zenodo record. Cross-repository relations are expressed through immutable release identifiers and `related_identifiers`; scientific artefacts are not silently duplicated or allowed to diverge.

The research programme remains integrated at the strategic level, but publication objects are separated at the evidentiary and archival levels.

## Canonical repository map

| Scientific object | Repository status | Canonical repository or planned slug | Authority |
|---|---|---|---|
| Exact RGΦ dynamics, portal times, Bellman certificates and traps | Existing | `FacundoFirmenich/rgphi-radix-mobius-dynamics` | `CANONICAL_ACTIVE` |
| Exact adaptive quaternary tomography and signed-permutation query complexity | Planned autonomous repository | `quaternary-signed-permutation-tomography` | `EXPERIMENTAL_MATHEMATICS`; independent paper |
| RGΦ-GEN / observational activation surfaces, modular rank, resolution and time | Planned autonomous repository | `radix-mobius-activation-surfaces` | `PARALLEL_ISOLATED`; independent paper |
| Exact rational-dynamics certification, trusted checkers and reproducibility methods | Planned autonomous repository | `exact-rational-dynamics-certification` | `METHODS_COMPANION` |
| Stable Toeplitz interfaces, unbounded Kasparov cycles and Real/APS refinements | Planned autonomous repository | `stable-toeplitz-kasparov-interfaces` | `EXPERIMENTAL_ISOLATED`; independent paper |
| Observational degeneration and higher-order observer synergy | Planned autonomous repository | `observational-degeneration-synergy` | `FOUNDATIONS_TRACK`; independent paper |
| U5-HD integrated prearchitecture and programme-level synthesis | Planned private programme repository | `u5-hd-research-program` | `PROGRAMME_CENTRUM`; not a paper release at present |

## Existing external validation repositories

The following repositories remain autonomous research objects and are not to be copied into the paper repositories:

- `FacundoFirmenich/sysmic` — seismic fractal tomography and Fisher-information barriers;
- `FacundoFirmenich/KwanTube` — nonperturbative quantum dynamics and model-jurisdiction tests;
- `FacundoFirmenich/fractal_analysis_of_seismics` — precursor seismic analysis;
- `FacundoFirmenich/scale-dependent-spacetime-geometry` — scale-dependent effective geometry.

Paper repositories may cite immutable releases from these projects as external evidence, but they may not rewrite their outcomes.

## Non-duplication rules

1. A theorem, computational certificate or dataset has one authoritative location.
2. A second repository may contain a small frozen verification fixture only when required for independent checking; the source release and checksum must be recorded.
3. Large outcomes and checkpoints are deposited as release assets or separate Zenodo datasets, not committed repeatedly to Git history.
4. Manuscript prose may summarize results from another repository, but the claim ledger must identify the source release or commit.
5. Experimental U5-HD results have no authority to modify RGΦ mainline claims.
6. Negative results, abstentions, censored windows and failed promotion gates remain part of the permanent record.

## Release boundary

A repository becomes eligible for its first archival release only after it contains:

- a stable scientific title and scope;
- `CITATION.cff` and `.zenodo.json` with synchronized authorship and version metadata;
- an explicit software and documentation/data licensing policy;
- a claim–evidence ledger;
- a reproducibility or proof contract;
- an independent checker or a clearly declared reason why none is applicable;
- a frozen manuscript or paper outline tied to the release;
- a complete file inventory and SHA-256 manifest;
- a release checklist signed off without unresolved critical claims.

## Relationship to this repository

This repository remains the sole canonical home of RGΦ exact dynamics. It must not become the umbrella repository for BQ, HM, observational foundations or the entire U5-HD programme. Those objects will refer back to tagged RGΦ releases when needed.
