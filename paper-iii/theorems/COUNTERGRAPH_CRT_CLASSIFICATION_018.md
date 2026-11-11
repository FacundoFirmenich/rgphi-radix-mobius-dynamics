# RGΦ Round 018-B — complete CRT classification of the realized five-state graph

Consider the action graph
\[
T=(0)(1\ 2)(3\ 4),
\qquad
S=(0\ 1)(2\ 4),\quad3\mapsto1,
\]
where \(3\mapsto1\) is the unique strict \(S\)-edge of factor three.

## State normal form

Every primitive high realization has uniquely determined fibre variables
\[
\begin{aligned}
x_0&=A/Q_0,&x_1&=A/Q_1,&x_2&=C/Q_1,\\
x_3&=3A/D,&x_4&=C/D.
\end{aligned}
\]
The strict-edge predecessor shift gives
\[
D=3Q_0+kA,\qquad |k|<3,\quad k\ne0.
\]
Since \(D<2C<2Q_1<4A\), positive \(k\) is impossible.  Therefore
\[
\boxed{D=3Q_0-\varepsilon A,\qquad\varepsilon\in\{1,2\}.}
\]

## Necessary and sufficient involution conditions

Besides highness, reducedness and pairwise state distinctness, require
\[
\begin{aligned}
Q_1&\mid C^2-A^2,\\
D&\mid C^2-9A^2,\\
A&\mid(Q_1-A)^2-(Q_0-A)^2,\\
C&\mid(D-C)^2-(Q_1-C)^2.
\end{aligned}
\]
Define the unit residues
\[
\begin{aligned}
r_{Q_0}&=1,\\
r_{Q_1}&\equiv CA^{-1}\pmod{Q_1},\\
r_D&\equiv C(3A)^{-1}\pmod D,\\
r_A&\equiv(Q_1-A)(Q_0-A)^{-1}\pmod A,\\
r_C&\equiv(D-C)(Q_1-C)^{-1}\pmod C.
\end{aligned}
\]
Then the graph is realized exactly iff the generalized CRT system
\[
\boxed{
B\equiv0\pmod3,
\ B\equiv r_{Q_0}\pmod{Q_0},
\ B\equiv r_{Q_1}\pmod{Q_1},
\ B\equiv r_D\pmod D,
\ B\equiv r_A\pmod A,
\ B\equiv r_C\pmod C
}
\]
is compatible.

The reverse edges follow from the four square-divisibility conditions.  The strict edge follows automatically: because \(3\nmid A\), write \(B=3b\) modulo \(A\); then
\[
D-3A\equiv3(Q_0-A)\pmod A
\]
and the ordinary edge \(S(x_0)=x_1\) yields
\[
b(D-3A)\equiv Q_1-A\pmod A.
\]

## Base-side completeness

If compatible, every realizing base belongs to one and only one class
\[
\boxed{B\equiv B_*\pmod L},
\qquad
L=\operatorname{lcm}(3,A,C,Q_0,Q_1,D).
\]
Thus the base-side classification of a fixed primitive state tuple is complete.

## The Round-017 tuple

For
\[
(A,C,Q_0,Q_1,D)=(406,712,557,731,1265),
\qquad\varepsilon=1,
\]
the residues are
\[
(0,1,171,254,349,179)
\]
modulo \((3,557,731,1265,406,712)\), giving
\[
B\equiv88\,011\,536\,665\,779
\pmod{223\,336\,848\,698\,040}.
\]
The labelled action graph has trivial automorphism group and is not isomorphic to itself under generator exchange.

## State-side boundary

An exact search of both \(\varepsilon=1,2\) branches with \(Q_1\le10,000\) and \(D\le30,000\) found only the Round-017 tuple.  This is finite evidence of small-height isolation, not a proof that no second primitive tuple exists.
