# RGΦ Round 021-C — four-fibre near-coprime splitting

The dense forms `DF015-0003`, `0007`, `0011` and `0017` share the state pattern
\[
\frac{P}{Q_0},\quad\frac{P}{Q_1},\quad\frac{U}{Q_1},\quad\frac{rP}{D},\quad\frac{U}{D},
\]
where \(r\in\{2,3\}\) and all fractions are primitive and high.

Every realization satisfies
\[
P\mid(Q_1-Q_0)(Q_1+Q_0-2P),
\]
\[
Q_1\mid(U-P)(U+P),
\]
\[
U\mid(D-Q_1)(D+Q_1-2U),
\]
\[
D\mid(U-rP)(U+rP).
\]

## Theorem 021-C

In each divisibility, the gcd of the modulus with both paired linear factors divides two.

For example, an odd prime dividing \(P\), \(Q_1-Q_0\) and \(Q_1+Q_0-2P\) would force \(Q_1\equiv Q_0\equiv P\equiv0\pmod\ell\), contradicting reducedness. The other cases are identical using the corresponding primitive fractions.

Therefore every odd prime power dividing a modulus belongs to exactly one of the two paired factors. Only a controlled two-adic overlap remains.

## Consequence

The dense forms reduce to divisor-allocation problems rather than height scans. The branch-specific predecessor-shift equations are recorded in `round-021/DENSE_BRANCHES_021.csv`.

This theorem does not yet eliminate the open branches.
