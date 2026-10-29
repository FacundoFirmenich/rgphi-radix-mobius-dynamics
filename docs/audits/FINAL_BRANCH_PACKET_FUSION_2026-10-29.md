# Final branch-packet fusion audit — 29 October 2026

## Scope

The final supplied packet contained:

- the complete `RGPHI-GLOBAL-TRAP-CUT-088` Stage A bundle;
- the HDH-013 constitutive-kernel bundle;
- a complete historical operational handoff;
- the Publication Deployment branch-fusion audit, matrix and hash receipt;
- a historical fused reviewer bundle.

## Authority decision

The public `main` branch remains the single canon. The packet contributes two
material deltas:

1. **Stage A exact evidence** — promoted to RGΦ mainline because it supplies the
   missing compact and bounded-exhaustive artifacts behind the canonical lower
   bound `tau_5 >= 186` and the D=10,000 trap cut.
2. **HDH-013** — integrated under `EXPERIMENTAL_ISOLATED`; it has no authority
   over RGΦ, Paper I, Stage B2 or physical interpretation.

All other packet components are provenance, already-integrated branch-fusion
material, duplicates, or historical reviewer artifacts.

## Stage A verification

The source bundle passed its internal manifest and compact verifier. The final
fusion audit independently reproduced:

- the D=500 trap atlas;
- the D=2,500 atlas and safe-state file byte-for-byte;
- the complete closure of the supplied D=10,000 safe-state set;
- the 89-source first-divergence partition;
- the t=120 cross-check;
- the no-hit envelope through t=185;
- the frontier-185 bucket-manifest identity.

The exact multiscale census is now committed as compact evidence. The complete
safe-state tables and the full bundle remain release assets.

## HDH-013 verification

The bundle manifest, primary run and independent checker pass. The audited
result is deliberately mixed:

- scalar local and scalar spectral closure fail on defective holdouts;
- the full positive kernel closes exactly under Schur/Kron reduction;
- composition, Green restriction, elimination-order independence and
  permutation covariance pass to machine precision;
- the causal-set benchmark validates its implementation but does not select the
  scalar graph susceptibility;
- no discrete Einstein equation is derived.

The exact kernel is promoted only as an RG-scale constitutive state within the
HDH model. HDH-014 is preregistered and open.

## Reviewer-bundle defect

The historical fused reviewer bundle has a valid outer ZIP hash but an invalid
internal `SHA256SUMS.txt`: paths retain the build-directory prefix and the
manifest hashes itself while being written. The current workflow inherited the
same pattern.

The workflow is corrected to:

- generate relative paths from inside the bundle directory;
- exclude `SHA256SUMS.txt` from its own manifest;
- unpack and verify the final ZIP before upload.

## Non-integrated material

- the historical operational handoff is preserved as provenance only;
- the branch-fusion audit/matrix were already integrated under PR #19;
- duplicate SHA receipts are not recommitted;
- the old reviewer ZIP is not a current review artifact;
- no checkpoint payload is present, so Stage B2 remains open;
- no claim of `tau_5=212` is made.

## Canon after fusion

\[
\tau_1=45,\quad \tau_2=85,\quad \tau_3=120,\quad \tau_4=162,
\]

\[
186\le\tau_5\le212,
\qquad
V_5(x_t)=212-t\quad(89\le t\le212).
\]

The final architecture is:

\[
\boxed{
\text{one public canon}
+
\text{exact Stage A evidence}
+
\text{bounded experimental branches}
-
\text{duplicate authority}
}
\]
