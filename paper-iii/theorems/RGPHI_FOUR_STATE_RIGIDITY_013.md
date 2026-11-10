# RGΦ Four-State Closure Rigidity 013

Let \(F\subset\mathbb Q\cap(1/2,1)\) be a closed strongly connected component of cardinality four for
\[
T_B(x)=\{Bx\},\qquad S_B=H\circ T_B\circ H^{-1},\qquad H(x)=\frac1{1+x}.
\]
Round 012 proves that if either restricted generator is nonpermutational, then there is a Hamiltonian four-cycle with exactly two T-edges, two S-edges, total reduction product \(r\in\{2,3\}\), and all other cycle edges unreduced. Up to cyclic rotation, the word is `TTSS` or `TSTS`.

## Theorem 013-A — `TTSS` is impossible

If the strict edge is a T-edge, the other T-edge is unreduced and the two S-edges preserve numerator. Two opposite states have the same numerator and denominators differing by \(r\), hence \(x_2=r x_0>1\). The strict-S case is dual. Therefore no all-high closed SCC contains a strict Hamiltonian `TTSS` cycle.

## Theorem 013-B — `TSTS` with strict T reduction is impossible

Orient
\[
x_0\xrightarrow{T_r}x_1\xrightarrow Sx_2\xrightarrow Tx_3\xrightarrow Sx_0.
\]
The unreduced edges give
\[
x_0=\frac{C}{rQ},\quad x_1=\frac{A}{Q},\quad x_2=\frac{A}{D},\quad x_3=\frac{C}{D}.
\]
Closure forces
\[
S:(x_0\ x_3)(x_1\ x_2),\qquad T:x_1\text{ fixed},\ (x_2\ x_3).
\]
The strict congruence excludes \(r=2\) and gives \(r=3\), \(Q=A+u\), \(C=2A-u\), with the high condition \(A>5u\). Writing \(D=2A-t\), \(0<t<u\), the forced two-cycles imply
\[
A\mid u^2-t^2,\qquad D\mid A^2-(u-t)^2.
\]
The quotient congruences yield \(A=4u-3t-k<4u\), contradicting \(A>5u\).

## Theorem 013-C — `TSTS` with strict S reduction is impossible

Orient
\[
x_0\xrightarrow{S_r}x_1\xrightarrow Tx_2\xrightarrow Sx_3\xrightarrow Tx_0.
\]
Closure forces three two-cycles and one fixed point. The resulting divisibilities reduce to the cases \(r=2\) and \(r=3\). The \(r=2\) branch yields the conic
\[
5P^2+4Pd-41d^2=0
\]
with nonsquare discriminant \(4\cdot209d^2\). The \(r=3\) branches reduce either to an immediate coprimality contradiction or, in the exceptional gcd-19 branch, to
\[
1197p^2-(80j+1520)pc+(j^2+38j+323)c^2=0,\qquad1\le j\le37.
\]
Its discriminant contains
\[
403j^2+15314j+190969,
\]
which is never a square for \(1\le j\le37\); the complete modular certificate uses moduli 68, 55 and 71.

## Corollary 013-D — four-state all-high rigidity

Every four-state all-high closed SCC satisfies
\[
\boxed{T_B|_F\text{ and }S_B|_F\text{ are permutations}.}
\]

## Evidence boundary

This theorem closes cardinality four only. Any minimal nonpermutation counterexample has at least five states and, by the cycle budget, occurs over a base divisible by 2 or 3.
