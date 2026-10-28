# Scientific status

**Canonical date:** 28 October 2026  
**Repository status:** public pre-DOI release candidate  
**Primary manuscript:** *Nonnested extremal targets in a rational radix–Möbius semigroup*

This document is the authoritative high-level boundary between **proved**, **finite exhaustive**, **large computer-assisted**, **open**, and **superseded** statements in the repository.

## 1. Core dynamical system

For integer \(B\ge2\),

\[
T_B(x)=\{Bx\},\qquad
H(x)=\frac1{1+x},\qquad
S_B=H\circ T_B\circ H^{-1}.
\]

For reduced \(x=a/b\),

\[
q(x)=\frac{b}{b-a},
\qquad
P_m(B,\kappa)=\{x:q(x)>\kappa B^m\}.
\]

## 2. Closed symbolic results

For the appropriate branch digit \(d\),

\[
M_{T_B}(d)=
\begin{pmatrix}B&-d\\0&1\end{pmatrix},
\qquad
M_{S_B}(d)=
\begin{pmatrix}1&0\\-(B-1+d)&B\end{pmatrix},
\]

both with determinant \(B\).

For

\[
x_{N,r}=\frac{N}{N+r},\qquad s\equiv Br\pmod N,
\]

one has

\[
S_B(x_{N,r})=\frac{N}{N+s}.
\]

For reduced \(a/q\),

\[
\operatorname{den}(T_B^n(a/q))=\frac{q}{\gcd(q,B^n)}.
\]

## 3. Closed finite-exhaustive benchmark results

For \(B=10\), seed \(17/19\), \(\kappa=11\), and the repository terminal convention,

\[
\boxed{
\tau_1=45,\quad
\tau_2=85,\quad
\tau_3=120,\quad
\tau_4=162.
}
\]

The corresponding first-hit states fail nested optimality at three consecutive levels:

\[
45\to87>85,\qquad
85\to139>120,\qquad
120\to168>162.
\]

The exact common robustness interval for the four-level chronology is

\[
\boxed{\kappa\in[10.6197,11.643),}
\]

and the three nonnesting inequalities persist simultaneously throughout

\[
\boxed{\kappa\in[10.6197,11.01).}
\]

## 4. Finite modular traps

The canonical eight-state set

\[
C_8=\{1/13,3/13,4/13,5/11,6/11,9/13,10/13,12/13\}
\]

is forward-invariant modulo the terminal set and has maximum portal height 13. Therefore

\[
\boxed{V_5(7/260)=\infty.}
\]

The denominator-500 atlas contains exactly:

- 76,094 nonterminal rational states;
- 109,254 directed nonterminal edges;
- 23,176 SCCs;
- 153 SCCs closed modulo the terminal set;
- 1,502 exact finite forward-invariant closures.

These counts certify the finite atlas only, not a global classification theorem.

## 5. Large computer-assisted depth-five status

An exact 212-action witness reaches

\[
\frac{1350416}{1350417}.
\]

GLOBAL-TRAP-CUT-088 Stage A classified all 89 first divergences from that witness:

- 23 inadmissible alternatives;
- 4 immediate terminal alternatives;
- 3 finite-trap basin alternatives;
- 59 residual bulk sources.

The joint exact search over those residual sources found no portal through global time 185. Consequently,

\[
\boxed{186\le\tau_5\le212.}
\]

The exact frontier at time 185 contains 2,462,600,671 states in 128 sorted-unique buckets. Its payload size is 19,700,805,368 bytes and its bucket-manifest SHA-256 is

```text
dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7
```

The lightweight repository records the checkpoint identity and 128 hashes; it does not contain the raw 19.7 GB payloads.

The repository does **not** currently claim \(\tau_5=212\).

## 6. Active exact frontier: Stage B2

Stage B2 must propagate the complete exact level envelope from time 185 through time 211.

- Any hit gives a shorter exact witness.
- No hit through 211 proves \(\tau_5=212\).
- Together with the complete first-divergence classification, a no-hit result completes the Bellman ladder along the 212-action witness for \(0\le t\le212\).

The production runner, strict checkpoint validator, exact external-memory worker/merger, transactional runbook, and independent smoke test are stored under `scripts/stage_b2/` and `docs/STAGE_B2_RUNBOOK.md`.

Production remains blocked solely by the physical location of the 128 certified bucket payloads.

## 7. Hidden-state program

There is exact evidence that visible portal height is not a sufficient value coordinate and that Farey/\(10\)-adic information can alter future control decisions. These claims remain a research line distinct from Paper I and require sharper family-level theorems and literature closure.

## 8. Context semantics

The prime-wise reduction ledger is exact. A global orthomodular lattice or poset has not been proved. Canonical terminology remains:

> **orthocomplemented contextual prime-wise budget semantics**

## 9. Superseded but retained results

The earlier 217-action witness remains valid locally but is superseded globally by the 212-action witness. The earlier lower bound 179 is superseded by the exact Stage-A lower bound 186.

## 10. Publication boundary

### Paper I can claim

- the exact rational radix–Möbius semigroup;
- exact first-hit times through depth four;
- three consecutive nonnesting counterexamples;
- exact threshold-robustness intervals;
- the exact computational protocol and evidence boundary.

### Paper I should not claim

- a solved value of \(\tau_5\);
- a complete trap classification over all denominators;
- a complete hidden \(p\)-adic control theorem;
- a proved global orthomodular structure;
- physical, quantum, cosmological, or natural-science implications.

## 11. Strongest current opportunities

1. Execute Stage B2 and close or improve \(\tau_5\).
2. Prove infinite-family trap and basin theorems.
3. Identify a minimal Markov-complete Farey/\(p\)-adic augmentation.
4. Classify base-\(B\) nonnesting and trap regimes.
5. Obtain independent clean-room replication of the large certificates.
