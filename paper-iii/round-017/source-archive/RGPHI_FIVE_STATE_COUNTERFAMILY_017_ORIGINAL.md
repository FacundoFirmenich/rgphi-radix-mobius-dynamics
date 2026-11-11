# RGΦ Round 017 — exact five-state nonpermutation counterfamily

Let
\[
T_B(x)=\{Bx\},\qquad
H(x)=\frac1{1+x},\qquad
S_B=H\circ T_B\circ H^{-1}.
\]

Define the five reduced high rationals
\[
\begin{aligned}
x_0&=\frac{406}{557},&
 x_1&=\frac{406}{731},&
 x_2&=\frac{712}{731},\\
x_3&=\frac{1218}{1265},&
 x_4&=\frac{712}{1265}.
\end{aligned}
\]
They are pairwise distinct and all belong to \((1/2,1)\).

Put
\[
B_0=88\,011\,536\,665\,779,
\qquad
M=223\,336\,848\,698\,040,
\]
and for every integer \(t\ge0\) let
\[
\boxed{B_t=B_0+tM.}
\]

## Theorem 017-A — exact closed SCC

For every \(t\ge0\), the set
\[
F=\{x_0,x_1,x_2,x_3,x_4\}
\]
is closed under \(T_{B_t},S_{B_t}\), strongly connected, and has action tables
\[
\boxed{T=(0)(1\ 2)(3\ 4)},
\]
\[
\boxed{S=(0\ 1)(2\ 4),\qquad 3\mapsto1.}
\]
Equivalently,
\[
T=(0,2,1,4,3),\qquad S=(1,0,4,1,2)
\]
in image-list notation.

The unique strict edge is
\[
\boxed{x_3\xrightarrow{S_3}x_1},
\]
because
\[
\gcd(1218,B_t)=3,
\]
whereas every other numerator and every denominator is coprime to \(B_t\).
Thus \(S|_F\) is not a permutation: state \(x_1\) has two \(S\)-preimages and \(x_3\) has none.

## CRT construction

The six required congruences are
\[
\begin{array}{rcl}
B&\equiv&1\pmod{557},\\
B&\equiv&349\pmod{406},\\
B&\equiv&171\pmod{731},\\
B&\equiv&179\pmod{712},\\
B&\equiv&254\pmod{1265},\\
B&\equiv&1161\pmod{1218}.
\end{array}
\]
They are mutually compatible. Their generalized CRT solution is
\[
B\equiv B_0\pmod M,
\]
where
\[
M=\operatorname{lcm}(557,406,731,712,1265,1218).
\]

### The \(T\)-edges

Modulo \(557\), \(B\equiv1\), hence \(T(x_0)=x_0\).

Modulo \(731\), \(B\equiv171\), and
\[
171\cdot406\equiv712\pmod{731},\qquad
171\cdot712\equiv406\pmod{731},
\]
so \(T\) swaps \(x_1,x_2\).

Modulo \(1265\), \(B\equiv254\), and
\[
254\cdot1218\equiv712\pmod{1265},\qquad
254\cdot712\equiv1218\pmod{1265},
\]
so \(T\) swaps \(x_3,x_4\).

### The unreduced \(S\)-edges

For numerator \(406\), the complementary residues are
\[
557-406=151,\qquad731-406=325.
\]
Since \(B\equiv349\pmod{406}\),
\[
349\cdot151\equiv325\pmod{406},\qquad
349\cdot325\equiv151\pmod{406},
\]
so \(S\) swaps \(x_0,x_1\).

For numerator \(712\), the complementary residues are
\[
731-712=19,\qquad1265-712=553.
\]
Since \(B\equiv179\pmod{712}\),
\[
179\cdot19\equiv553\pmod{712},\qquad
179\cdot553\equiv19\pmod{712},
\]
so \(S\) swaps \(x_2,x_4\).

### The strict \(S\)-edge

For \(x_3\),
\[
p_3=1218=3\cdot406,\qquad q_3-p_3=47.
\]
The congruence \(B\equiv1161\pmod{1218}\) gives
\[
\frac B3\equiv387\pmod{406}.
\]
Then
\[
387\cdot47\equiv325\pmod{406},
\]
which is precisely the complement of \(x_1=406/731\). Hence
\[
S(x_3)=x_1
\]
with reduction factor three.

## Strong connectivity

From \(x_0\), the path
\[
x_0\xrightarrow Sx_1\xrightarrow Tx_2\xrightarrow Sx_4\xrightarrow Tx_3
\]
reaches every state. Every state returns to \(x_0\): \(x_1\xrightarrow Sx_0\),
\(x_2\xrightarrow T x_1\xrightarrow Sx_0\),
\(x_4\xrightarrow Sx_2\), and \(x_3\xrightarrow Sx_1\).
Therefore the closed graph is strongly connected.

## Corollary 017-B — sharp minimal cardinality

All-high permutation rigidity was already proved for cardinalities \(2,3,4\). The family above is a nonpermutational all-high SCC of cardinality five. Therefore
\[
\boxed{\text{the least possible nonpermutational all-high cardinality is exactly }5.}
\]

In particular, the conjecture of global all-high permutation rigidity is false.

## Evidence boundary

This theorem is an exact symbolic/CRT construction. The finite targeted scan that discovered the parameters is not part of the proof.