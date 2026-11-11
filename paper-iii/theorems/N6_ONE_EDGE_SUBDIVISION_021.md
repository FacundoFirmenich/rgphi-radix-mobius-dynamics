# RGΦ Round 021-E — complete one-edge-subdivision catalogue at cardinality six

Start from the exact five-state graph
\[
T=(0)(1\ 2)(3\ 4),
\]
\[
S=(0\ 1)(2\ 4),\qquad3\xrightarrow{S_3}1.
\]
A one-edge-subdivision extension introduces vertex 5, replaces one old generator edge \(i\to j\) by \(i\to5\to j\), and assigns the other generator at 5 arbitrarily. If the subdivided edge is strict, factor three may lie on either new segment.

## Complete universe

Nine non-strict edges give \(9\cdot6=54\) profiles; the strict edge gives \(1\cdot6\cdot2=12\). Hence exactly
\[
\boxed{66}
\]
labelled profiles form this extension class.

## Exact adjudication

| status | profiles |
|---|---:|
| state collision | 25 |
| forbidden mixed two-cycle | 11 |
| high-domain Farkas infeasibility | 10 |
| fibre-injectivity violation | 5 |
| cycle-budget violation | 5 |
| structural survivors | 10 |

The ten infeasible profiles carry exact rational Farkas certificates.

Every survivor fixes the new vertex under the generator not being subdivided: five T-edge subdivisions with \(S(5)=5\), four non-strict S-edge subdivisions with \(T(5)=5\), and one strict-S subdivision with \(T(5)=5\) and factor three on \(5\to1\).

## Fixed-tuple extension theorem

Keeping the five Round-017 rational states unchanged, the forced fibres allow exactly 3,206 high reduced candidates for state 5 across the ten survivors. The universal CRT test rejects all 3,206.

Therefore the known five-state tuple admits no realization in any one-edge-subdivision extension.

## Boundary

This exhausts one declared six-state extension class. It does not classify all six-state SCCs.
