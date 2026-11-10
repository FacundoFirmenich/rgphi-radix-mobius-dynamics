# RGΦ Effective Bound 009 — explicit fixed-base depth envelope

Round 008 reduced fixed-base high-depth finiteness to a binary \(S\)-unit
equation. This round makes that argument quantitatively explicit.

Let \(B\ge2\) be fixed and \(G\) a finite closed trap. Let
\[
\Sigma_0=
\operatorname{PrimeDiv}\!\left(
B\prod_{g\in G}\operatorname{num}(g)\operatorname{den}(g)
\right).
\]
For each
\[
k\in\{B-1,\ldots,2B-2\},
\]
put
\[
\Sigma_k=\Sigma_0\cup\operatorname{PrimeDiv}(k),
\qquad s_k=|\Sigma_k|.
\]

## Theorem 009-A — explicit \(S\)-chain bound

Set
\[
N_k=3\cdot7^{2s_k+3},
\qquad
M_B=\sum_{k=B-1}^{2B-2}N_k.
\]
Then
\[
\boxed{
D_S(B,G)=(\omega(B)+1)M_B
}
\]
bounds the length of every chain of distinct high universal-basin states
linked by \(S_B(x_{j+1})=x_j\).

### Proof sketch

Along a backward \(S\)-chain, the support of primes of \(B\) in the numerator
can enlarge at most \(\omega(B)\) times. Hence there are at most
\(\omega(B)+1\) support phases.

Inside one phase,
\[
p_{n+1}=A p_n,\qquad A\mid B
\]
with \(A\) fixed, and \(C=B/A\). If the active branch digit is \(d_n\), put
\[
k_n=B-1+d_n.
\]
Then
\[
Cq_{n+1}-q_n=k_np_n.
\]
Thus
\[
u_n=\frac{q_n}{Cq_{n+1}},
\qquad
v_n=\frac{k_np_n}{Cq_{n+1}}
\]
are \(\Sigma_{k_n}\)-units satisfying \(u_n+v_n=1\).

Evertse's quantitative theorem over \(\mathbb Q\) gives at most
\(3\cdot7^{2s_k+3}\) such solutions for a fixed \(k\).
For fixed \(k\), the state is recovered from
\[
x_n=\frac{v_n}{k u_n},
\]
so the mapping is injective. Summing over digits and support phases gives the
bound.

## Corollary 009-A1 — explicit high-state count

If \(g_H\) is the number of high trap states, then
\[
\boxed{
H_*(B,G)=g_H\frac{B^{D_S+1}-1}{B-1}
}
\]
bounds the total number of high universal-basin states.

## Corollary 009-A2 — explicit universal-rank bound

Let
\[
P_*=\max\{\operatorname{num}(g):g\in G,\ g\ge1/2\}.
\]
Every high state satisfies
\[
p\le P_*B^{D_S},
\qquad
q<2P_*B^{D_S}.
\]
Set
\[
Q_*=2P_*B^{D_S}.
\]
A deterministic low \(T_B\)-segment with denominator at most \(Q_*\) can visit
at most \(Q_*^2\) distinct rational states before repeating. A repeated low
state before reaching lower rank would never enter the trap, so this cannot
occur in the universal basin.

Hence
\[
\boxed{
K_{\rm explicit}(B,G)
=
H_*(B,G)(Q_*^2+1)
}
\]
is a fully explicit fixed-base upper bound.

## Boundary

The bound is valid but astronomically loose. Its purpose is to turn
effectivity into a closed formula; practical sharpening remains open.