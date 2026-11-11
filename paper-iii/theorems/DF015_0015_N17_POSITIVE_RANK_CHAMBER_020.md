# RGΦ Round 020-B — a positive-rank chamber component for n=17

The Round-019 cubic \(F_{17}=0\) contains the primitive integral point

\[
\boxed{P=[64233:11741:1138]}.
\]

Exact checks give

\[
F_{17}(64233,11741,1138)=0,
\qquad
64233>5\cdot11741>1138>0,
\]

and

\[
\frac{11741^3+1138^3}{64233}=25220421.
\]

Put

\[
C=2A-z=116725,
\qquad
D=2A-w=127328.
\]

Then

\[
\gcd(C,D)=23,
\]

while

\[
\frac{(2z-3w)(2z-w)}D=\frac{80997}{23},
\qquad
\frac{(7z+2w)(11z-2w)}C=\frac{2111575}{23}.
\]

Thus P is a certified near realization: the cubic equation, strict chamber and cubic divisibility hold, but both cycle divisibilities fail by the same exact factor 23.

Let \(O=[0:1:-1]\) be the rational origin. Exact projective enumeration gives smooth reductions

\[
\#F_{17}(\mathbb F_7)=10,
\quad
\#F_{17}(\mathbb F_{11})=14,
\quad
\#F_{17}(\mathbb F_{13})=18,
\quad
\#F_{17}(\mathbb F_{17})=23.
\]

The reduction bounds exclude every possible prime divisor of rational torsion, so

\[
F_{17}(\mathbb Q)_{\rm tors}=0.
\]

Since \(P\ne O\), P has infinite order and

\[
\boxed{\operatorname{rank}F_{17}(\mathbb Q)\ge1}.
\]

The real points form a compact one-dimensional Lie group. The closure of a non-torsion cyclic subgroup contains a real circle component. Because \(A>5z>w>0\) is open and contains P, infinitely many rational multiples return to the chamber. Therefore

\[
\boxed{F_{17}=0\text{ contains infinitely many rational points in }A>5z>w>0.}
\]

Consequently real/chamber geometry cannot eliminate `DF015-0015`; the decisive filters are arithmetic, especially coprimality and the cubic divisibility.
