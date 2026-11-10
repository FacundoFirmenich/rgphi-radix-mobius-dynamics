# RGΦ Closure Rigidity 012 — cycle reduction budget

Let \(F\subset\mathbb Q\cap(1/2,1)\) be a finite closed strongly connected
component for
\[
T_B(x)=\{Bx\},
\qquad
S_B=H\circ T_B\circ H^{-1},
\qquad
H(x)=\frac1{1+x}.
\]

For a reduced state \(x=p/q\), define the local reduction factors
\[
g_T(x)=\gcd(q,B),
\qquad
g_S(x)=\gcd(p,B).
\]

Recall the exact reduction laws
\[
\operatorname{den}(T_Bx)=\frac q{g_T(x)},
\qquad
\operatorname{num}(S_Bx)=\frac p{g_S(x)}.
\]

---

## Theorem 012-A — reduction budget on a high cycle

Let
\[
C:x_0\to x_1\to\cdots\to x_{m-1}\to x_0
\]
be a directed cycle entirely contained in \((1/2,1)\).

Let \(m_T\) and \(m_S\) be its numbers of \(T\)- and \(S\)-edges, and put
\[
R_C=
\prod_{\text{\(T\)-edges }x_i\to x_{i+1}}g_T(x_i)
\prod_{\text{\(S\)-edges }x_i\to x_{i+1}}g_S(x_i).
\]

Also define the numerical spread
\[
\eta_C=\min_{x\in C}x,
\qquad
\theta_C=\max_{x\in C}x,
\qquad
\rho_C=\frac{\theta_C}{\eta_C}<2.
\]

Then
\[
\boxed{
R_C\le
\rho_C^{\,m_T}
}
\]
and
\[
\boxed{
R_C\le
\rho_C^{\,m_S}.
}
\]

Consequently
\[
\boxed{
R_C\le
\rho_C^{\,\min(m_T,m_S)}
<
2^{\min(m_T,m_S)}.
}
\]

### Proof

For a \(T\)-edge \(x_i=p_i/q_i\to x_{i+1}\),
\[
q_{i+1}=\frac{q_i}{g_T(x_i)}.
\]
Since \(x_{i+1}=p_{i+1}/q_{i+1}\),
\[
\frac{p_{i+1}}{p_i}
=
\frac{x_{i+1}}{g_T(x_i)x_i}
\le
\frac{\rho_C}{g_T(x_i)}.
\]

For an \(S\)-edge,
\[
p_{i+1}=\frac{p_i}{g_S(x_i)},
\]
so
\[
\frac{p_{i+1}}{p_i}
=
\frac1{g_S(x_i)}.
\]

Multiplying numerator ratios around the cycle gives
\[
1\le
\frac{\rho_C^{m_T}}{R_C}.
\]

Dually, on a \(T\)-edge
\[
\frac{q_{i+1}}{q_i}
=
\frac1{g_T(x_i)},
\]
while on an \(S\)-edge
\[
\frac{q_{i+1}}{q_i}
=
\frac{x_i}{g_S(x_i)x_{i+1}}
\le
\frac{\rho_C}{g_S(x_i)}.
\]
Multiplication around the cycle gives the second inequality.

---

## Corollary 012-B — cardinality obstruction

Let \(F\) have cardinality \(n\), and let
\[
\ell(B)
\]
be the least prime divisor of \(B\).

If either \(T_B|_F\) or \(S_B|_F\) is not a permutation, then some edge has
reduction factor \(>1\). Every edge in a strongly connected finite graph lies
on a simple directed cycle of length at most \(n\). Therefore
\[
\ell(B)\le R_C
<
2^{\min(m_T,m_S)}
\le
2^{\lfloor n/2\rfloor}.
\]

Hence
\[
\boxed{
\ell(B)<2^{\lfloor n/2\rfloor}.
}
\]

Equivalently, every nonpermutation all-high SCC satisfies
\[
\boxed{
n\ge
2\left(\lfloor\log_2\ell(B)\rfloor+1\right).
}
\]

---

## Corollary 012-C — large-prime rigidity

If
\[
\boxed{
\ell(B)\ge2^{\lfloor n/2\rfloor},
}
\]
then every all-high closed SCC of cardinality \(n\) is in the permutation
regime:
\[
\boxed{
T_B|_F,\ S_B|_F
\text{ are permutations}.
}
\]

Indeed, if every local reduction factor equals one, \(T_B\) preserves each
denominator fibre and acts injectively there because \(B\) is invertible
modulo that denominator. Different fibres cannot collide. Thus \(T_B|_F\) is
injective and therefore bijective. The argument for \(S_B\), using numerator
fibres, is dual.

A sharper data-dependent certificate is
\[
\boxed{
\ell(B)>
\left(\frac{\max F}{\min F}\right)^{\lfloor n/2\rfloor}
\Longrightarrow
T_B|_F,\ S_B|_F
\text{ are permutations}.
}
\]

---

## Corollary 012-D — the four-state frontier

A nonpermutation all-high SCC of cardinality \(4\) would have to satisfy all
of the following:

1. \(2\mid B\) or \(3\mid B\);
2. the strict edge belongs to a Hamiltonian four-cycle;
3. that cycle has exactly two \(T\)-edges and two \(S\)-edges;
4. its total reduction product is
   \[
   R_C\in\{2,3\};
   \]
5. every other edge on that cycle has reduction factor one.

Thus the global rigidity problem at the first unresolved cardinality has been
reduced to two generator words, up to cyclic rotation:
\[
TSTS
\qquad\text{and}\qquad
TTSS,
\]
over bases divisible by \(2\) or \(3\).

---

## Boundary example — strict cycle without closed SCC

For \(B=200\),
\[
\frac{111}{182}
\xrightarrow{T}
\frac{89}{91}
\xrightarrow{S}
\frac{89}{133}
\xrightarrow{T}
\frac{111}{133}
\xrightarrow{S}
\frac{111}{182}
\]
is a high four-cycle with
\[
R_C=2.
\]

It satisfies the budget:
\[
2<
2^2.
\]

But it is not a closed all-high SCC. The alternate closure edge gives
\[
T_B(111/133)=122/133,
\]
and then
\[
T_B(122/133)=61/133<1/2.
\]

This proves that strict high cycles exist, while preserving the possibility
that full all-high closure forces permutation rigidity.

---

## Evidence boundary

Round 012 does **not** prove the global closure-rigidity conjecture.

It proves:

- an exact reduction budget for every high directed cycle;
- a cardinality lower bound for every possible nonpermutation SCC;
- a large-prime rigidity theorem;
- a complete structural reduction of the four-state counterexample problem.

The remaining open jurisdiction is concentrated in small-prime bases and
cardinality at least four.