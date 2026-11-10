# RGΦ Trap Classification 005 — complete binary SCC theorem

Let \(x=p/q\) always denote a reduced rational.

## Lemma 1 — denominator law for \(T_B\)

For
\[
T_B(x)=\{Bx\},
\]
the reduced denominator is
\[
\operatorname{den}(T_Bx)=\frac{q}{\gcd(q,B)}.
\]

Before reduction the numerator is \(Bp-dq\), hence
\[
\gcd(Bp-dq,q)=\gcd(B,q).
\]

## Lemma 2 — numerator law for \(S_B\)

For a high state \(x=p/q\ge1/2\),
\[
S_B(x)=
\frac{p}{Bq-(B-1+d_S)p}
\]
before reduction. Therefore
\[
\operatorname{num}(S_Bx)=\frac{p}{\gcd(p,B)}.
\]

Indeed the gcd of numerator and denominator before reduction is
\[
\gcd(p,Bq)=\gcd(p,B).
\]

## Lemma 3 — first forbidden crossing

There are no distinct high states
\[
\frac12\le a<b<1
\]
with
\[
T_B(b)=a,\qquad S_B(a)=b.
\]

Write \(a=p_a/q_a\), \(b=p_b/q_b\).
The first identity gives \(q_a\le q_b\); the second gives \(p_b\le p_a\).
Hence \(b\le a\), contradiction.

## Lemma 4 — second forbidden crossing

There are no distinct high states
\[
\frac12\le a<b<1
\]
with
\[
T_B(a)=b,\qquad S_B(b)=a.
\]

Let
\[
g_q=\gcd(q_a,B),\qquad g_p=\gcd(p_b,B).
\]
Then
\[
q_b=q_a/g_q,\qquad p_a=p_b/g_p,
\]
hence
\[
\frac ba=g_pg_q.
\]
The right side is an integer. Since \(a<b\), it is at least \(2\); but
\(a\ge1/2\) and \(b<1\) imply \(b/a<2\). Contradiction.

# Theorem 005-A — global exclusion of the seven open high–high patterns

For two high states \(a<b\), the seven previously open strongly connected
patterns are impossible:

- `swap/swap`: contains both forbidden crossings;
- `swap/c0`: contains \(T(a)=b,\ S(b)=a\);
- `swap/c1`: contains \(T(b)=a,\ S(a)=b\);
- `c0/swap`: contains \(T(b)=a,\ S(a)=b\);
- `c0/c1`: contains \(T(b)=a,\ S(a)=b\);
- `c1/swap`: contains \(T(a)=b,\ S(b)=a\);
- `c1/c0`: contains \(T(a)=b,\ S(b)=a\).

Thus the only realizable strongly connected high–high patterns are
\[
\boxed{T=id,\ S=swap}
\]
and
\[
\boxed{T=swap,\ S=id}.
\]

# Theorem 005-B — complete binary closed-SCC classification

Every binary closed strongly connected component belongs to exactly one of
four arithmetic classes.

## LL

Both states are below \(1/2\):
\[
u=\frac{Bd+e}{B^2-1},\qquad
v=\frac{d+Be}{B^2-1},
\]
for \(0\le d<e\le B-1\), with \(v<1/2\).

## LH

One state is low and one high.  There is
\[
B\le D\le2B-3
\]
with
\[
D\mid(B-1)^2(B+1),\qquad D\nmid(B-1)^2,
\]
and, writing
\[
r=B(B-1)\bmod D,
\]
\[
2r<D,\qquad
u=\frac rD,\qquad v=\frac{B-1}{D}.
\]

## HH-I

Both states are high, \(T=id\), \(S=swap\):
\[
a=\frac p{B-1},\qquad b=\frac q{B-1},
\]
and
\[
pq\mid(B-1)(Bq-p-pq),
\]
\[
pq\mid(B-1)(Bp-q-pq).
\]

## HH-II

Both states are high, \(T=swap\), \(S=id\).  There is a divisor parameter
\(D\) as in the period-two classification, with
\[
r=B(B-1)\bmod D,\qquad 2r>D,
\]
and
\[
r\mid(B-1)(D-r).
\]

No fifth binary class exists.

# Theorem 005-C — infinite counterfamily to canonical-basin maximality

For every
\[
B=35+210t,\qquad t\ge0,
\]
the pair
\[
G=\{1/3,2/3\}
\]
is a mixed binary trap:
\[
T_B(1/3)=2/3,\qquad
T_B(2/3)=1/3,\qquad
S_B(2/3)=2/3.
\]

Let
\[
x=14/15.
\]
Since \(B\equiv5\pmod{15}\),
\[
T_B(14/15)=2/3.
\]
Also \(H^{-1}(14/15)=1/14\), and since \(B\equiv7\pmod{14}\),
\[
T_B(1/14)=1/2,
\]
so
\[
S_B(14/15)=H(1/2)=2/3.
\]

Hence
\[
\boxed{T_B(14/15)=S_B(14/15)=2/3}.
\]

Thus \(14/15\) is a high universal predecessor of the trap.  The canonical
Round-003 basin contains no high state outside the trap itself, so
\[
\boxed{
\mathcal B_{\rm canonical}
\subsetneq
\mathcal B^\forall_{\rm maximal}
}
\]
for infinitely many bases.

This globally refutes the equality conjecture from Round 004.