# Independent referee checklist

## Mathematical correctness

- [ ] Verify the branch formulae and exact gcd reduction laws.
- [ ] Verify `C_k = H A_k H^{-1}` and the projective conjugacy.
- [ ] Verify the content cocycle and determinant/trace identities.
- [ ] Verify the cycle reduction budget, including strict inequalities.
- [ ] Verify the cardinality and large-prime corollaries.
- [ ] Verify diameter-two rigidity.
- [ ] Verify that the four-state reduction exhausts all possible strict cycles.
- [ ] Verify the `TTSS` scale contradiction.
- [ ] Verify the forced closure pattern and descent in strict-`T` `TSTS`.
- [ ] Verify all quotient bounds in strict-`S` `TSTS`.
- [ ] Replay the 37-row nonsquare certificate independently.
- [ ] Verify all ten transitions and all gcd factors in the five-state family.
- [ ] Verify generalized CRT compatibility and arithmetic progression.
- [ ] Verify strong connectivity and noninjectivity.
- [ ] Verify the fixed-cardinality defect bound and finite-type theorem.
- [ ] Verify the universal CRT-fibre theorem.

## Exposition and novelty

- [ ] Is the object definition mathematically natural rather than merely notational?
- [ ] Is the sharp threshold theorem stated at the strongest justified level?
- [ ] Is the relation to radix dynamics, continued fractions and matrix cocycles accurate?
- [ ] Are physical analogies sufficiently restrained?
- [ ] Are any priority/literature claims missing or overstated?
- [ ] Is the main paper better as one article, or should a theorem be split off?

## Reproducibility

- [ ] Run `python3 code/check_publication.py` in a clean environment.
- [ ] Recompile main paper and supplement from source.
- [ ] Independently reconstruct the nonsquare residues.
- [ ] Independently reconstruct at least the base `t=0` action table.
- [ ] Compare produced hashes with the manifest.
