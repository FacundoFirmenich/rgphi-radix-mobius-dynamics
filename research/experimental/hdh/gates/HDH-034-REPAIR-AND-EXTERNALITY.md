# HDH-034 — binding next gates after HDH-033-V2

**Authority:** EXPERIMENTAL_ISOLATED.

## Scientific theorem gate

Either derive the uniform modewise consistency estimate for a specified
elliptic moving-interface problem (geometry, trace spaces, velocity, P1 FEM,
transport and constants uniform in J), or supply a counterexample.
Current status: `OPEN_PDE_ASSUMPTION`. Abstract spectral summation is
conditional and does not establish this estimate.

## External blind gate

1. An independent executor verifies public ZIP/code/dependency hashes.
2. Before receiving hidden seeds, the executor submits its frozen code and
   environment receipt to an independent custodian.
3. The custodian releases exactly the 768 already committed new seed values.
4. The executor runs all three families without retuning, records hardware
   and failures, freezes the return ZIP and records its SHA-256.
5. The custodian checks frozen return against private expected outputs only
   *after* return freeze, preserving negative outcomes.
6. Only an independent report with provenance can upgrade externality;
   the 768-set same-genealogy internal technical reference cannot.

Status: `READY_FOR_EXTERNAL_ACTION`, not `PASS_EXTERNAL`.

## Packaging and arXiv

- No full historical parent in any public ZIP.
- Source packages compile twice in clean extracted trees; ancillary checks
  and relative SHA-256 manifests pass.
- Paper A requires specialist review of the uniform PDE estimate and theorem.
- Paper B remains a methods-note with an explicit externality HOLD.
- No arXiv submission, external specialist report, DOI or physical interpretation
  is claimed in this gate.

## Formal proof artifact

Inherited HDH-032 Lean CI status is PASS for the retained-basis covariance.
HDH-033-V2 includes pinned Lean/Mathlib source metadata but has not performed
a fresh `lake build` in this runtime (Lean unavailable). This is an
independent formal replay gate, not a reason to mislabel algebraic proof
status.

All HDH-032 frozen negative evidence, especially the raw square-root gate
failure, remains valid under its original jurisdiction.
