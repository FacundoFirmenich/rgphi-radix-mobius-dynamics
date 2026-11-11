# OR-4 — six-state hexagonal / dual-triad test

This is a preregistered prospective test. It must be applied without changing its definitions after the next exact six-state results are known.

## Object under test

The lexicographically minimal canonical isomorphism class of an exact all-high nonpermutation six-state SCC discovered after the preregistration commit.

## Primary endpoint — DUAL_TRIAD

A hit occurs iff there is a partition `A union B` with `|A|=|B|=3` and a choice `(G,H)` from `(T,S)` such that:

- `G` acts as a 3-cycle on `A`;
- `G` acts as a 3-cycle on `B`;
- `H(A)=B` and `H(B)=A` bijectively.

## Secondary endpoint — ALTERNATING_HEXAGON

A hit occurs iff the labelled graph contains a Hamiltonian cycle with labels alternating exactly `T,S,T,S,T,S`.

## Anti-flexibility rules

- No geometric drawing counts unless the exact graph signature is present.
- No `2+4`, `1+5`, approximate hexagon or visually suggestive embedding counts.
- The three previously tested six-state lift architectures are historical negative evidence, not prospective tests of these signatures.
- If the first complete declared six-state jurisdiction has no hit, the hypothesis is weakened and the null result is retained.
