# RGΦ Complete Ternary SCC Classification 010

Let
\[
T_B(x)=\{Bx\},\qquad
S_B=H\circ T_B\circ H^{-1},\qquad
H(x)=\frac1{1+x},
\]
with \(S_B\) admissible on \([1/2,1]\).

A ternary closed SCC is a three-element set closed under every admissible
generator and strongly connected under the directed action graph.

## 0. Endpoint lemma

No nontrivial closed SCC contains \(0,1/2\), or \(1\):

- \(T_B(0)=0\), so 0 cannot leave itself;
- \(T_B(1)=0\);
- \(S_B(1/2)=1\), hence closure would force 1 and then 0.

Thus every state of a nontrivial SCC lies in either
\((0,1/2)\) or \((1/2,1)\).

For a reduced rational \(x=p/q\), recall
\[
\operatorname{den}(T_Bx)=\frac q{\gcd(q,B)},
\qquad
\operatorname{num}(S_Bx)=\frac p{\gcd(p,B)}.
\]
Also, for a high state \(p/q\),
\[
S_B(p/q)=p/q
\iff p\mid B-1.
\]
The last equivalence follows because
\(H^{-1}(p/q)=(q-p)/p\) is reduced and must be fixed by \(T_B\).

---

# 1. LLL — complete, inherited from Round 009

Let
\[
L_B=\lceil B/2\rceil,
\qquad
\mathcal D_B=\{0,\ldots,L_B-1\}.
\]

Every all-low ternary SCC is a single \(T_B\)-cycle and is therefore in
bijection with a primitive necklace of length three over \(\mathcal D_B\).
Its exact count is
\[
\boxed{N_{LLL}(B)=\frac{L_B^3-L_B}{3}}.
\]

---

# 2. LLH — complete classification

Let \(\ell_1,\ell_2<1/2<h\).
Since \(S_B(h)\) is high and \(h\) is the unique high state, closure forces
\[
S_B(h)=h.
\]
This is only a self-loop, so strong connectivity forces \(T_B\) itself to be
a 3-cycle.

## Theorem 010-A

LLH ternary SCCs are in bijection with data \((q,r)\) such that

1. \(\gcd(q,B)=1\);
2. \(B\) has exact multiplicative order three modulo \(q\):
   \[
   B^3\equiv1\pmod q,\qquad B\not\equiv1\pmod q;
   \]
3. the orbit
   \[
   r,\quad Br\bmod q,\quad B^2r\bmod q
   \]
   has exactly two residues below \(q/2\) and one residue \(p_h\) above
   \(q/2\);
4. the unique high numerator satisfies
   \[
   \boxed{p_h\mid B-1}.
   \]

The SCC is the three reduced fractions obtained from that residue orbit.

### Infinite LLH family

The fixed set
\[
\{1/7,2/7,4/7\}
\]
is an LLH SCC for both arithmetic progressions
\[
\boxed{B\equiv9\pmod{28}}
\qquad\text{and}\qquad
\boxed{B\equiv25\pmod{28}}.
\]
Here \(4/7\) is the unique high state and is \(S_B\)-fixed.

---

# 3. LHH — complete structural and arithmetic classification

Write the states as
\[
\ell<1/2<a<b<1.
\]
The restriction of \(S_B\) to \(\{a,b\}\) is one of: identity, swap,
collapse to \(a\), or collapse to \(b\).

## Lemma 010-B1 — collapse to the upper high state is impossible

If \(S(a)=S(b)=b\), then any path from \(b\) to \(a\) must reach \(a\)
through \(T\)-edges only. Hence \(q_a\le q_b\). But \(S(a)=b\) gives
\(p_b\le p_a\). Therefore \(b\le a\), contradiction.

## Lemma 010-B2 — collapse to the lower high state is impossible

Assume \(S(a)=S(b)=a\). Then \(S(a)=a\) gives \(\gcd(p_a,B)=1\), while
\[
p_a=\frac{p_b}{\gcd(p_b,B)}.
\]
If \(\gcd(p_b,B)\ge2\), then
\(p_b\ge2p_a>q_a\ge q_b\), contradicting \(b<1\).
Thus \(p_a=p_b=P\).

