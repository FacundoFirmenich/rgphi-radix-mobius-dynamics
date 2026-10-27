# Evidence model and claim discipline

RGΦ is a mixed symbolic/computational research program. The repository therefore uses an explicit evidence taxonomy.

## S — Symbolic theorem

A statement derived algebraically from declared hypotheses.

Required artifacts:

- precise theorem statement;
- proof or derivation;
- exact regression test when machine-checkable.

Examples:

- branch determinant equals \(B\);
- seed-family conjugacy identity;
- radix denominator law.

## F — Finite exhaustive theorem

A statement proved by complete enumeration of a finite state space.

Required artifacts:

- exact transition rules;
- exact target predicate;
- finite search boundary;
- complete enumeration;
- deterministic summary counts;
- machine-readable evidence.

Examples:

- \(\tau_1,\ldots,\tau_4\) for the benchmark;
- threshold robustness intervals derived from complete layers;
- denominator-\(\le500\) trap atlas counts.

## C — Large computer-assisted certificate

A statement whose proof depends on a large exact computation.

Required artifacts whenever feasible:

- exact integer/rational implementation;
- mathematically justified pruning only;
- target test before pruning;
- canonical state encoding;
- independent engine or independent checkpoint verification;
- checksums or frontier hashes;
- explicit resource/search horizon.

Examples:

- depth-five lower/upper bounds;
- long Bellman branch closures.

## O — Open statement

A conjecture, incomplete bound, programmatic hypothesis, or unproved generalization.

Examples:

- exact value of \(\tau_5\);
- all-denominator trap classification;
- global orthomodular structure;
- asymptotic law for \(\tau_m\).

## Status transitions

A claim may move only through an evidence-producing transition, for example:

\[
O\rightarrow F,\qquad O\rightarrow S,\qquad C\rightarrow S.
\]

A stronger numerical experiment does not convert an open statement into a theorem.

## Negative and superseded results

Negative results are preserved because they constrain theory development.

Superseded results remain in the history when mathematically valid. The repository distinguishes:

- **false/refuted**;
- **locally valid but globally superseded**;
- **open**;
- **closed**.

## Floating-point policy

Floating-point quantities may be used for plotting or readability only.

Reachability, equality, reduction, target membership, and theorem-critical comparisons use integers or exact rationals.

## Literature claims

“Novel” is never used to mean that every ingredient is new.

The repository separates:

1. established ingredients;
2. a possibly new coupling or theorem;
3. computational evidence;
4. priority risk still requiring specialist review.

The literature audit is therefore part of the evidence model rather than promotional material.
