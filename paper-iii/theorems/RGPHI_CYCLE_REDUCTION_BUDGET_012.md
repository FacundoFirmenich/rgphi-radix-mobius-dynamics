# RGΦ Closure Rigidity 012 — cycle reduction budget

Let \(F\subset\mathbb Q\cap(1/2,1)\) be a finite closed strongly connected component for
\[
T_B(x)=\{Bx\},\qquad S_B=H\circ T_B\circ H^{-1},\qquad H(x)=\frac1{1+x}.
\]
For a reduced state \(x=p/q\), define
\[
g_T(x)=\gcd(q,B),\qquad g_S(x)=\gcd(p,B).
\]
Recall
\[
\operatorname{den}(T_Bx)=\frac q{g_T(x)},\qquad \operatorname{num}(S_Bx)=\frac p{g_S(x)}.
\]

## Theorem 012-A — reduction budget on a high cycle

Let \(C:x_0\to\cdots\to x_{m-1}\to x_0\) be a directed cycle in \((1/2,1)\). Let \(m_T,m_S\) count its T/S edges and
\[
R_C=\prod_{T\text{-edges}}g_T(x_i)\prod_{S\text{-edges}}g_S(x_i).
\]
Put \(\eta_C=\min_Cx\), \(\theta_C=\max_Cx\), \(\rho_C=\theta_C/\eta_C<2\). Then
\[
\boxed{R_C\le\rho_C^{m_T}},\qquad \boxed{R_C\le\rho_C^{m_S}},
\]
therefore
\[
\boxed{R_C\le\rho_C^{\min(m_T,m_S)}<2^{\min(m_T,m_S)}}.
\]

For a T-edge, \(q_{i+1}=q_i/g_T(x_i)\) and
\[
\frac{p_{i+1}}{p_i}=\frac{x_{i+1}}{g_T(x_i)x_i}\le\frac{\rho_C}{g_T(x_i)}.
\]
For an S-edge, \(p_{i+1}/p_i=1/g_S(x_i)\). Multiplication around the cycle proves the first inequality; the denominator-dual argument proves the second.

## Corollary 012-B — cardinality obstruction

If an all-high closed SCC of cardinality \(n\) is nonpermutational, then, for the least prime divisor \(\ell(B)\),
\[
\boxed{\ell(B)<2^{\lfloor n/2\rfloor}},
\]
equivalently
\[
\boxed{n\ge2(\lfloor\log_2\ell(B)\rfloor+1)}.
\]

## Corollary 012-C — large-prime rigidity

If
\[
\ell(B)\ge2^{\lfloor n/2\rfloor},
\]
then
\[
\boxed{T_B|_F,\ S_B|_F\text{ are permutations}}.
\]
A sharper data-dependent certificate is
\[
\ell(B)>\left(\frac{\max F}{\min F}\right)^{\lfloor n/2\rfloor}
\Longrightarrow T_B|_F,S_B|_F\text{ are permutations}.
\]

## Four-state frontier and boundary control

For \(|F|=4\), every nonpermutation candidate is over a base divisible by 2 or 3 and contains a Hamiltonian cycle of word `TSTS` or `TTSS`, with total reduction product 2 or 3 and every other cycle edge unreduced.

A strict high cycle can exist without closed all-high SCC. For \(B=200\),
\[
111/182\xrightarrow T89/91\xrightarrow S89/133\xrightarrow T111/133\xrightarrow S111/182,
\]
but the alternate closure route gives \(T(111/133)=122/133\) and then \(T(122/133)=61/133<1/2\).

## Evidence boundary

This theorem supplies the exact budget, cardinality obstruction and four-state reduction. It does not by itself prove global closure rigidity.
