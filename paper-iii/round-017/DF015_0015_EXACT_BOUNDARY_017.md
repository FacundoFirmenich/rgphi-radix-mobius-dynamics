# RGΦ Round 017 — secondary front: exact boundary for `DF015-0015`

The five-state threshold is already resolved by the strict-`S` counterfamily,
but the remaining strict-`T`, factor-three form `DF015-0015` is retained as
an independent arithmetic question.

## Exact normal form

Write
\[
x_0=\frac A Q,\quad
x_1=\frac C Q,\quad
x_2=\frac C{3D},\quad
x_3=\frac A D,\quad
x_4=\frac A E.
\]
The maps are
\[
T:(x_0\ x_1),\qquad x_2\mapsto x_3,\qquad T(x_3)=x_3,\quad T(x_4)=x_4,
\]
and
\[
S:(x_0\ x_3\ x_4),\qquad (x_1\ x_2).
\]

The predecessor-shift theorem gives
\[
C=3A-D.
\]
Put
\[
D=A+z,\qquad C=2A-z.
\]
Highness of the strict source yields
\[
\boxed{A>5z.}
\]
Since \(C<Q<2A\), write
\[
Q=2A-w,\qquad0<w<z,
\]
and put
\[
h=z-w.
\]

Three necessary divisibilities follow:
\[
Q\mid C^2-A^2,
\]
\[
C\mid(A+4z)^2-h^2,
\]
\[
A\mid z^3+w^3.
\]

The first two imply the relaxed necessary conditions
\[
Q\mid(3h-z)(h+z),
\]
\[
C\mid81z^2-4h^2.
\]
Moreover
\[
Q>9z,\qquad C>9z.
\]

## Symbolic exclusion of the zero-factor subcase

If
\[
3h-z=0,
\]
then
\[
z=3u,\qquad w=2u.
\]
The cubic closure becomes
\[
A\mid35u^3.
\]
Reducedness gives \(\gcd(A,u)=1\), hence \(A\mid35\). But \(A>15u\), so
only \(u=1,2\) and \(A=35\) can remain.

For \(u=1\),
\[
C=67,\qquad81z^2-4h^2=725,
\]
and \(67\nmid725\).

For \(u=2\),
\[
C=64,\qquad81z^2-4h^2=2900,
\]
and \(64\nmid2900\).

Therefore the subcase \(3h=z\) is globally impossible.

## Finite exhaustive necessary-condition audit

For
\[
2\le z\le5000,\qquad1\le h<z,\qquad3h\ne z,
\]
the supplied C++ checker enumerates every divisor
\[
C>9z
\]
of
\[
(9z-2h)(9z+2h),
\]
recovers
\[
A=(C+z)/2,\qquad Q=C+h,
\]
and applies:

- parity and \(A>5z\);
- \(Q\mid(3h-z)(h+z)\);
- all primitive gcd conditions;
- \(A\mid z^3+(z-h)^3\).

Results:
\[
48\,518
\]
relaxed divisor-core candidates,
\[
682
\]
primitive candidates, and
\[
\boxed{0}
\]
candidates satisfying the cubic closure.

This is a complete finite audit of the declared \(z\)-jurisdiction, not a
global proof. Thus `DF015-0015` remains open.

## Evidence boundary

- zero-factor subcase: `CLOSED_SYMBOLIC`;
- \(z\le5000\) nonzero-factor jurisdiction: `FINITE_EXHAUSTIVE`;
- global `DF015-0015`: `OPEN`.
