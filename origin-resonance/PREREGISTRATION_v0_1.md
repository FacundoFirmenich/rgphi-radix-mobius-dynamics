# Origin–Resonance preregistration v0.1

Timestamp: 2026-11-11  
Base canonical commit: `700fa58e7420ddbf3a53003eccd56a64524a50cf`

## OR-1 — sharpness of the `4/9` bound

For

\[
a=A/z>5,\qquad t=w/z\in(0,1),
\]

and

\[
\frac hz=\frac{(2-3t)(2-t)}{2a-t},
\]

determine the exact supremum of `|h|/z` over the continuous chamber.

Decision rule:

- `4/9` structural iff the exact supremum is `4/9`;
- otherwise mark it `PROOF_BOUND_ARTIFACT` and retain the exact supremum.

## OR-2 — sharpness of the index 19

Determine the exact continuous supremum of

\[
\frac{L}{A},\qquad L=j-h+5w+85z,
\]

under the same chamber, where

\[
\frac jz=\frac{(7+2t)(11-2t)}{2a-1}.
\]

Then decide separately:

1. whether `n<=19` survives sharpening;
2. whether `F_19=0` has a real point in the strict chamber;
3. whether it has rational/integral admissible points.

## OR-3 — independence of `17/19` and the nineteen curves

Construct a dependency DAG from the current Paper III formula chain. The historical benchmark `17/19` counts as an independent recurrence only if no formal edge reaches the derivation of `n in {1,...,19}`.

Absence of a formal edge gives `CURRENT_FORMAL_INDEPENDENCE` only. Historical independence requires a broader archive audit.

## OR-4 — preregistered six-state signature

This test applies to the lexicographically minimal canonical isomorphism class of an exact all-high nonpermutation six-state SCC obtained after this preregistration.

Canonical encoding:

`(T(0),...,T(5),S(0),...,S(5),strict_T_mask,strict_S_mask)`, minimized over all vertex relabelings and the duality `T <-> S`.

### Primary signature: DUAL_TRIAD

There exists a partition into two three-state blocks `A,B` and an ordering of the generators `(G,H)` such that:

1. `G|A` and `G|B` are both 3-cycles;
2. `H` maps `A` bijectively onto `B` and `B` bijectively onto `A`.

### Secondary signature: ALTERNATING_HEXAGON

The labelled action graph contains a Hamiltonian six-cycle whose labels strictly alternate `T,S,T,S,T,S`.

No geometric drawing, approximate hexagon, `2+4` partition or post-hoc proxy counts.

## OR-5 — five as a universal defect cell

### Primary hypothesis: SHORT_DEFECT_CYCLE

Every minimal finite all-high nonpermutation SCC contains a simple directed cycle of length at most five with exactly one strict edge and all remaining cycle edges unreduced.

### Secondary hypothesis: FIVE_STATE_DEFECT_QUOTIENT

After quotienting maximal unreduced numerator/denominator fibre cycles, the minimal defect quotient has exactly five vertices and is isomorphic to one of the twenty canonical five-state forms.

## Hyperaccess boundary

Ratios in `(0,1)` may motivate a future access functional, but no ratio in this branch is called hyperaccess unless an explicit map with an operational invariance or monotonicity theorem is supplied.
