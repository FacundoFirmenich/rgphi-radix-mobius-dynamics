# RGΦ Round 021-B — common boundary point and relative-integral finiteness

Let
\[
C=2A-z,\qquad D=2A-w,
\]
and let \([A:z:w]\) be a primitive integral projective point on a smooth cubic \(F_n=0\).

## Universal boundary point

The rational point
\[
\boxed{R=[1:2:2]}
\]
lies on every curve \(F_n=0\).

## Theorem 021-B

For every prime \(p\),
\[
\boxed{p\mid\gcd(C,D)\iff[A:z:w]\bmod p=R.}
\]

If \(p\mid C,D\), then \(z\equiv2A\) and \(w\equiv2A\pmod p\). Primitivity excludes \(A\equiv0\pmod p\), so the reduction is \(R\). The converse is immediate.

Thus \(\gcd(C,D)=1\) means exactly that the rational point avoids \(R\) in every finite reduction.

## Corollary 021-B1 — finiteness

For each fixed \(n\), the primitive rational points on \(F_n=0\) satisfying
\[
\gcd(2A-z,2A-w)=1
\]
form a finite set.

After adjoining the finitely many bad primes to a set \(S_n\), these points are \(S_n\)-integral relative to the nonempty divisor \([R]\) on the elliptic curve \(F_n\). Siegel's theorem gives finiteness.

Round 020 proved that \(F_{17}\) has positive rank and infinitely many rational chamber points. Round 021 shows that only finitely many can satisfy the RGΦ coprimality condition.

## Boundary

Siegel's theorem supplies finiteness, not the explicit list. Effective relative-integral enumeration remains open.
