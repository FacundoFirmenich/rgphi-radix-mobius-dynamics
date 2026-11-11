# RGΦ Round 018-C — divisor reduction for `DF015-0015`

The secondary strict-\(T\), factor-three form remains
\[
A>5z>w>0,
\]
with
\[
C=2A-z,\qquad D=2A-w,
\]
and necessary conditions
\[
D\mid C^2-A^2,
\qquad
C\mid(A+4z)^2-(z-w)^2,
\qquad
A\mid z^3+w^3.
\]
Put
\[
\delta=z-w\in(0,z).
\]

## Factorized divisor constraints

The exact identities
\[
4(C^2-A^2)=(6A+3w-8z)D+(3\delta-z)(\delta+z)
\]
and
\[
4\big((A+4z)^2-(z-w)^2\big)
=(2A+17z)C+(9z-2\delta)(9z+2\delta)
\]
give the necessary conditions
\[
\boxed{D\mid(3\delta-z)(\delta+z)},
\]
\[
\boxed{C\mid(9z-2\delta)(9z+2\delta)}.
\]
Since \(A>5z\), both \(C,D>9z\).  Therefore the associated quotients satisfy
\[
\left|\frac{(3\delta-z)(\delta+z)}D\right|<\frac{4z}{9},
\qquad
0<\frac{(9z-2\delta)(9z+2\delta)}C<9z.
\]
This converts the remaining search from an \(A\)-scan into a divisor problem controlled by \((z,w)\).

## Exceptional zero-remainder branch

If
\[
(3\delta-z)(\delta+z)=0,
\]
then \(\delta=z/3\), so \(z=3h,w=2h\).  The cubic divisibility and \(\gcd(A,z)=1\) imply
\[
A\mid35.
\]
Together with \(A>15h\) and integrality of the quotient, the only candidate is
\[
(A,z,w,y)=(35,3,2,13).
\]
For it
\[
C=67,
\qquad
(A+4z)^2-(z-w)^2=2208\not\equiv0\pmod{67}.
\]
Hence the zero-remainder branch is globally impossible.

## Expanded exact audit

For every
\[
1\le w<z\le3000,
\]
all divisors \(A>5z\) of \(z^3+w^3\) were enumerated.  This covers \(A\) values as large as
\[
53\,973\,008\,999,
\]
not merely a bounded interval \(A\le N\).

The audit examined 213,800,681 admissible divisor candidates.  Exactly 587 passed the first cycle divisibility and forced-\(y\) test; none passed the second \(C\)-cycle divisibility.

This remains finite evidence in \(z\), not a global no-go.  `DF015-0015` remains open, but its exceptional branch is closed and the nonexceptional branch is reduced to two factorized divisor quotients.
