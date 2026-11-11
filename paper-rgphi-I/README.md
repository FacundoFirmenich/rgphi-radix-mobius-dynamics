# RGΦ I — pre-submission RC1

**External title:** *Primitive projective radix–Möbius dynamics: content cocycles and a sharp rigidity threshold*  
**Internal provenance:** Paper III / Rounds 012–022  
**RC1 audit date:** 2026-11-11  
**Status:** `RC1_INTERNAL_AUDIT_PASS / GO_WITH_EXTERNAL_GATES / NOT_SUBMITTED`

RGΦ I is the first mathematics paper intended for external publication from the RGΦ programme. It is not the older benchmark/Bellman manuscript under `paper/`; that manuscript remains separate.

## Frozen mathematical arc

1. primitive projective lift of the rational radix–Möbius system;
2. exact content cocycle and cycle spectral identity;
3. high-cycle reduction budget and general rigidity criteria;
4. permutation rigidity for every high closed SCC of cardinality at most four;
5. an exact nonpermutational five-state counterfamily for an infinite arithmetic progression of bases;
6. sharp minimal nonpermutation cardinality equal to five;
7. finite defect-decorated type decomposition at fixed cardinality;
8. universal CRT fibre theorem for a fixed primitive state tuple.

## RC1 adversarial audit

The pre-submission audit found twelve major issues and resolved all twelve. The principal corrections were:

- one canonical labelling across article, supplement, CSV, JSON, Python and C++;
- a new symbolic lemma proving global uniqueness of the strict edge in the four-state proof;
- explicit proofs of the four-state normal-form reduction and forced alternate maps;
- explicit quotient bounds and gcd/parity arguments in the conic elimination;
- precise partial-domain formulation;
- corrected MSC classification and nearest-prior-art framing;
- removal of a non-substantive toy checker;
- one-command `make verify` and `make pdf` workflows.

## RC1 identities

- Main article PDF SHA-256: `79520c306ec3c0cd1647859982fc157b441118410a1a29e9052dc2dd8483daad`
- Supplement PDF SHA-256: `c73449d51e98d7ee80ed2e200493997f738e61b05c6ebafd7529f0b558914f9e`
- Full RC1 bundle SHA-256: `c93e52391b5fd6e81636e45a1573d90c70cfdf31a2f38999dfd0954d14f67aac`
- RC1 source/audit archive SHA-256: `2e6825639b56a9547cab8b7716a75cae8e6c451673965d86b63ab9a722e071da`

## Explicit exclusions

The article does not claim the twenty-form arithmetic classification, elliptic relative-integral programme, six-state catalogue, Bellman targets, or a physical interpretation. Those are later papers.

## Binding external gates

- author metadata confirmation;
- written adversarial review by Daniel Barraco;
- independent arithmetic-dynamics review;
- independent clean-room compilation and replay;
- final MathSciNet/zbMATH priority chaining;
- immutable arXiv/Zenodo release;
- journal submission.
