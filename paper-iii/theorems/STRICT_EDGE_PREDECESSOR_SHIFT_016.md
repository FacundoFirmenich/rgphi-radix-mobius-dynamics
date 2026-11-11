# RGΦ Round 016-A — strict-edge predecessor-shift theorem

Let \(F\subset\mathbb Q\cap(1/2,1)\) be finite, closed and strongly connected. Assume the functional normal form of Round 015: one generator has exactly one strict edge of factor \(r>1\), its complement is a permutation, and the other generator is a permutation.

## Strict \(T\)

Let
\[
x_s=\frac{p_s}{rQ}\xrightarrow{T_r}x_t=\frac{p_t}{Q},
\]
and let
\[
x_u=\frac{p_u}{Q}
\]
be the predecessor of \(x_t\) in the \(T\)-permutation on \(F\setminus\{s\}\).

Write \(B=rb\). Exact reduction gives
\[
bp_s\equiv p_t\pmod Q,
\qquad
rbp_u\equiv p_t\pmod Q.
\]
Since \(\gcd(b,Q)=1\),
\[
\boxed{p_s\equiv rp_u\pmod Q.}
\]
Both \(p_s\) and \(rp_u\) lie in the open interval
\[
\left(\frac{rQ}{2},rQ\right).
\]
Hence
\[
\boxed{p_s=rp_u+kQ,\qquad |k|<r/2.}
\]
The case \(k=0\) is impossible because it makes \(p_s\) divisible by \(r\), while \(r\mid B\) and the source fraction is reduced.

Consequently:

- for \(r=2\), no strict-\(T\) defect-one all-high system exists;
- for \(r=3\), necessarily
  \[
  \boxed{p_s=3p_u\pm Q.}
  \]

## Strict \(S\)

Let
\[
x_s=\frac{rP}{q_s}\xrightarrow{S_r}x_t=\frac{P}{q_t},
\]
and let \(x_u=P/q_u\) be the predecessor of \(x_t\) in the \(S\)-permutation on the complement. Put
\[
c_s=q_s-rP,\qquad c_u=q_u-P.
\]
The conjugate radix equations give
\[
\boxed{c_s\equiv rc_u\pmod P},
\]
therefore
\[
\boxed{q_s=rq_u+kP,\qquad |k|<r.}
\]
The value \(k=0\) is impossible: it makes the source fraction equal to the predecessor after cancellation by \(r\), contradicting both reducedness and state distinctness. Thus
\[
\boxed{k\in\{-(r-1),\ldots,-1,1,\ldots,r-1\}.}
\]

## Authority

This is a symbolic theorem for arbitrary finite cardinality within the single-strict-edge/lollipop jurisdiction. It does not assume cardinality five.
