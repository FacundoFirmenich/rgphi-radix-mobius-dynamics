# Context-semantics formal boundary

## 1. Purpose

The RGΦ reduction bookkeeping naturally separates prime-wise choices between state reduction and context/Farey reduction.

Earlier internal work used the term “orthomodular” too broadly. The public repository adopts a stricter algebraic boundary.

## 2. Exact local structure

For each relevant prime \(p\mid B\), the local reduction-allocation mode records two coordinates:

\[
(s_p,\kappa_p),
\]

where \(s_p\) measures the exponent allocated to primitive state reduction and \(\kappa_p\) the exponent allocated to context reduction.

In the decimal squarefree one-unit case, the local binary choices form four modes with complement

\[
(s_p,\kappa_p)^\perp=(1-s_p,1-\kappa_p).
\]

This local four-element structure is Boolean.

For the two decimal primes \(2\) and \(5\), the direct local product yields sixteen elementary modes.

## 3. What is proved

- exact prime-wise budget update;
- local complement involution;
- Boolean structure of each elementary local block;
- exact computational context tracking;
- strong compression of many explicit context genealogies in finite audits.

## 4. What is not proved

The global collection of contexts has not been shown to possess:

- globally defined meet and join operations;
- an orthomodular-poset structure;
- an orthomodular-lattice structure;
- an effect-algebra or orthoalgebra structure satisfying all required axioms.

Local Boolean blocks do not imply a global orthomodular object.

## 5. Canonical terminology

Until a global theorem is established, use:

> **orthocomplemented contextual prime-wise budget semantics**

Avoid presenting “orthomodular dynamics” as a closed theorem.

## 6. Formalization program

Three candidate mathematical targets remain open.

### A. Orthomodular poset

Prove that the global pasted structure has a partial order, orthocomplement, and the required joins for orthogonal pairs, together with the orthomodular law.

### B. Orthoalgebra/effect algebra

Model context combination as a partial binary operation and prove the corresponding algebraic axioms.

### C. Contextual pasting of Boolean blocks

Retain only the blockwise Boolean structure and formalize compatibility/pasting without claiming a stronger global lattice.

## 7. Publication boundary

This line is not required for Paper I.

It should become a standalone mathematical claim only after:

1. the global carrier set is defined independently of implementation details;
2. operations are specified;
3. all axioms are proved or counterexamples identified;
4. the resulting structure is compared with the established literature.
