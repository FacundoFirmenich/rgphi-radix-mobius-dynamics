# T006-D — complete marked high-defect skeletons in six states

Assume a six-state all-high SCC contains a marked strict edge of defect
\[
d\in\{4,5,6,7\}.
\]
Every simple cycle containing it is Hamiltonian and balanced, with three `T` and three `S` edges.

Normalize the marked cycle as
\[
v_0\to v_1\to v_2\to v_3\to v_4\to v_5\to v_0,
\]
where `v_0->v_1` is strict.

## Back-edge normal form

For `1<=i<=5`, the alternate edge at `v_i` must point into
\[
\{v_1,\ldots,v_i\}.
\]
The alternate edge at `v_0` is arbitrary.

A forward jump creates a shorter strict cycle; an alternate edge to the cycle successor changes the balanced `3+3` word into a forbidden `4+2` word. These are the only exclusions.

## Exact count

For one balanced word and one marked source, the numbers of choices are
\[
1\cdot2\cdot3\cdot4\cdot5\cdot6=720.
\]
The three balanced necklaces are
\[
TTTSSS,\qquad TTSTSS,\qquad TSTSTS.
\]
Therefore there are
\[
\boxed{2160}
\]
normalized marked skeletons and, after decorating the marked edge by `4,5,6,7`,
\[
\boxed{8640}
\]
normalized marked defect profiles. Restoring the six rotations gives `51,840` raw marked profiles.

## Preregistered signatures

Every profile has directed distance five from the strict target to the source. A DUAL_TRIAD graph has diameter at most three, hence
\[
\boxed{\text{DUAL_TRIAD is impossible in this high-defect jurisdiction}.}
\]

The Hamiltonian vertex order is forced. Thus
\[
\boxed{\text{ALTERNATING_HEXAGON occurs iff the word is }TSTSTS.}
\]
Exactly `720` of the `2160` normalized skeletons carry that signature.

This classifies the marked combinatorial skeletons; arithmetic realization remains open.
