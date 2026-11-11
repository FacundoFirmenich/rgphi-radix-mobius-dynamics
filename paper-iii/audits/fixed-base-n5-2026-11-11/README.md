# Fixed-base high-state audit — bounded, verified source archive

Date: 2026-11-11. Scope: Paper III auxiliary exact arithmetic audit; **not** a theorem-claim promotion.

## Jurisdiction and result

For each integer base 2 <= B <= 40 and cardinality at most 5, enumerate candidate reduced fractions p/q in (1/2,1) using the proven fixed-(B,n) divisor bound Omega(B,n) = B^(n-1) lcm(B^k-1 : 1 <= k <= n). Keep vertices with both T_B and S_B within that candidate set; compute strongly connected components and retain only fully closed components of size <= 5.

- Exactly 39 bases inspected; 890417 theorem-admissible candidate states considered.
- Exactly 16 closed components of size <= 5 identified in this window, all with bijective restrictions; maximum closed-component size = 2.
- No non-bijective component of cardinality <= 5 was observed for B in [2,40]. **No inference for B > 40**, and no assertion that the known CRT base is globally minimal.
- This finite base-window audit does not close the full five-state Diophantine classification.

## Source and replay

- `FIXED_B_N5_AUDIT_B2_40.csv` is an exact copy of the original 39-row output, including its non-reproducible wall-clock seconds. Original Git blob SHA-1: `6628d9b91a813ed4f4a4d429aaaf289d5d813ffe`; original SHA-256: `b06aa0b7296538571c1653b48d7398d5dc9c5796b54b4f226a1783a65263a87f`. Original line endings: CRLF.
- `fixed_B_n_audit_original.py` is the unchanged original source, Git blob SHA-1: `bf3453cd1a58f893092120bb820de1060638ec37`; SHA-256: `88c748b2d740b20c261c302336197988189d626dc6241f203122745598db7b53`.
- **Replayed:** the source function was run for B=2,...,38 with all five deterministic CSV fields exactly matching, and independently invoked at B=39,40 with the same five matching fields. The full script includes a later 41,...,50 extension; **that extension was not validated as part of this certificate**.
- Reproduction requires Python 3 and SymPy. Verify arithmetic columns, not `seconds`.

## Scientific boundary

The canonical Paper III version remains v1.13 and the controlling gate remains 023. The global five-state arithmetic realization, effective relatively integral-point enumeration, and six-state classification retain their prior OPEN/OPEN_PARTIAL authority.

A separate, unpromoted no-T/S-swap 1492-profile exploratory audit from the local RC2 working area was **not** synchronized as certified: its bundled `trusted_checker_five_state_defect_uniqueness.py` failed an assertion in the `S_FIBRE_INJECTIVITY` adjudication. Its arithmetic terminal exclusions therefore cannot be treated as verified by that checker. This bounded base audit neither uses nor validates those classifications.
