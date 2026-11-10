# RGΦ Finite-Cardinality Frontier 011

This round does **not** claim complete arbitrary-cardinality classification.
It closes three large structural sectors and isolates one genuinely open
rigidity problem.

# Theorem 011-A — complete classification with exactly one high state

Let \(F\subset\mathbb Q\cap(0,1)\) be a finite closed strongly connected
component of cardinality \(n\ge2\), with exactly one state
\[
h\ge1/2.
\]

Then:

1. \(S_B(h)=h\);
2. \(T_B|_F\) is a single \(n\)-cycle;
3. every state has one common reduced denominator \(q\), with
   \[
   \gcd(q,B)=1,\qquad \operatorname{ord}_q(B)=n;
   \]
4. if
   \[
   h=\frac{p_h}{q},
   \]
   then
   \[
   \boxed{p_h\mid B-1}.
   \]

Conversely, let \(q\) be coprime to \(B\) with
\[
\operatorname{ord}_q(B)=n,
\]
and let
\[
p_j\equiv B^j p_0\pmod q,\qquad 0<p_j<q,
\]
be its \(T_B\)-cycle.  If exactly one \(p_j/q\) is high and its numerator
divides \(B-1\), then these \(n\) states form a closed SCC with exactly one
high state.

## Proof

The only admissible \(S_B\)-edge in the component starts at \(h\).  Since
\(S_B\) always maps a high state to a high state and \(h\) is the unique high
state,
\[
S_B(h)=h.
\]
That edge is a self-loop and contributes no inter-state connectivity.
Therefore the deterministic \(T_B\)-graph itself must be strongly connected,
hence a single cycle.

Along a finite \(T_B\)-cycle,
\[
\operatorname{den}(T_Bx)
=
\frac{\operatorname{den}(x)}
{\gcd(\operatorname{den}(x),B)}
\]
cannot decrease strictly and return.  Thus the denominator is constant and
coprime to \(B\).  The cycle is multiplication by \(B\) on reduced residues
modulo \(q\), giving \(\operatorname{ord}_q(B)=n\).

Finally
\[
S_B(h)=h
\iff
T_B(H^{-1}h)=H^{-1}h.
\]
Since
\[
H^{-1}(h)=\frac{q-p_h}{p_h}
\]
is reduced, its denominator \(p_h\) must divide \(B-1\).

# Corollary 011-A1 — an explicit one-high family for every \(n\)

For every \(n\ge2\), set
\[
q_n=2^n-1,\qquad
B_n=2^n+1,
\]
and
\[
x_j=\frac{2^j}{2^n-1},
\qquad j=0,\ldots,n-1.
\]

Since
\[
B_n\equiv2\pmod{q_n},
\]
\(T_{B_n}\) cyclically permutes the \(x_j\).  Exactly
\[
x_{n-1}=\frac{2^{n-1}}{2^n-1}
\]
is high, and
\[
2^{n-1}\mid B_n-1=2^n,
\]
so it is \(S\)-fixed.

Hence every finite cardinality occurs in an explicit one-high closed SCC.
More generally the same component exists for the full CRT progression
\[
B\equiv2\pmod{2^n-1},
\qquad
B\equiv1\pmod{2^{n-1}}.
\]

This simultaneously extends the mixed binary traps and the ternary LLH
sector.

# Theorem 011-B — transitive-generator rigidity in the all-high sector

Let \(F\) be an all-high finite closed SCC of cardinality \(n\).

## B1. If \(T_B|_F\) is one \(n\)-cycle

Then
\[
\boxed{S_B|_F=id}.
\]

All states share a denominator \(q\) coprime to \(B\).  If
\(x=p/q\in F\) and \(g=\gcd(p,B)>1\), then
\[
\operatorname{num}(S_Bx)=p/g<p/2<q/2,
\]
while every target in \(F\) has denominator \(q\) and is high.  Contradiction.
Thus \(g=1\), \(S_Bx\) has numerator \(p\) and denominator \(q\), and so
\(S_Bx=x\).

Consequently every numerator in the \(T\)-cycle divides \(B-1\), and
\[
\boxed{n\le\tau(B-1)}.
\]

## B2. If \(S_B|_F\) is one \(n\)-cycle

Dually,
\[
\boxed{T_B|_F=id}.
\]

