# RGΦ Round 019-A — global twenty-form catalogue at cardinality five

Let F be a five-state closed strongly connected component contained in the high domain (1/2,1), and suppose at least one of T_B|F or S_B|F is not a permutation.

## Theorem 019-A

Up to vertex relabelling and exchange of T and S, F belongs to exactly one of the twenty factor-specific normal forms DF015-0001,...,DF015-0020.

Equivalently, there are ten functional/fibre topologies, each paired with the only possible strict factors r=2 and r=3.

## Proof architecture

1. The cycle reduction budget forces every strict edge in cardinality five to have factor 2 or 3 and to lie on one of the four witness architectures TTSS, TSTS, TTSSS or TSTSS.
2. TTSS and TTSSS are globally impossible.
3. Round 018 proves that every nonpermutation five-state SCC has exactly one strict edge globally, not merely on the selected witness cycle.
4. With one global strict edge, the strict generator is a defect-one lollipop: its complement is a permutation, and the other generator is a permutation.
5. Exhaustive enumeration of all TSTS-plus-one and Hamiltonian-TSTSS closure assignments, followed by quotienting by labelled isomorphism and T/S duality, gives the twenty forms. Fibre closure and exact state-distinctness are part of the quotient.

The enumeration is finite in functional graph space; it is not a denominator or base scan.

## Arithmetic status

- Seven forms are globally impossible: DF015-0009, 0010, 0013, 0014, 0016, 0019, 0020.
- DF015-0007 contains the exact Round-017 family in branch B2; branch B1 remains open.
- The remaining twelve forms have no known realization and remain open.

Thus the combinatorial classification is complete, while arithmetic realizability is not.
