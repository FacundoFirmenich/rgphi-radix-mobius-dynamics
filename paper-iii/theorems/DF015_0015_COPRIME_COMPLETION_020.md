# RGΦ Round 020-A — coprime-completion theorem on the elliptic cubics

For `DF015-0015`, put

\[
C=2A-z,\qquad D=2A-w,
\]

\[
f=(2z-3w)(2z-w),\qquad g=(7z+2w)(11z-2w).
\]

Round 019 introduced, for \(n=1,\ldots,19\), the plane cubic

\[
\begin{aligned}
F_n(A,z,w)={}&4nA^3-2nA^2(w+z)+nAwz\\
&-20A^2w-340A^2z+24Aw^2+148Awz+24Az^2\\
&-4(z^3+w^3).
\end{aligned}
\]

## Exact identity

Direct expansion gives

\[
\boxed{gD-fC+(5w+85z-nA)CD=-F_n(A,z,w).}
\]

## Theorem 020-A

If \(F_n(A,z,w)=0\) and \(\gcd(C,D)=1\), then

\[
\boxed{C\mid g},\qquad \boxed{D\mid f}.
\]

Indeed, modulo \(C\) the identity gives \(gD\equiv0\), and modulo \(D\) it gives \(-fC\equiv0\). Coprimality makes the complementary factor invertible in each congruence.

## Consequence

Inside \(A>5z>w>0\), a primitive integral point on one of the nineteen cubics satisfies the first two cycle divisibilities automatically once

\[
\gcd(2A-z,2A-w)=1
\]

is imposed. The global problem reduces further to the cubic equation, \(A\mid z^3+w^3\), this coprimality condition, and the remaining primitive-state constraints.

This is a symbolic theorem. It does not establish existence or impossibility.
