# Origin–Resonance · Turno 012 independent audit (2026-11-17)

**Authority:** \`SEPARATE_PROSPECTIVE_NO_CANONICAL_OVERRIDE\`.
**Source ref before this audit:** \`51737b553f1008761fbe33e9fd9045a468cc0133\` on \`research/origin-resonance-001\`.
**Canonical main observed:** \`c25857e53eea8585a4f10e0a5a42295a315151ec\` (unchanged).
**Connected FST snapshot:** \`FacundoFirmenich/sinus-math\` at \`a771a6115f31859587e2995c56d2c0802a9be9d5\` on both available branches; its observed Git tree contains **README.md only**. The README describes external FST machinery and 24 local regression tests, but those executables/receipts are **not available in the inspected connected commit**. No new FST mathematical certificate is inferred from that README.

## Exact independent checks

Executed locally on Python 3 with standard library only:

\`\`\`sh
python origin-resonance/turnos/turno-012/check_t012_independent.py
\`\`\`

Output:

\`\`\`text
PASS_T012_INDEPENDENT_FINITE_AUDIT
extremal_label=8 Amax(1000)=395 bits=9 Smax(1000)=197913 bits=18
ell=6 fibre_histogram={1: 994178, 2: 2899, 3: 8}
limiting_ambiguity_probability=685/117649
limiting_conditional_entropy_formula=0.005837332402614633262171 bits
limiting_fixed_key_cost_formula=0.005847854308123188048597 bits
scope=finite_exact_enumeration_and_high_precision_series_only
open=non_CFL,natural_boundary,nonuniform_sources,T013_complexity
\`\`\`

The arithmetic threshold for \`Amax\` is evaluated by **integer comparisons** \`343**j <= 10**ell\`, avoiding floating-point ambiguity in the floor. The same primitive label \`h=8\` realizes all length-wise thresholds in the tested range through \`8^t C(8*343^j)\`. The \`ell=6\` histogram enumerates all \(10^6\) literal decimal words and independently checks the reported fibre distribution. An additional 501 signed integers \`K=8+9z\`, \`-250<=z<=250\`, test the superaccess LCM identity for a declared overlapping family of erased-prime sets.

The rational ambiguity fraction is verified exactly as \(1-(342/343)^2=685/117649\). The entropy values are high-precision evaluations of the **stated limiting distribution formula**, not an independent proof of convergence of the empirical finite-length distribution to that law. The distinguishing entropy is \(H(J\mid H,\ell)\) for uniform fixed-length words; it is **not total word compression**, a universal constant, or an unconditional information-gain rate.

## Taxonomy and retained boundaries

- **SUPERACCESS:** reconstruct hidden internal arithmetic or subsystemic information; combined primitive channels can recover \(K\).
- **HYPERACCESS:** residual zero-error key choosing the exact literal representative in an observation fibre; fixed-length worst-case key \(\lceil\log_2 A_h(\ell)\rceil\). Vanishing normalized cost is compatible with a nonvanishing exact selection requirement.
- Normal form: \(w=8^t C(K_0\,343^j)\), \((j,t)\in\mathbb N_0^2\); exact-length fibre section is a finite staircase.
- Maximum at \(\ell=1000\): **395, not 394**; nine bits. Unknown length bounded by \(L=1000\): 197913 combinations, 18 bits, under the specified observation model. Without any length bound the uniform finite-key endpoint is impossible.
- Dimension 1 for known exact length and dimension 2 for bounded unknown length are conditional complexity dimensions, not physical dimensions.
- The non-context-free and natural-boundary assertions, optimal *temporal* complexity, higher-language conditioning, nonuniform/Markov source entropy, hexafacial FST/UMI composition, and universal residual codes are **not independently certified by this finite checker**. Their extant labels and jurisdictions are unchanged.
- Turno-010 competing geometries retain their stated input-conflict hold. Turno-011 non-linear Koch \(\tau(q)\) applies to the specified nonuniform self-similar measure, not automatically to the frozen single-ratio model. The corrected semidirect \(D_3\) six-face law does not establish a physical noncommutative or quantum realization.
- No RC28 independent prospective outcome or Ramanujan cross-program operator theorem was found in the inspected new changes. Post-hoc and negative labels remain in force.

## Endpoint decision

**Material branch evidence:** Turno 012 introduces exact FST fibre and inverse-complexity assertions; the present audit adds independent finite verification of selected numerical and constructive consequences. **Not a new canonical result:** \`main\` is untouched. **Turno 013 remains OPEN** for time complexity, nonuniform/Markov sources, FST/hexafacial composition, analytic-observer scope, higher languages, and universal coding.

This audit is an additive artifact on the separate resonance branch, not a restatement or amendment of Paper III.