Since \(a\) must reach \(b\) through \(T\)-edges only, denominator monotonicity
gives \(q_b\le q_a\). Because \(b>a\) and the numerators are equal,
\(q_b<q_a\). A strict denominator drop under one or two \(T\)-steps is by an
integer factor at least two, so \(q_a\ge2q_b>2P\), contradicting \(a>1/2\).

Thus both collapse patterns are globally impossible.

## Type LHH-I — \(S=id\), \(T\) a 3-cycle

If \(S\) is the identity on the two highs, it contributes only loops, so
\(T\) itself must be a 3-cycle.

Equivalently, choose a reduced exact period-three residue orbit modulo \(q\)
with exactly one low and two high residues, and require that **both** high
numerators divide \(B-1\).

This is necessary and sufficient.

Two infinite exact families are:
\[
\boxed{B\equiv61\pmod{780}},
\qquad
\{4/13,10/13,12/13\},
\]
and
\[
\boxed{B\equiv121\pmod{210}},
\qquad
\{3/7,5/7,6/7\}.
\]

## Type LHH-II — \(S\) swaps the highs

From the numerator law around the 2-cycle,
\[
\boxed{a=P/q_a,\qquad b=P/q_b,\qquad \gcd(P,B)=1}.
\]
Thus the two highs have the same reduced numerator.

Strong connectivity, the two forbidden high crossings from Round 005, and the
integer-factor denominator law force the following unique architecture:

- one high \(f=P/q_f\) is fixed by \(T\);
- the other high \(h=P/q_h\) forms a \(T\)-2-cycle with the low state;
- \(S\) swaps \(f\) and \(h\).

A complete arithmetic parameterization is:

\[
P<q_f,q_h<2P,\qquad \gcd(P,q_fq_h)=1,
\]
\[
q_f\mid B-1,
\]
\[
q_h\mid B^2-1,\qquad q_h\nmid B-1,
\]
\[
P\mid B^2-1,\qquad P\nmid B-1,
\]
\[
\boxed{q_h\equiv Bq_f\pmod P},
\]
and, with
\[
r_h=BP\bmod q_h,
\]
\[
\boxed{2r_h<q_h}.
\]

Then
\[
f=P/q_f,\qquad h=P/q_h,\qquad \ell=r_h/q_h
\]
form the SCC. Conversely every LHH-II component has this form.

Two simple infinite families are
\[
\boxed{B\equiv11\pmod{60}},
\qquad
\{1/4,3/5,3/4\},
\]
and
\[
\boxed{B\equiv29\pmod{60}},
\qquad
\{2/5,3/5,3/4\}.
\]

---

# 4. HHH — complete classification

Let
\[
1/2<a<b<c<1.
\]

## Lemma 010-C1 — \(T\) and \(S\) must be permutations

Suppose a \(T\)-edge \(x\to y\) strictly reduces denominator. Then
\[
q_y\le q_x/2,
\qquad
p_y<q_y\le q_x/2<p_x.
\]
So both numerator and denominator strictly decrease.

In a strongly connected graph on three vertices there is a simple return path
from \(y\) to \(x\) of length at most two. A one-edge return is impossible by
numerator/denominator monotonicity. For a two-edge return:

- \(TT\) cannot restore the denominator;
- \(SS\) cannot restore the numerator;
- after \(TS\), the intermediate numerator is still \(<p_x\), so the final
  \(S\)-edge cannot reach \(x\);
- after \(ST\), the intermediate denominator is still \(<q_x\), so the final
  \(T\)-edge cannot reach \(x\).

Thus no strict \(T\)-reduction edge exists. If \(T\) were noninjective, a
collision would force such an edge; when denominators are preserved,
multiplication by \(B\) modulo the common denominator is injective. Hence
\(T\) is a permutation.

The argument with numerator and denominator interchanged proves that \(S\) is
also a permutation.

