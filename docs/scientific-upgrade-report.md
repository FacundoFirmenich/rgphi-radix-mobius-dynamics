# RGΦ — Scientific upgrade report

**Date:** 27 October 2026  
**Purpose:** identify and close the main scientific risks blocking an international journal submission.

## 1. Principal conclusion

The literature audit does not support presenting the individual ingredients of RGΦ as new. Radix maps, Möbius transformations, Farey systems, \(p\)-adic symbolic structures, state augmentation, open systems, modular cycles, and computer-assisted proofs all have substantial prior literatures.

The defensible novelty claim is narrower and stronger:

> RGΦ studies an exact interaction between rational radix dynamics, a Möbius-conjugate branch, primitive/Farey reduction, extremal first-hit optimization, hidden arithmetic context, and finite modular traps.

Priority remains a claim to be tested by specialist review, not assumed from an open-web search.

## 2. Ten-front upgrade program

### Front 1 — General base \(B\)

Status: **symbolically established**.

The branch formulas, determinant law, seed family, denominator law, and prime-wise reduction accounting extend naturally from base 10 to integer base \(B\ge2\).

Remaining task: produce nontrivial finite/extremal theorems beyond the decimal benchmark.

### Front 2 — Parameterized seeds

Status: **symbolically established**.

The benchmark seed is embedded in

\[
x_{N,r}=\frac{N}{N+r}.
\]

Remaining task: classify orbit behavior by arithmetic invariants of \((B,N,r)\).

### Front 3 — Parameterized thresholds

Status: **materially advanced**.

The target family

\[
P_m(B,\kappa)
\]

replaces the historical single threshold.

The benchmark chronology and nonnesting have exact positive-width \(\kappa\)-intervals.

### Front 4 — Theorems independent of \(\tau_5\)

Status: **closed for Paper I**.

Paper I no longer depends on resolving the depth-five optimum.

### Front 5 — Trap atlas

Status: **finite atlas closed; global classification open**.

The denominator-\(\le500\) atlas demonstrates that \(C_8\) belongs to a wider population of modularly structured finite components.

Remaining task: convert observed families into an infinite-family theorem and basin theory.

### Front 6 — Context algebra

Status: **corrected boundary**.

Local Boolean complement structure is exact. A global orthomodular object remains unproved.

### Front 7 — Reproducibility

Status: **strong internally**.

The repository contains exact code, tests, CI, paper build, metadata, and independent scripts.

Remaining task: external replication.

### Front 8 — External validation

Status: **pending**.

This is now the largest non-bibliographic validation gap.

### Front 9 — Literature and priority

Status: **open-web audit complete; specialist closure pending**.

Before submission, the project should add MathSciNet/zbMATH citation chaining and expert review.

### Front 10 — Scientific framing

Status: **corrected**.

The public framing explicitly excludes unsupported digit-correlation, physical, quantum, or cosmological claims.

## 3. Risk register

| Risk | Current severity | Mitigation |
|---|---:|---|
| prior-art collision on individual ingredients | high if overclaimed | claim coupling/theorems, not ingredients |
| benchmark specificity | medium | base-\(B\), seed, and \(\kappa\) parameterization |
| computational dependence | medium | exact evidence taxonomy and independent checkers |
| external replication gap | high | clean-room protocol |
| hidden-state theorem not generalized | medium-high | Paper II separation |
| orthomodular overclaim | controlled | terminology downgraded |
| \(\tau_5\) unresolved | low for Paper I | explicit open interval |
| threshold fine tuning | low | exact robustness interval |

## 4. Current research-level assessment

The program is publication-ready at the level of a specialized arithmetic/dynamical-systems contribution, provided the manuscript remains disciplined about scope.

The strongest present submission unit is Paper I.

The highest ceiling belongs to the future trap-family and hidden-state theorems.

## 5. Required pre-submission actions

1. freeze an English-only public repository;
2. complete closed-database citation audit;
3. solicit at least one specialist mathematical reading;
4. archive code/data release;
5. post manuscript on arXiv;
6. add independent replication when available;
7. submit the paper with claims restricted to the evidence map.