All states share one numerator \(p\) coprime to \(B\).  Any strict denominator
reduction by \(T_B\) would produce a target with denominator at most \(q/2\le
p\), impossible for a state in \([1/2,1)\).  Hence every state is \(T\)-fixed,
each denominator divides \(B-1\), and again
\[
n\le\tau(B-1).
\]

# Corollary 011-B3 — all-high transitive examples for every \(n\)

## \(T\)-transitive / \(S=id\)

For \(n\ge2\), set
\[
q=3^n-1,\qquad
p_j=q-3^j,\quad j=0,\ldots,n-1.
\]
Every \(p_j/q>1/2\).

Let
\[
L_T=\operatorname{lcm}(p_0,\ldots,p_{n-1}).
\]
Because
\[
\gcd(q,p_j)=\gcd(q,3^j)=1,
\]
the CRT system
\[
B\equiv3\pmod q,\qquad
B\equiv1\pmod{L_T}
\]
has infinitely many solutions.

For every such \(B\),
\[
T_B(p_j/q)=p_{j+1\bmod n}/q,
\qquad
S_B(p_j/q)=p_j/q.
\]

## \(S\)-transitive / \(T=id\)

Let
\[
P=3^n-1,\qquad
r_j=P-3^j,
\qquad
q_j=P+r_j=2P-3^j.
\]
Put
\[
x_j=P/q_j.
\]
Every \(x_j>1/2\).

Let
\[
L_S=\operatorname{lcm}(q_0,\ldots,q_{n-1}).
\]
Again \(\gcd(P,q_j)=1\), so
\[
B\equiv3\pmod P,\qquad
B\equiv1\pmod{L_S}
\]
has infinitely many solutions.  Then
\[
T_B(x_j)=x_j,
\qquad
S_B(x_j)=x_{j+1\bmod n}.
\]

Thus both transitive all-high architectures exist at every finite
cardinality.

# Theorem 011-C — bipartite cycle-incidence representation

Assume now only that \(F\) is all-high and that both
\[
T_B|_F,\qquad S_B|_F
\]
are permutations.

Partition \(F\) into \(T\)-cycles and \(S\)-cycles.

1. Every \(T\)-cycle has one constant denominator \(q\), with
   \(\gcd(q,B)=1\).  Along that cycle the numerators obey
   \[
   p\mapsto Bp\bmod q.
   \]

2. Every \(S\)-cycle has one constant numerator \(p\), with
   \(\gcd(p,B)=1\).  Writing \(r=q-p\), the complements obey
   \[
   r\mapsto Br\bmod p.
   \]

Construct a bipartite multigraph \(\Gamma_F\):

- left vertices are \(T\)-cycles;
- right vertices are \(S\)-cycles;
- every state \(x=p/q\) is one edge joining its \(T\)-cycle to its \(S\)-cycle.

Then
\[
\boxed{
F\text{ is strongly connected under }T,S
\iff
\Gamma_F\text{ is connected}.
}
\]

Moreover each left vertex carries the cyclic order induced by multiplication
by \(B\) modulo its denominator, while each right vertex carries the cyclic
order induced by multiplication by \(B\) on complements modulo its numerator.

Conversely every arithmetically consistent connected incidence graph of this
form realizes an all-high permutation SCC.

This converts the permutation sector at arbitrary finite cardinality into a
connected bipartite cycle-incidence problem.

# Open problem 011-D — global all-high permutation rigidity

The following statement remains open:

> Every finite all-high closed SCC has both \(T_B|_F\) and \(S_B|_F\)
> permutations.

No counterexample was found in the exact bounded audit
\[
2\le B\le1000,\qquad
\operatorname{den}(x)\le700,
\]
over closed all-high SCCs of arbitrary cardinality inside that domain.

This is finite evidence only.

Importantly, strict reduction **can** occur on a selected all-high cycle:
for \(B=200\),
\[
\frac{111}{182}
\xrightarrow{T}
\frac{89}{91}
\xrightarrow{S}
\frac{89}{133}
\xrightarrow{T}
\frac{111}{133}
\xrightarrow{S}
\frac{111}{182}.
\]
Thus no proof may argue that strict reduction is impossible on every high
cycle.

The full closure under both generators, however, leaves the high region:
\[
T_B(111/133)=122/133,
\qquad
T_B(122/133)=61/133<1/2.
\]

So the unresolved theorem is genuinely a **closure rigidity** statement, not
a cycle rigidity statement.