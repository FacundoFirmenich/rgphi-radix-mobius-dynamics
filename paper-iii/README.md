# RGΦ Paper III — finite modular traps, universal basins and closure rigidity

**Canonical status:** `ACTIVE_RESEARCH / PREPRINT_NOT_FROZEN`  
**Current theorem stack:** `v1.4 integrated`  
**Current frontier:** `Five-State Closure 014`  
**Last synchronized:** 2026-11-10

This directory is the canonical in-repository home of **Paper III only**. It does not modify the authority or status of Paper I, Paper II, Stage B2, HDH, ODT or other isolated research lines.

## System

For an integer base `B >= 2`,

\[
T_B(x)=\{Bx\},\qquad H(x)=\frac1{1+x},\qquad S_B=H\circ T_B\circ H^{-1},
\]

with `S_B` admissible on the high domain `[1/2,1]`.

## Closed theorem stack

- complete binary closed-SCC classification;
- complete ternary closed-SCC classification;
- all-low SCC classification at arbitrary finite cardinality by primitive necklaces;
- exactly-one-high classification at arbitrary finite cardinality;
- exact universal-predecessor divisor calculus;
- canonical and maximal universal-basin results;
- arbitrary high predecessor depth as the base varies;
- fixed-base finiteness by reduction to a binary S-unit equation;
- explicit, non-sharp fixed-base bounds;
- directed-diameter-at-most-two rigidity;
- cycle reduction budget and least-prime obstruction;
- all-high permutation rigidity for cardinalities 2, 3 and 4.

## Open frontier

The first unresolved all-high nonpermutation cardinality is five. A minimal counterexample, if one exists, must occur over a base divisible by 2 or 3 and contain a strict factor-2 or factor-3 edge on a simple cycle of length four or five.

The binding gate is [`gates/RGPHI_FIVE_STATE_CLOSURE_014_REVISED.md`](gates/RGPHI_FIVE_STATE_CLOSURE_014_REVISED.md).

## Evidence boundary

- `SYMBOLIC_EXACT`: algebraic theorem/proof;
- `SYMBOLIC_PLUS_FINITE_CERTIFICATE`: symbolic reduction plus complete finite certificate;
- `FINITE_EXHAUSTIVE`: complete finite jurisdiction only;
- `OPEN`: not promoted.

Global all-high permutation rigidity remains `OPEN` for cardinality at least five.

## Reviewer object

The standalone explanatory report for mathematical review is under `reviewer/`. It is scoped exclusively to Paper III.
