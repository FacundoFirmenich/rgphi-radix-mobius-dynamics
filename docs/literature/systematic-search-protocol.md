# Systematic literature-review protocol

## Objective

Identify prior art, overlap, priority risk, and current-frontier developments for every headline RGΦ claim.

## Time windows

- **Canonical:** no date restriction.
- **Current frontier:** 1 January 2024 through the current review date.
- **Living update:** before each preprint version and each journal resubmission.

## Sources

### Open sources

- arXiv
- Crossref
- publisher/journal sites
- zbMATH Open
- OpenAlex
- Semantic Scholar
- Google Scholar for citation chaining

### Institutional sources when available

- MathSciNet
- Web of Science
- Scopus

## Core query families

1. “beta transformation rational periodic orbit Möbius conjugacy”
2. “integer radix transformation projective continued fraction”
3. “Farey map hidden coordinate natural extension”
4. “rational Möbius semigroup exact dynamics”
5. “nonnested hitting times dynamic programming arithmetic”
6. “finite rational invariant trap continued fraction map”
7. “survivor set integer base rational point”
8. “p-adic phase symbolic dynamics rational map”
9. “computer assisted proof reachability exact rational dynamics”
10. “multiplicative order finite invariant set radix map”

Queries should be expanded with synonyms and names found during citation chaining.

## Claim-centered workflow

For each claim:

1. state the claim in theorem-level language;
2. identify the closest standard object;
3. search by object, not by RGΦ terminology;
4. find canonical references;
5. find recent papers;
6. follow references backward;
7. follow citations forward;
8. record nearest overlap;
9. classify novelty risk;
10. rewrite the public claim conservatively.

## Risk levels

### Low

The exact theorem appears structurally distinct after direct comparison.

### Medium

Nearby literature contains similar constructions but not the same theorem.

### High

A close theorem, natural extension, invariant-set construction, or equivalent reformulation may already exist.

High-risk claims require specialist review before submission.

## Current high-risk areas

- hidden \(p\)-adic/Farey state;
- projective/Farey classification language;
- global trap classification;
- orthomodular/contextual algebra terminology;
- Artin/Kummer density claims.

## Output artifacts

- literature-matrix.csv
- claim-to-literature-map.csv
- claims-with-priority.csv
- literature-priority-audit.md
- current-frontier-2024-2026.md
- paper/references.bib

## Review standard

A literature search can support “we are not aware of” language.

It cannot, by itself, prove absolute historical priority.
