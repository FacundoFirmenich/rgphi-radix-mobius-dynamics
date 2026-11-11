# RGΦ Round 021-D — countergraph divisor-allocation normal form

For the realized branch `DF015-0007-B2`, write
\[
Q_0=P+a,\quad Q_1=P+b,\quad U=P+c,\quad D=3Q_0-P=2P+3a.
\]
The chamber is
\[
\frac P3<a<\frac{2P}{3},\qquad\frac{3a}{2}<c<b<P.
\]
The state-side system is
\[
P\mid(b-a)(b+a),
\]
\[
P+b\mid c(2P+c),
\]
\[
P+c\mid(P+3a-b)(P+3a+b-2c),
\]
\[
2P+3a\mid(c-2P)(c+4P).
\]
Each paired-factor overlap divides two, so odd prime powers have unique side allocation.

The known solution is
\[
(P,a,b,c)=(406,151,325,306),
\]
corresponding to
\[
(Q_0,Q_1,U,D)=(557,731,712,1265).
\]
Its exact allocations are recorded in `round-021/KNOWN_SOLUTION_DIVISOR_ALLOCATIONS.csv`.

An independent exact audit through \(Q_1\le16000\), \(D\le48000\) examined 496,924,929 candidates and again found exactly this tuple. This is finite evidence, not a global uniqueness proof.