## Lemma 010-C2 — permutation-pattern reduction

Among pairs of permutations on three ordered vertices that generate a strongly
connected directed graph, the two high-crossing impossibility lemmas from
Round 005 eliminate every case except:

1. \(T\) a 3-cycle, \(S=id\);
2. \(T=id\), \(S\) a 3-cycle;
3. \(T\) and \(S\) distinct transpositions.

If both restrictions were 3-cycles, the T-cycle would force a common reduced denominator while the S-cycle would force a common reduced numerator, so the three states would coincide. The remaining 36-case ordered permutation check is included in the audit package.

## Type HHH-I — \(T\) a 3-cycle, \(S=id\)

All states have a common reduced denominator \(q\). Their numerators form an
exact order-three orbit under multiplication by \(B\bmod q\), all three are
high, and
\[
\boxed{p_i\mid B-1\quad(i=0,1,2)}.
\]
This condition is necessary and sufficient.

An infinite family is
\[
\boxed{B\equiv391\pmod{7410}},
\qquad
\{10/19,13/19,15/19\}.
\]
The reverse orientation occurs for
\[
B\equiv4681\pmod{7410}.
\]

## Type HHH-II — \(T=id\), \(S\) a 3-cycle

A cycle of \(S\) forces all reduced numerators to be equal:
\[
x_i=P/q_i,
\qquad \gcd(P,B)=1.
\]
Since \(T(x_i)=x_i\),
\[
q_i\mid B-1.
\]
Put
\[
c_i=q_i-P.
\]
Then the \(c_i/P\) form an exact \(T\)-3-cycle. Equivalently the residues
\(c_i\) form an exact order-three orbit modulo \(P\).

This is necessary and sufficient.

An infinite family is
\[
\boxed{B\equiv463\pmod{8778}},
\qquad
\{19/33,19/22,19/21\}.
\]
The reverse orientation occurs for
\[
B\equiv3697\pmod{8778}.
\]

## Type HHH-III — distinct transpositions

Let \(x\) be the unique state moved by both transpositions, let \(y\) be its
\(S\)-partner and \(T\)-fixed, and let \(z\) be its \(T\)-partner and
\(S\)-fixed. Then necessarily
\[
x=P/Q,\qquad y=P/R,\qquad z=U/Q.
\]

A complete arithmetic parameterization is:

\[
P<Q<2P,\qquad P<R<2P,\qquad U<Q<2U,
\]
with the three fractions reduced, together with
\[
R\mid B-1,
\qquad
U\mid B-1,
\]
\[
Q\mid B^2-1,\quad Q\nmid B-1,
\qquad
U\equiv BP\pmod Q,
\]
\[
P\mid B^2-1,\quad P\nmid B-1,
\qquad
\boxed{R\equiv BQ\pmod P}.
\]

These conditions say exactly that \(T\) swaps \(x,z\) and fixes \(y\), while
\(S\) swaps \(x,y\) and fixes \(z\).

A simple infinite family is
\[
\boxed{B\equiv99\pmod{280}},
\qquad
\{5/8,5/7,7/8\}.
\]

---

# 5. Complete ternary theorem

Every ternary closed SCC belongs to exactly one of the following classes:

1. **LLL:** primitive radix necklace of length three;
2. **LLH:** one exact \(T\)-3-cycle with one high \(S\)-fixed state;
3. **LHH-I:** \(T\)-3-cycle, both highs \(S\)-fixed;
4. **LHH-II:** \(S\)-swapped highs, one high \(T\)-fixed and the other in a
   \(T\)-2-cycle with the low state;
5. **HHH-I:** \(T\)-3-cycle, \(S=id\);
6. **HHH-II:** \(T=id\), \(S\)-3-cycle;
7. **HHH-III:** distinct transpositions.

No eighth ternary architecture exists.

## Evidence boundary

The classification is exact for cardinality three. It does **not** classify
mixed SCCs of cardinality four or higher.

The finite denominator census in the audit package is used only as a check of
the theorem, never as its proof.