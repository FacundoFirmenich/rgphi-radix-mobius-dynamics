# RGΦ Round 016-B — global no-go for strict \(T\) factor two

Under the hypotheses of the predecessor-shift theorem, a strict \(T\)-edge of factor \(2\) would satisfy
\[
p_s=2p_u+kQ,\qquad |k|<1.
\]
Therefore \(k=0\), so
\[
p_s=2p_u.
\]
But \(2\mid B\). Hence
\[
\gcd(p_s,B)\ge2,
\]
contradicting the fact that the other generator is unreduced at the source and that \(p_s/(2Q)\) is primitive.

Thus
\[
\boxed{\text{no finite all-high defect-one lollipop can have a strict }T\text{ edge of factor }2.}
\]

This eliminates `DF015-0009` and `DF015-0010` globally, not merely inside a bounded search.
