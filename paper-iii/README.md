# RGΦ Paper III — finite modular traps, universal basins and closure rigidity

**Canonical status:** `ACTIVE_RESEARCH / PREPRINT_NOT_FROZEN`  
**Current theorem stack:** `v1.5`  
**Current frontier:** `Five-State Diophantine Quotient 015`  
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
- all-high permutation rigidity for cardinalities 2, 3 and 4;
- impossibility of five-state Hamiltonian `TTSSS`;
- impossibility of repairing a strict `TTSS` core by a fifth state.

## Five-state frontier

The five-state gate is `OPEN_PARTIAL`.

The remaining exhaustive architecture classes are:

- Hamiltonian `TSTSS`: 228 canonical classes;
- strict `TSTS` core plus fifth closure state: 332 canonical classes.

The binding gate is [`gates/RGPHI_FIVE_STATE_DIOPHANTINE_QUOTIENT_015.md`](gates/RGPHI_FIVE_STATE_DIOPHANTINE_QUOTIENT_015.md). It must reduce the 560 canonical classes to exact Diophantine normal forms and eliminate or realize every form.

## Evidence boundary

- `SYMBOLIC_EXACT`: algebraic theorem/proof;
- `SYMBOLIC_PLUS_FINITE_CERTIFICATE`: symbolic reduction plus complete finite certificate;
- `FINITE_EXHAUSTIVE`: complete finite jurisdiction only;
- `OPEN_PARTIAL`: exact partial closure with unresolved certified classes;
- `OPEN`: not promoted.

Global all-high permutation rigidity remains `OPEN` for cardinality at least five.

## Reviewer object

The standalone explanatory report for mathematical review is under `reviewer/`. It is scoped exclusively to Paper III.
