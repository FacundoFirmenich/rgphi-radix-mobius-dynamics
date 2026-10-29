# RGΦ Paper II — P2 PRIME-001

**Status:** `PASS_CANONICAL_PROOF_AUDIT_WITH_NEW_THEOREMS`  
**Authority:** Paper-II development branch; no modification of RGΦ mainline claims.  
**Canonical project boundary:** `186 <= tau_5 <= 212`; Stage B2 remains open.

## Paper thesis

Paper II studies the exact arithmetic lift obtained by propagating a primitive rational state and an oriented primitive Farey shadow through the same radix–Möbius branch matrix. Primitive reductions couple the visible state, the Farey defect, prime-wise budgets and a generally unbounded address phase.

Provisional title:

> **Farey-shadow lifts, prime-wise reduction budgets, and hidden control in a rational radix–Möbius semigroup**

## P2-01 material advances

1. **Exact one-step phase modulus.** In canonical coordinates, with `N=hB/g` and `L=gt+h alpha`, the full residue `L mod N` has exact period `N/gcd(g,N)` in `t`.
2. **Universal residue-controlled action flip.** For every `B>=2`, at `v_B=B/(B+1)` and defect-one shadows `c_t=(Bt+1)/((B+1)t+1)`, the lexicographic shadow compiler selects `T` iff `t=-1 mod B`, and `S` otherwise.
3. **Pure-sector address cylinders.** A pure maximal-cancellation word of length `n` determines one address cylinder modulo `B^n`.
4. **Finite-task information lower bound.** The certified 212/217 addresses agree modulo `10^146`, differ modulo `10^147`, and select opposite controls at step 147 from the same visible rational state. Any decoder factoring through only the first 146 digits fails on at least one member of the pair.
5. **Compiler scope refutation.** At `B=2`, visible state `3/4`, shadow `1`, and target `q(x)>4`, the compiler selects `T`, which is absorbing for the declared task, while `STTT` reaches `4/5`. Hence the witness compiler is not a universal Bellman-optimal policy.

## Retained exact results

- defect cocycle `Delta'=B Delta/(gk)`;
- canonical update in `(h,t)` coordinates;
- prime-wise ledger `e_p'=e_p+v_p(B)-v_p(g)-v_p(k)`;
- 74-edge finite germ anti-amplification audit, minimum derivative `18/5`;
- 440-state, 142-edge defect-one automaton;
- exact compilation of the certified 212- and 217-action witnesses;
- same-state control flip at `61913/88527`.

## Explicit non-claims

P2-01 does **not** claim:

- a new Farey map;
- an ergodic-theoretic natural extension;
- global invertibility or an invariant measure;
- global minimality of the Farey address;
- universal Bellman optimality of the compiler;
- `tau_5=212`;
- a physical hidden variable.

## Research object

The full verified local bundle is `RGPHI_P2_PRIME_001_BUNDLE.zip` with SHA-256:

```text
1643df64e5fd33fa94f57268c790b646437fa037423329948e366225ec5b3fb8
```

It contains the 12-page v0.2 manuscript, theorem/claim ledgers, exact evidence, independent verifier, source genealogy, reviewer-risk register, literature positioning and the preregistered P2-02 gate.

## Next gate

`P2-02 — COMPILER_SCOPE_AND_FINITE_TASK_MINIMALITY`

The next gate will freeze a finite exact corpus and classify the compiler action as uniquely Bellman-optimal, tied, suboptimal finite, or catastrophic. It will construct a task-relative Myhill–Nerode quotient and compare precision levels `t mod B^j` without promoting benchmark-specific behavior to a universal policy.
