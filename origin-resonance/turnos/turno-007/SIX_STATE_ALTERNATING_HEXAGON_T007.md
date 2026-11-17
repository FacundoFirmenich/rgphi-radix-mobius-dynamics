# Six-state high-defect reduction to the alternating hexagon

Assume a six-state all-high component has one marked strict `T` edge of factor `d in {4,5,6,7}` on a Hamiltonian balanced cycle. The cycle budget forces every alternative edge from vertex `i>0` to return into `{1,...,i}`.

There are 720 marked skeletons for each balanced word

\[
TTTSSS,\qquad TTSTSS,\qquad TSTSTS.
\]

Imposing the defect-one lollipop conditions leaves one functional map per word:

| word | T | S |
|---|---|---|
| TTTSSS | `(1,2,3,1,4,5)` | `(3,1,2,4,5,0)` |
| TTSTSS | `(1,2,1,4,3,5)` | `(4,1,3,2,5,0)` |
| TSTSTS | `(1,1,3,2,5,4)` | `(5,2,1,4,3,0)` |

`TTTSSS` is impossible: highness of the strict source forces a shared numerator `P>2Q`, whereas another state is `P/Q<1`.

`TTSTSS` is impossible: the strict source gives `P>2Q`; a second high fibre forces `C>Q`, while another state requires `C/Q<1`.

Therefore every realizable component in this declared high-defect lollipop jurisdiction must use

\[
\boxed{TSTSTS}.
\]

This is a prospective structural confirmation of `ALTERNATING_HEXAGON` in the declared jurisdiction. `DUAL_TRIAD` remains impossible there.

The surviving fibre normal form is

\[
\frac{P}{dQ},\quad\frac{A}{Q},\quad\frac{A}{D},\quad\frac{C}{D},\quad\frac{C}{E},\quad\frac{P}{E},
\]

with

\[
P=dA+kQ,\qquad0<|k|<d/2,
\]

and cycle divisibilities

\[
A\mid D^2-Q^2,\ D\mid C^2-A^2,\ C\mid E^2-D^2,\ E\mid P^2-C^2,\ P\mid E^2-d^2Q^2.
\]

An exact audit for `Q<=500` found no candidate reaching CRT compatibility. This is finite negative evidence only.
