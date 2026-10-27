# RGΦ — Modular Trap Classification Theorem v1.0

## 1. Setting

Fix an integer base \(B\ge 2\). For \(x\in[0,1]\), define

\[
T_B(x)=\{Bx\},
\qquad
S_B=H\circ T_B\circ H^{-1},
\qquad
H(x)=\frac1{1+x},
\]

on the branch where \(S_B\) is admissible. Let \(E\) be a forward-invariant terminal set. A finite set \(F\subset \mathbb Q\cap(0,1)\setminus E\) is an **\(E\)-relative trap** when every admissible child of every \(x\in F\) lies in \(F\cup E\).

For a reduced rational \(x=a/q\), put

\[
Q(x)=\frac{q}{q-a}.
\]

The portal target is

\[
P_m(B,\kappa)=\{x:Q(x)>\kappa B^m\}.
\]

---

## 2. Radix denominator theorem

### Theorem 2.1

For every reduced \(a/q\) and every \(n\ge0\),

\[
T_B^n(a/q)
=
\left\{\frac{B^n a}{q}\right\},
\]

and the reduced denominator is

\[
\boxed{
\operatorname{den}(T_B^n(a/q))
=
\frac{q}{\gcd(q,B^n)}.
}
\]

### Proof

Before reduction, the numerator is the residue \(B^n a\bmod q\). Since \(\gcd(a,q)=1\),

\[
\gcd(B^n a,q)=\gcd(B^n,q).
\]

Reduction therefore removes exactly \(\gcd(q,B^n)\). ∎

---

## 3. Eventual modular cycle theorem

Write

\[
q=q_{\parallel}q_{\perp},
\]

where every prime factor of \(q_{\parallel}\) divides \(B\), while

\[
\gcd(q_{\perp},B)=1.
\]

Define

\[
\nu_B(q)=
\max_{p\mid B}
\left\lceil\frac{v_p(q)}{v_p(B)}\right\rceil.
\]

### Theorem 3.1

After at most \(\nu_B(q)\) applications of \(T_B\), the denominator is \(q_{\perp}\). If \(q_{\perp}>1\), the subsequent orbit is periodic with exact period

\[
\boxed{
\operatorname{ord}_{q_{\perp}}(B).
}
\]

If \(q_{\perp}=1\), the orbit reaches zero.

### Proof

The denominator formula gives

\[
q_n=q/\gcd(q,B^n).
\]

For \(n\ge\nu_B(q)\), all prime powers shared with \(B\) have been removed, so \(q_n=q_{\perp}\). Thereafter multiplication by \(B\) acts as a permutation of the invertible residue class of the numerator modulo \(q_{\perp}\). Since the numerator is invertible,

\[
B^k a\equiv a\pmod{q_{\perp}}
\iff
B^k\equiv1\pmod{q_{\perp}},
\]

and the least such \(k\) is \(\operatorname{ord}_{q_{\perp}}(B)\). ∎

---

## 4. Finite trap criterion

### Theorem 4.1 — Terminal-relative trap criterion

A finite set \(F\) is an \(E\)-relative trap if and only if, for every \(x\in F\),

\[
T_B(x)\in F\cup E
\]

and, whenever \(S_B(x)\) is admissible,

\[
S_B(x)\in F\cup E.
\]

This is an exact finite certificate requiring at most two child checks per state.

### Corollary 4.2 — Infinite portal value

Assume

\[
\max_{x\in F}Q(x)\le \kappa B^m
\]

and \(E\cap P_m(B,\kappa)=\varnothing\). Then every trajectory entering \(F\cup E\) before hitting the target remains outside the target forever. Consequently,

\[
\boxed{V_m(x)=\infty}
\]

for every state \(x\) whose target-free forward orbit is forced into \(F\cup E\).

---

## 5. Structural classification

### Theorem 5.1 — Modular skeleton classification

Every finite \(E\)-relative trap decomposes into:

1. finite \(T_B\)-preperiodic chains, on which the denominator loses prime powers shared with \(B\);
2. modular \(T_B\)-cycles of lengths \(\operatorname{ord}_{q_{\perp}}(B)\);
3. admissible \(S_B\)-edges coupling those chains and cycles;
4. terminal exits into \(E\).

Conversely, any finite union of complete \(T_B\)-forward components satisfying the \(S_B\)-closure condition modulo \(E\) is an \(E\)-relative trap.

### Proof

The map \(T_B\) is functional. Theorems 2.1 and 3.1 imply that every \(T_B\)-orbit consists of a finite denominator-stripping prefix followed by a modular cycle or zero. Hence the restriction of \(T_B\) to a finite trap is a union of preperiodic functional components. The only additional edges are the admissible \(S_B\)-edges. The trap criterion is exactly closure of this union under those edges modulo \(E\). The converse is immediate. ∎

---

## 6. Exact D≤500 audit

For base ten and the certified 23-state terminal set, the audit covered every reduced nonterminal rational with denominator at most 500.

- states: **76,094**;
- closed SCCs modulo terminals: **153**;
- exact finite forward closures: **1,502**;
- denominator-formula checks: **7,145,037**;
- modular \(T\)-cycle/order checks: **47**;
- closure edge checks: **11,056**;
- failures: **0**.

The audit establishes the theorem family independently of any particular portal horizon.

---

## 7. C8 as a mixed modular trap

The set

\[
C_8=
\left\{
\frac1{13},\frac3{13},\frac4{13},
\frac5{11},\frac6{11},
\frac9{13},\frac{10}{13},\frac{12}{13}
\right\}
\]

contains a six-cycle governed by

\[
\operatorname{ord}_{13}(10)=6
\]

and a two-cycle governed by

\[
\operatorname{ord}_{11}(10)=2.
\]

The admissible \(S\)-edges couple the two modular components without creating any nonterminal exit. Moreover,

\[
\max_{x\in C_8}Q(x)=13.
\]

Therefore, for the depth-five benchmark threshold \(1{,}100{,}000\),

\[
\boxed{V_5(7/260)=\infty.}
\]

---

## 8. Scope and next theorem

The classification theorem characterizes the internal anatomy of finite traps. The D≤500 atlas is complete only for closures whose nonterminal successors remain inside the enumerated denominator range.

The next global theorem should identify arithmetic conditions on a finite family of denominators and \(S_B\)-links that guarantee closure without a denominator bound. That would turn the current exact atlas into a parameterized infinite-family classification.
