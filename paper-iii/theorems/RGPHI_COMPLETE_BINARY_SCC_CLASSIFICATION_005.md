# RGΦ Trap Classification 005 — complete binary SCC theorem

Let \(x=p/q\) be reduced.

## Reduction laws

\[
\operatorname{den}(T_Bx)=\frac q{\gcd(q,B)},\qquad
\operatorname{num}(S_Bx)=\frac p{\gcd(p,B)}.
\]

These imply two forbidden high crossings: there are no distinct \(1/2\le a<b<1\) with either \(T(b)=a,S(a)=b\) or \(T(a)=b,S(b)=a\).

## Complete binary classification

Every binary closed SCC belongs to exactly one class.

### LL

\[
u=\frac{Bd+e}{B^2-1},\qquad v=\frac{d+Be}{B^2-1},
\]
for \(0\le d<e\le B-1\), with \(v<1/2\).

### LH

There is \(B\le D\le2B-3\) with
\[
D\mid(B-1)^2(B+1),\qquad D\nmid(B-1)^2,
\]
and, for \(r=B(B-1)\bmod D\),
\[
2r<D,\qquad u=r/D,\qquad v=(B-1)/D.
\]

### HH-I

\(T=id,S=swap\), with
\[
a=p/(B-1),\qquad b=q/(B-1),
\]
and
\[
pq\mid(B-1)(Bq-p-pq),\qquad pq\mid(B-1)(Bp-q-pq).
\]

### HH-II

\(T=swap,S=id\), with divisor parameter \(D\), \(r=B(B-1)\bmod D\), \(2r>D\), and
\[
r\mid(B-1)(D-r).
\]

No fifth binary class exists.

## Counterfamily to canonical-basin maximality

For every \(B=35+210t\), the trap \(G=\{1/3,2/3\}\) has the high universal predecessor \(14/15\):
\[
T_B(14/15)=S_B(14/15)=2/3.
\]
Therefore
\[
\mathcal B_{\rm canonical}\subsetneq\mathcal B_B^\forall
\]
for infinitely many bases.
