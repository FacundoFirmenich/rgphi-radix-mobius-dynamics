# Validation and archival elevation roadmap

**Goal:** reach an evidence-based score above 9/10 in three independent dimensions before minting the archival DOI:

1. archival readiness;
2. literature positioning;
3. external mathematical validation.

The scores are not promotional ratings. Each is tied to observable exit criteria.

## Gate A — Archival readiness

### A1. Canonical public documentation

Required:

- academic-English README;
- scientific-status boundary;
- evidence taxonomy;
- repository guide;
- open-problem register;
- release policy;
- reproducibility protocol.

Status: **closed**.

### A2. Scientific consistency

Required:

- manuscript agrees with repository claims;
- terminal convention is machine-audited;
- \(\tau_5\) is explicitly open everywhere;
- superseded 217-step witness is not presented as current;
- finite trap claims are scoped to their finite evidence where appropriate.

Status: **closed internally**.

### A3. Software and manuscript verification

Required:

- Python 3.11 CI PASS;
- Python 3.12 CI PASS;
- exact repository verifier PASS;
- LaTeX build PASS;
- rendered PDF visually inspected;
- package build PASS.

Status: **closed internally**.

### A4. Integrity and archival metadata

Required:

- regenerated manifest from the frozen tree;
- SHA-256 ledger;
- consistent VERSION / pyproject / CFF / CodeMeta / Zenodo metadata;
- ORCID and license split checked;
- release notes generated from the same commit.

Status: **ready for final freeze; final v1.0.0 ledger intentionally deferred until the freeze commit**.

### A5. Repository hygiene

Required:

- default branch = main;
- zero unintended open PRs;
- no bootstrap/staging artifacts;
- no canonical Spanish-only documentation;
- no stale checked-in hashes.

Status: **one manual GitHub setting remains: default branch should be changed to main**.

### A6. Archival deposition

Required:

- v1.0.0 tag;
- GitHub Release;
- Zenodo version DOI and concept DOI;
- post-deposit cross-links;
- Software Heritage archival when available.

Status: **intentionally pending**.

### Gate-A score rule

A score >= 9.2 requires A1–A5 complete and A6 fully prepared.  
A score >= 9.7 requires the DOI/tag/archive to exist and resolve.

## Gate B — Literature positioning

### B1. Canonical literature

Map the project against:

- radix / beta transformations;
- continued fractions and Farey maps;
- Möbius/projective systems;
- arithmetic dynamics;
- hitting/return-time theory;
- dynamic programming and state augmentation;
- open systems / survivor sets;
- \(p\)-adic dynamics;
- formal certificates / computer-assisted proof.

Status: **closed at open-source level**.

### B2. 2024–2026 frontier

Required:

- current published and arXiv work in projective/Farey systems;
- recent natural-extension and continued-fraction constructions;
- finite rational-orbit statistics;
- rational semigroup actions;
- open-system survivor sets;
- \(p\)-adic Möbius/continued-fraction arithmetic;
- modern proof-certificate literature.

Status: **materially closed; living update required before submission**.

### B3. Claim-by-claim nearest-prior-art table

Each headline claim must list:

- nearest known theorem/object;
- overlap;
- exact distinction;
- novelty risk;
- permitted wording.

Status: **closed in CLAIM_BY_CLAIM_POSITIONING.md**.

### B4. Manuscript integration

The paper itself must cite and discuss the nearest recent work, rather than delegating novelty to repository notes.

Status: **closed in the current source revision**.

### B5. Closed-database / specialist priority check

Required:

- MathSciNet or equivalent citation chaining;
- zbMATH follow-up;
- at least two domain specialists asked whether a closer theorem is known.

Status: **external component pending**.

### Gate-B score rule

>= 9.0: B1–B4 complete with conservative novelty language.  
>= 9.3: B5 receives no unresolved priority collision.  
>= 9.6: specialist feedback is incorporated and the claim map is version-pinned.

## Gate C — External mathematical validation

Internal self-review does not count toward this score.

### C1. Adversarial internal referee simulation

Purpose: eliminate avoidable objections before asking external researchers.

Status: **closed**.

### C2. Specialist referee A — dynamics / continued fractions

Required review topics:

- formal partial-semigroup definition;
- relation to Farey / natural-extension literature;
- nonnesting theorem and threshold robustness;
- novelty boundary.

Candidate profiles include researchers active in continued fractions, projective interval maps, or arithmetic dynamics.

### C3. Specialist referee B — arithmetic dynamics / number theory

Required review topics:

- exact rational reduction;
- modular trap mechanism;
- multiplicative-order arguments;
- arithmetic generalization claims.

### C4. Independent computational replicator

Clean-room reproduction target, without copying the reference implementation:

1. 23-state terminal-set closure;
2. \(\tau_1=45,\tau_2=85,\tau_3=120,\tau_4=162\);
3. continuation times 87, 139, 168;
4. robustness intervals;
5. \(C_8\) closure;
6. denominator-500 trap-atlas summary counts.

### C5. Resolution round

Every major or critical objection must produce one of:

- accepted correction;
- additional proof/evidence;
- narrowed claim;
- documented disagreement.

A second reviewer pass confirms closure.

### Gate-C score rule

External validation < 9 until actual third-party reports exist.

Score >= 9.0 requires:

- two independent mathematical reviews;
- no unresolved critical issue;
- at least one independent reproduction of the core finite theorem stack.

Score >= 9.5 additionally requires:

- reviewer feedback archived or summarized with consent;
- clean-room counts/hashes match;
- all material comments incorporated and rechecked.

## Preferred execution order

1. Freeze current internal quality.
2. Send a short introduction request through the existing FAMAF/UNC relationship.
3. In parallel, request one direct field-specialist read.
4. Run clean-room replication independently.
5. Resolve comments.
6. Freeze v1.0.0.
7. Mint Zenodo DOI.
8. Submit arXiv version.
9. Request journal-level specialist feedback or submit to the target journal.

## Stop condition

Do not mint the archival DOI merely because the code is green.

The archive gate opens when:

\[
\boxed{
A\ge9.2,\qquad B\ge9.2,\qquad C\ge9.0.
}
\]
