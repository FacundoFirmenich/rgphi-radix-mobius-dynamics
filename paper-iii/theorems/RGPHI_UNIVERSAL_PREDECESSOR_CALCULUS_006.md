# RGΦ Basin Classification 006 — exact universal-predecessor calculus

Let \(A\subset\mathbb Q\cap(0,1)\) be finite and let
\[
A_H=A\cap(1/2,1).
\]
Define
\[
\mathcal U_B(A)=
\{x:\text{every admissible child of }x\text{ lies in }A\}.
\]

## Theorem 006-A — low universal predecessors

For \(y\in A\), every low predecessor is
\[
x=\frac{k+y}{B},\qquad 0\le k\le B-1,
\]
subject only to \(x<1/2\).

Thus
\[
\mathcal L_B(A)=
\bigcup_{y\in A}
\left\{\frac{k+y}{B}<\frac12:0\le k<B\right\}.
\]

A low state has only the \(T_B\)-action, so this is exact.

## Theorem 006-B — divisor-lift classification of high predecessors

Fix reduced targets
\[
y=\frac AC\in A,\qquad
z=\frac PQ\in A_H.
\]

A reduced high state \(x=p/q\) satisfies
\[
T_B(x)=y,\qquad S_B(x)=z
\]
iff there exist divisors \(a,b\mid B\) such that
\[
p=aP,\qquad q=bC,
\]
and all of the following hold:
\[
\gcd(aP,B)=a,\qquad \gcd(bC,B)=b,
\]
\[
\gcd(aP,bC)=1,
\]
\[
bC>aP,\qquad 2aP\ge bC,
\]
\[
\left(\frac Bb\,aP\right)\bmod C=A,
\]
and
\[
\left(\frac Ba\,(bC-aP)\right)\bmod P=Q-P.
\]

### Proof

For reduced \(x=p/q\),
\[
\operatorname{den}(T_Bx)=\frac q{\gcd(q,B)}.
\]
Hence \(T_Bx=y=A/C\) forces
\[
q=bC,\qquad b=\gcd(q,B).
\]
After this reduction,
\[
T_B(x)=
\frac{((B/b)p)\bmod C}{C},
\]
giving the first congruence.

Similarly
\[
\operatorname{num}(S_Bx)=\frac p{\gcd(p,B)}.
\]
Thus \(S_Bx=z=P/Q\) forces
\[
p=aP,\qquad a=\gcd(p,B).
\]
Since \(H^{-1}(x)=(q-p)/p\) is reduced,
\[
T_B(H^{-1}x)
=
\frac{((B/a)(q-p))\bmod P}{P}.
\]
But
\[
H^{-1}(z)=\frac{Q-P}{P},
\]
which gives the second congruence.  The gcd and interval conditions are exactly
the conditions that \(x\) be the stated reduced high rational.  The converse
follows by reversing the calculation. ∎

## Corollary 006-B1 — finite candidate bound

Let \(\tau(B)\) denote the divisor-counting function.  For a finite \(A\),
\[
|\mathcal H_B(A)|
\le |A|\,|A_H|\,\tau(B)^2.
\]

Therefore
\[
\boxed{
\mathcal U_B(A)=
\mathcal L_B(A)\cup
\mathcal H_B(A)
}
\]
is computable from a finite arithmetic candidate set, without searching the
ambient rational interval.

## Theorem 006-C — exact maximal universal basin recursion

Let \(G\) be any finite closed trap.  Define
\[
A_0=G,\qquad
A_{n+1}=A_n\cup\mathcal U_B(A_n).
\]
Then the finite-time universal basin is exactly
\[
\boxed{
\mathcal B^\forall_B(G)=\bigcup_{n\ge0}A_n.
}
\]

Every state in \(A_n\) reaches \(G\) under every admissible policy in at most
\(n\) further predecessor ranks.  Conversely, a state universally forced into
\(G\) in finite time belongs to some \(A_n\).

Since each state has at most two admissible children, if every path from a
state eventually enters \(G\) but no uniform finite bound existed, König's
lemma would produce an infinite path avoiding \(G\).  Hence the same union
also captures the ordinary universal eventual-entry basin.

This gives an exact arithmetic recursion for the maximal universal basin.

## Corollary 006-D — recovery of the Round-005 counterfamily

For
\[
G=\{1/3,2/3\},\qquad B\equiv35\pmod{210},
\]
take \(z=y=2/3\), \(a=7\), \(b=5\).  The divisor-lift theorem gives
\[
x=\frac{a\,2}{b\,3}=\frac{14}{15},
\]
and the congruences reduce precisely to
\[
B/5\equiv1\pmod3,\qquad B/7\equiv1\pmod2.
\]
Together with \(5,7\mid B\), this is
\[
B=35(6t+1)=35+210t.
\]

Thus the previous counterfamily is a special case of the general calculus.

## Theorem 006-E — an infinite two-level high branch

For every
\[
\boxed{B\equiv665\pmod{19950}},
\]
the trap \(G=\{1/3,2/3\}\) has
\[
h_1=\frac{14}{15}\in A_1
\]
and
\[
h_2=\frac{38}{75}\in A_2\setminus A_1
\]
with
\[
T_B(h_2)=h_1,\qquad S_B(h_2)=2/3.
\]

Indeed the first layer follows from \(B\equiv35\pmod{210}\).  For the second,
\[
T_B(38/75)=14/15
\]
is equivalent to
\[
38B\equiv70\pmod{75},
\]
i.e.
\[
B\equiv65\pmod{75},
\]
while
\[
S_B(38/75)=2/3
\]
is equivalent to
\[
37B\equiv19\pmod{38},
\]
i.e.
\[
B\equiv19\pmod{38}.
\]
The simultaneous CRT solution with \(B\equiv35\pmod{210}\) is
\[
B\equiv665\pmod{\operatorname{lcm}(210,75,38)}
=
665\pmod{19950}.
\]

Therefore high universal structure is not restricted to a single finite
decoration attached directly to the trap.

## Evidence boundary

The exact predecessor calculus is complete for every finite target set \(A\).

It does not yet give a closed-form description of the infinite fixed point
\(\mathcal B^\forall_B(G)\) for every trap.  The recursion can generate
additional high states at later ranks, and classifying the resulting
graph-directed structure is the next problem.