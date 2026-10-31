# HDH constitutive-kernel branch

**Authority:** `EXPERIMENTAL_ISOLATED`

HDH studies constitutive laws under exact coarse-graining. It does not modify RGΦ
mainline, Paper I or the first-hit chronology, and does not establish physical,
gravitational, cosmological or ontological dynamics.

## Scientific genealogy and currently audited frontiers

| Gate | Scoped result | Status |
|---|---|---|
| HDH-013 | scalar local/spectral closure fails on defective holdouts; full positive kernel closes under Schur/Kron reduction | VERIFIED_INTERNAL |
| HDH-014–030 | constitutive-memory, causal and nonsmooth investigations; historical ancestry retained in private original bundles | HISTORICAL/SCOPED |
| HDH-031 | integration of Schur inverse, memory derivative and rectangular typed contraction in Lean | FORMAL_CI_PASS |
| HDH-032 | retained-basis transport covariance in Lean | FORMAL_CI_PASS |
| [HDH-033-V2](gates/HDH-033-V2.md) | corrected conditional spectral bound; repaired public challenge and fresh 768-set internal reference | PASS_WITH_EXTERNAL_AND_PDE_HOLDS |
| [HDH-034](gates/HDH-034-REPAIR-AND-EXTERNALITY.md) | independent executor and derivation/refutation of specific PDE/FEM estimate | OPEN |

The complete proof of the **conditional** norm estimate is
[HDH-033-V2-ENERGY-PROOF.md](HDH-033-V2-ENERGY-PROOF.md).
Public-safe ZIP/source identities and private-custody exclusions are in
[HDH-033-V2-PUBLIC-ASSETS.json](HDH-033-V2-PUBLIC-ASSETS.json).

## Critical boundaries

- The moving-interface FEM modewise `O(h² (jk)^(3/2))` estimate is a
  **hypothesis**, not derived from the audited PDE/discretization.
- The three-family 768-set experiment is same-genealogy **internal**
  validation; it is not an independent second-team result.
- The historical HDH-033 integral bundle includes private custodian data in a
  nested parent and **must not be publicly released**.
- The repaired public release and the confidential new V2 custody are
  physically separated. Do **not** commit either seed values or private
  expected outputs to GitHub or arXiv.
- The repaired source candidates are **not deposited on arXiv** and have no DOI.
- A byte-identical retained-basis covariance source now passes a **fresh**
  GitHub Lean 4.35.0/Mathlib v4.35.0 `lake build --wfail` under
  `research/experimental/hdh033_v2_formal/`. This covers only the
  inherited covariance theorem, not the new spectral bound or the PDE gate.

The full patched source bundles are separately available as SHA-256-identified
public release assets. Git stores compact scoped claims and governance, not
historical duplicate ZIPs or private payloads.