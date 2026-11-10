# RGΦ Paper III — finite modular traps, universal basins and closure rigidity

**Canonical status:** `ACTIVE_RESEARCH / PREPRINT_NOT_FROZEN`  
**Current theorem stack:** `v1.6`  
**Current frontier:** `Five-State Normal-Form Elimination 016`  
**Last synchronized:** 2026-11-11

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
- fixed-base high finiteness and explicit non-sharp bounds;
- directed-diameter-at-most-two rigidity;
- cycle reduction budget and least-prime obstruction;
- all-high permutation rigidity for cardinalities 2, 3 and 4;
- impossibility of five-state Hamiltonian `TTSSS`;
- impossibility of repairing a strict `TTSS` core by a fifth state;
- exact fibre-closure adjudication of the 560 remaining architecture classes;
- exact quotient to 24 factor-specific classes and 12 structural Diophantine normal forms.

## Five-state frontier

The five-state gate remains `OPEN_PARTIAL`.

The previous 560 canonical architecture classes have been adjudicated exactly:

- state collision: 432;
- strict-fibre conflict: 60;
- unreduced-fibre injectivity conflict: 34;
- additional cycle-budget conflict: 10;
- exact survivors: 24.

The 24 survivors pair by strict factor `2/3` and define exactly **12** structural Diophantine normal forms.

The binding gate is [`gates/RGPHI_FIVE_STATE_NORMAL_FORM_ELIMINATION_016.md`](gates/RGPHI_FIVE_STATE_NORMAL_FORM_ELIMINATION_016.md).

## Evidence boundary

- `SYMBOLIC_EXACT`: algebraic theorem/proof;
- `SYMBOLIC_PLUS_FINITE_CERTIFICATE`: symbolic reduction plus complete finite certificate;
- `FINITE_EXHAUSTIVE`: complete finite jurisdiction only;
- `OPEN_PARTIAL`: exact partial closure with unresolved certified forms;
- `OPEN`: not promoted.

Global all-high permutation rigidity remains `OPEN` for cardinality at least five.
