# Literature, priority, and novelty audit

**Cutoff:** 27 October 2026  
**Coverage:** canonical background plus a focused 2024–2026 frontier review  
**Status:** open-source audit complete; MathSciNet/zbMATH/Scopus/Web of Science closure and specialist review remain pending

## 1. Executive conclusion

The literature review changes the framing of RGΦ in an important way.

The individual ingredients belong to mature literatures:

- integer-radix and beta transformations;
- continued fractions, Farey and Gauss maps;
- Möbius/projective dynamical systems;
- rational symbolic codings and natural extensions;
- \(p\)-adic dynamics and cylinder structures;
- dynamic programming and state augmentation;
- open dynamical systems, survivor sets, and trapping;
- multiplicative orders and Artin-type arithmetic;
- computer-assisted proof and model-checking certificates.

Accordingly, the project should **not** claim priority for any of these ingredients in isolation.

The defensible research question is whether the particular exact coupling in RGΦ yields theorems not already documented in nearby systems, especially:

1. robust nonnested extremal targets;
2. arithmetic counterexamples to scalar Bellman summaries;
3. hidden Farey/\(p\)-adic control within the rational semigroup;
4. prime-wise reduction-budget structure;
5. finite modular traps with exact no-escape consequences.

No absolute priority claim is made before closed-database and specialist review.

## 2. Literature clusters

### 2.1 Radix and beta transformations

Relevant background includes the classical Rényi–Parry theory and subsequent work on beta expansions, invariant measures, periodic rational orbits, symbolic coding, and natural extensions.

RGΦ overlap: \(T_B(x)=\{Bx\}\) is standard in spirit.

Potential contribution: the interaction with a Möbius-conjugate control branch and extremal dynamic-programming objective.

### 2.2 Farey, Gauss, and continued-fraction dynamics

The Farey/Gauss ecosystem contains extensive results on inducing, first-return maps, projective branches, geodesic codings, and natural extensions.

RGΦ must therefore avoid presenting “Farey geometry” itself as novel.

Potential contribution: the use of exact Farey-neighbor/context data as a control-relevant hidden coordinate in the radix–Möbius semigroup.

### 2.3 Möbius and projective semigroups

Matrix and linear-fractional representations of interval dynamics are established tools.

Potential contribution: the exact determinant-\(B\) branch family coupled to primitive rational reduction and extremal hitting objectives.

### 2.4 \(p\)-adic and symbolic dynamics

\(p\)-adic shifts, cylinders, symbolic interpreters, and ultrametric state structures are established.

Potential contribution: a minimal arithmetic augmentation theorem explaining when visible rational state fails to determine future extremal value.

### 2.5 Bellman state and non-Markovian control

Dynamic programming already teaches that insufficient state summaries can destroy optimal substructure.

RGΦ does not claim that principle as new.

Potential contribution: an exact arithmetic system in which the failure can be exhibited, quantified, and related to number-theoretic hidden coordinates.

### 2.6 Open systems and traps

Finite invariant sets, holes, survivor sets, repellers, and trapping are well established.

Potential contribution: exact modular trap families produced by the interaction of radix cycles and Möbius coupling, with Bellman implications.

### 2.7 Multiplicative order and Artin-type questions

Primitive-root and index-map literatures are mature and technically deep.

The separate RGΦ arithmetic-density line should be framed as an Artin-type specialization unless a genuinely new theorem is proved.

### 2.8 Computer-assisted mathematics

Exhaustive reachability, independent checkers, proof certificates, hashes, and reproducible workflows have substantial precedent.

Potential contribution: a domain-specific exact certificate architecture, not the generic idea of certification itself.

## 3. Claim-to-prior-art discipline

The machine-readable file claim-to-literature-map.csv is the operational map.

For each headline claim, the submission should identify:

- nearest known mathematical object;
- nearest known theorem;
- what changes in RGΦ;
- whether the difference is structural or merely notational;
- priority risk;
- evidence required before using “new”, “first”, or “novel”.

## 4. Current novelty ranking

### Strongest current claim

**Robust nonnested extremal targets in the benchmark semigroup.**

Why it is strong:

- exact;
- finite but nontrivial;
- parameter-robust;
- directly connected to a clean dynamical question;
- does not depend on speculative hidden-state language.

### Highest-ceiling future claim

**General hidden Farey/\(p\)-adic control theorem.**

Why it has high ceiling:

- connects several mature areas in a specific control problem;
- could explain the failure of visible-state Bellman summaries;
- may yield a minimal state-augmentation theorem.

Risk: high prior-art sensitivity.

### Highest-ceiling structural program

**Infinite-family modular trap and basin theorem.**

Why it has high ceiling:

- replaces brute-force non-reachability by arithmetic structure;
- may generalize across bases;
- naturally connects multiplicative order, SCC structure, and extremal escape.

## 5. Current-frontier review

Recent work in Farey/projective IFS, first-return systems, rational orbit statistics, natural extensions, generalized continued fractions, and open expanding systems increases the burden of comparison.

The current-frontier document records this literature separately so that the manuscript can be updated without rewriting the conceptual audit.

## 6. Search methodology

The audit uses:

- arXiv;
- Crossref and publisher pages;
- zbMATH Open where available;
- Google Scholar / OpenAlex / Semantic Scholar for citation chaining;
- official journal pages.

Before submission, add:

- MathSciNet;
- full zbMATH citation graph;
- Scopus/Web of Science if available institutionally;
- dissertations and proceedings for niche priority questions.

## 7. Referee-facing novelty language

Recommended:

> “We introduce and analyze the following rational radix–Möbius system and prove robust nonnesting for its benchmark extremal targets.”

Recommended when comparison is incomplete:

> “We are not aware of an identical theorem in the nearby radix/Farey literature; the relationship to natural extensions and projective systems is discussed explicitly.”

Avoid:

- “unprecedented”;
- “first ever”;
- “new mathematical paradigm”;
- claims that the component techniques themselves are novel.

## 8. Priority status

\[
\boxed{\text{priority assessment: promising but not closed}}
\]

The repository treats this as a scientific risk to manage, not a marketing problem to hide.
