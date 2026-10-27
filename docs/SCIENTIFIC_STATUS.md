# Scientific status

**Canonical date:** 27 October 2026  
**Repository status:** public pre-DOI release candidate  
**Primary manuscript:** *Nonnested extremal targets in a rational radix–Möbius semigroup*

This document is the authoritative high-level boundary between **proved**, **computer-assisted**, **open**, and **superseded** statements in the repository.

## 1. Core dynamical system

For integer \(B\ge2\),

\[
T_B(x)=\{Bx\},\qquad
H(x)=\frac1{1+x},\qquad
S_B=H\circ T_B\circ H^{-1}.
\]

The system acts on rational states in the admissible branches of \((0,1)\).

For reduced \(x=a/b\),

\[
q(x)=\frac{b}{b-a},
\qquad
P_m(B,\kappa)=\{x:q(x)>\kappa B^m\}.
\]

## 2. Closed symbolic results

The following are algebraic identities or theorems.

### 2.1 Integer-branch matrices

For the appropriate branch digit \(d\),

\[
M_{T_B}(d)=
\begin{pmatrix}
B&-d\\
0&1
\end{pmatrix},
\qquad
M_{S_B}(d)=
\begin{pmatrix}
1&0\\
-(B-1+d)&B
\end{pmatrix},
\]

with determinant \(B\).

### 2.2 Seed-family identity

For

\[
x_{N,r}=\frac{N}{N+r},
\qquad
s\equiv Br\pmod N,
\]

one has

\[
S_B(x_{N,r})=\frac{N}{N+s}.
\]

### 2.3 Radix denominator law

For reduced \(a/q\),

\[
\operatorname{den}(T_B^n(a/q))
=
\frac{q}{\gcd(q,B^n)}.
\]

Once the denominator component supported on primes dividing \(B\) has been removed, the remaining radix orbit is periodic with period governed by the multiplicative order of \(B\) modulo the coprime denominator component.

## 3. Closed finite-exhaustive results

For the benchmark \(B=10\), seed \(17/19\), \(\kappa=11\), and the repository terminal convention,

\[
\boxed{
\tau_1=45,\quad
\tau_2=85,\quad
\tau_3=120,\quad
\tau_4=162.
}
\]

The corresponding extremal states fail nested optimality at three consecutive levels:

\[
45\to87>85,\qquad
85\to139>120,\qquad
120\to168>162.
\]

The exact common robustness interval for the four-level chronology is

\[
\boxed{\kappa\in[10.6197,11.643),}
\]

and the exact interval on which the three nonnesting inequalities persist simultaneously is

\[
\boxed{\kappa\in[10.6197,11.01).}
\]

## 4. Finite modular traps

The canonical eight-state set

\[
C_8=
\left\{
1/13,3/13,4/13,5/11,6/11,9/13,10/13,12/13
\right\}
\]

is forward-invariant modulo the terminal set. Its maximum portal height is \(13\), and therefore

\[
\boxed{V_5(7/260)=\infty.}
\]

The finite atlas for denominator bound \(500\) contains exactly:

- 76,094 nonterminal rational states;
- 109,254 directed nonterminal edges;
- 23,176 SCCs;
- 153 SCCs closed modulo the terminal set;
- 1,502 exact finite forward-invariant closures.

These counts certify the finite atlas only. They do not by themselves constitute a global classification of all traps.

## 5. Large computer-assisted results

The depth-five search has produced an exact 212-step witness ending at

\[
\frac{1350416}{1350417}.
\]

A rigorous lower bound gives

\[
\boxed{179\le\tau_5\le212.}
\]

A Bellman ladder has been certified along a long suffix of the 212-step witness. These computations use exact integer arithmetic, viability bounds, canonical state encodings, and independent cross-checks.

The repository does **not** currently claim \(\tau_5=212\).

## 6. Hidden-state program

The research program contains exact evidence that visible portal height is not a sufficient value coordinate and that Farey/\(10\)-adic information can alter future control decisions.

The strongest hidden-state claims are currently treated as a separate research line from Paper I. They require a more general theorem and a sharper literature comparison before becoming the headline claim of a submission.

## 7. Context semantics

The prime-wise reduction ledger is exact. However, the global structure has **not** been proved to form an orthomodular lattice or orthomodular poset.

Canonical terminology at this stage is:

> **orthocomplemented contextual prime-wise budget semantics**

See [Context semantics boundary](theorems/context-semantics-boundary.md).

## 8. Superseded but retained results

The earlier 217-step depth-five witness remains mathematically valid as a local construction but is superseded as a global upper bound by the 212-step witness.

Historical results are not deleted when superseded. Their status is explicitly downgraded.

## 9. Current publication boundary

### Paper I can claim

- exact rational radix–Möbius semigroup definition;
- exact benchmark first-hit times through depth four;
- three consecutive nonnesting counterexamples;
- exact threshold robustness intervals;
- exact computational protocol and evidence boundary.

### Paper I should not claim

- a solved value of \(\tau_5\);
- a complete trap classification over all denominators;
- a complete theory of hidden \(p\)-adic control;
- a proved global orthomodular structure;
- physical, quantum, cosmological, or natural-science implications.

## 10. Current strongest research opportunities

1. Infinite-family trap theorem.
2. Basin classification for finite traps.
3. General hidden-state/Farey control theorem.
4. Base-\(B\) classification of nonnesting.
5. Exact completion or improvement of the depth-five global bound.
6. Independent clean-room replication.
