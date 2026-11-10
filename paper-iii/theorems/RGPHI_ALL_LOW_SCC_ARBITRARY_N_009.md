# RGΦ All-Low SCC Theorem 009 — arbitrary cardinality

Let
\[
L_B=\left\lceil\frac B2\right\rceil,
\qquad
\mathcal D_B=\{0,\ldots,L_B-1\}.
\]

For \(n\ge2\), all-low \(n\)-state closed SCCs are in bijection with primitive
necklaces of length \(n\) over \(\mathcal D_B\).

For a primitive word
\[
\mathbf d=(d_0,\ldots,d_{n-1}),
\]
define
\[
x_j=
\frac{
\sum_{r=0}^{n-1}d_{j+r\bmod n}B^{n-1-r}
}{
B^n-1
}.
\]
Then
\[
T_B(x_j)=x_{j+1\bmod n},
\]
the states are distinct and all lie below \(1/2\).

Conversely, below \(1/2\) the branch \(S_B\) is inadmissible, so every finite
closed strongly connected set for the deterministic map \(T_B\) is one cycle;
its branch digits give the primitive necklace.

The exact count is
\[
\boxed{
N_{LL}(B,n)=
\frac1n\sum_{d\mid n}\mu(d)L_B^{n/d}.
}
\]

For \(n=3\),
\[
\boxed{
N_{LL}(B,3)=\frac{L_B^3-L_B}{3}.
}
\]
Thus the ternary all-low sector is completely classified, and the theorem
extends to every cardinality \(n\ge2\).