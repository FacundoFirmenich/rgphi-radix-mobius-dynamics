# RGΦ Round 017 — exact cubic reduction of `DF015-0015`

Within the conditional defect-one Round-015/016 jurisdiction, the remaining secondary branch `DF015-0015` has maps
\[
T=(0,0,2,4,3),\qquad S=(2,3,4,1,0),
\]
with the unique strict edge \(1\xrightarrow{T_3}0\).

Every realization has the normal form
\[
\begin{aligned}
x_0&=\frac{A}{A+z},&
x_1&=\frac{2A-z}{3(A+z)},&
x_2&=\frac{A}{A+y},\\
x_3&=\frac{2A-z}{2A-w},&
x_4&=\frac{A}{2A-w},
\end{aligned}
\]
with
\[
A>5z>w>0,\qquad0<y<A.
\]

The two \(T\)-cycle conditions and the two \(S\)-cycles imply
\[
2A-w\mid(2A-z)^2-A^2,
\]
\[
2A-z\mid(A+4z)^2-(z-w)^2,
\]
\[
A\mid y^2+wz,
\qquad
A\mid yw+z^2.
\]
Since \(\gcd(A,wz)=1\), the last two congruences give
\[
\boxed{A\mid z^3+w^3.}
\]

Let
\[
k=\frac{(2A-z)^2-A^2}{2A-w}.
\]
Modulo \(A\), the defining identity gives
\[
kw\equiv-z^2\pmod A.
\]
The \(S\)-cycle gives the same congruence with \(y\) in place of \(k\), hence
\[
y\equiv k\pmod A.
\]
The interval \(A>5z>w>0\) implies
\[
A<k<2A.
\]
Since \(0<y<A\), necessarily
\[
\boxed{y=k-A.}
\]

Thus the five-state form is reduced to the three positive integer variables
\[
\boxed{(A,z,w)}
\]
subject to the displayed divisibilities, coprimality, and high-domain inequalities.  Once \((A,z,w)\) is fixed, \(y\) is forced.

A direct exact search through \(A\le5000\), using the complete radix/CRT edge equations, tested 17,747,136 admissible candidates and found no realization. This is a finite audit only and does not prove global impossibility.

`DF015-0015` therefore remains `OPEN_REDUCED_CONDITIONAL`.  This does not adjudicate multi-strict-edge five-state SCCs outside the defect-one jurisdiction.