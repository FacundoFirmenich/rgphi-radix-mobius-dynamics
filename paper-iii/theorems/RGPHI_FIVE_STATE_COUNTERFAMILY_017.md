# RGΦ Round 017 — exact five-state counterfamily and sharp rigidity threshold

Let
\[
R=88\,011\,536\,665\,779,\qquad
M=223\,336\,848\,698\,040,
\]
and for every integer \(n\ge0\) put
\[
B_n=R+nM.
\]

Define five reduced rational states
\[
x_0=\frac{406}{731},\quad
x_1=\frac{712}{731},\quad
x_2=\frac{712}{1265},\quad
x_3=\frac{1218}{1265},\quad
x_4=\frac{406}{557}.
\]

Every state lies strictly in \((1/2,1)\).

## Theorem 017-A — exact action table

For every \(n\ge0\),
\[
T_{B_n}:(x_0\ x_1)(x_2\ x_3)(x_4),
\]
while
\[
S_{B_n}(x_0)=x_4,\quad S_{B_n}(x_4)=x_0,
\]
\[
S_{B_n}(x_1)=x_2,\quad S_{B_n}(x_2)=x_1,
\]
and
\[
S_{B_n}(x_3)=x_0.
\]

Thus \(T_{B_n}|_F\) is a permutation, but \(S_{B_n}|_F\) is not:
\(x_0\) has the two \(S\)-preimages \(x_3,x_4\), and \(x_3\) has no
\(S\)-preimage.

The set
\[
F=\{x_0,x_1,x_2,x_3,x_4\}
\]
is closed and strongly connected. Indeed
\[
x_3\xrightarrow Sx_0\xrightarrow Tx_1\xrightarrow Sx_2\xrightarrow Tx_3
\]
is a directed four-cycle, and
\[
x_0\xleftrightarrow{S}x_4.
\]

## CRT certificate

The simultaneous edge congruences are
\[
B\equiv171\pmod{731},
\qquad
B\equiv254\pmod{1265},
\qquad
B\equiv1\pmod{557},
\]
\[
B\equiv349\pmod{406},
\qquad
B\equiv179\pmod{712},
\qquad
B\equiv1161\pmod{1218}.
\]

Their generalized CRT solution is exactly
\[
B\equiv R\pmod M,
\]
where
\[
M=\operatorname{lcm}(731,1265,557,406,712,1218).
\]

The ordinary radix congruences are certified by
\[
171\cdot406\equiv712,\quad
171\cdot712\equiv406\pmod{731},
\]
\[
254\cdot712\equiv1218,\quad
254\cdot1218\equiv712\pmod{1265}.
\]
The fixed state satisfies \(B\equiv1\pmod{557}\).

For the ordinary \(S\)-cycles, the complementary residues are
\[
731-406=325,\quad557-406=151,
\]
and
\[
731-712=19,\quad1265-712=553.
\]
Hence
\[
349\cdot325\equiv151,\quad
349\cdot151\equiv325\pmod{406},
\]
\[
179\cdot19\equiv553,\quad
179\cdot553\equiv19\pmod{712}.
\]

Finally
\[
\gcd(B_n,1218)=3.
\]
Writing \(B_n=3b_n\), the strict edge has source complement
\[
1265-1218=47
\]
and target complement
\[
731-406=325.
\]
Since
\[
b_n\equiv387\pmod{406},
\qquad
387\cdot47\equiv325\pmod{406},
\]
we obtain
\[
S_{B_n}(1218/1265)=406/731
\]
with exact numerator reduction factor \(3\).

All remaining numerator and denominator gcds with \(B_n\) are one.

## Corollary 017-B — sharp minimal cardinality

All-high permutation rigidity is already proved for cardinalities \(2,3,4\).
The family above is a closed strongly connected nonpermutation example of
cardinality \(5\). Therefore
\[
\boxed{
\min\{|F|:\ F\text{ is a finite all-high closed SCC and }T|_F
\text{ or }S|_F\text{ is nonpermutational}\}=5.
}
\]

Hence the global all-high permutation-rigidity conjecture is false, and the
threshold \(4/5\) is sharp.

## Location in the conditional Round-016 jurisdiction

Within the defect-one taxonomy, this counterfamily realizes branch
\[
\boxed{\texttt{DF015-0007-B2}}
\]
with
\[
D_1=3D_2-A_0.
\]
In fibre variables
\[
A_0=406,\quad A_1=712,\quad
D_0=731,\quad D_1=1265,\quad D_2=557,
\]
and indeed
\[
1265=3\cdot557-406.
\]

## Evidence boundary

This theorem proves existence, infinitude in the base parameter, and sharp
minimal cardinality. It does not depend on the Round-015/016 quotient being
globally exhaustive. It does not classify every five-state nonpermutation
component, does not adjudicate the other conditional Round-016 branches, and
does not treat architectures with additional strict edges outside the witness
cycle.
