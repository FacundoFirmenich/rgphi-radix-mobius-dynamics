# Paper I omnibus branch audit — 29 October 2026

## Verdict

The 120 MB omnibus package is **not a third canon**. It combines a Paper I
freeze, historical handoffs, an old repository snapshot, experimental branches
and many transport duplicates.

Primary line:

\[
\boxed{\texttt{rgphi-radix-mobius-dynamics/main}}
\]

Secondary role of the omnibus:

\[
\boxed{\texttt{PROVENANCE\_OMNIBUS + EXPERIMENTAL\_GENEALOGY}}
\]

## Integrity and duplication

- outer ZIP: PASS;
- 32 nested ZIPs: PASS;
- 57-page document QA: PASS;
- historical worktree checks: PASS;
- 463 file instances;
- 282 unique SHA-256 values;
- 172 duplicate groups;
- 181 redundant instances.

The package is valid but deliberately broad rather than deduplicated.

## Scientific deltas recovered

1. **HM-001** — foundational seven-hexagon patch, distributed holonomy and
   exact obstruction to one rigid global \(\mathbb Z_5\) phase.
2. **EO-001** — partial-observer atlas, four exact lifts, triple-cocycle
   obstruction and active refinement \(4\to2\to1\).
3. **BQ-009** — exact 31-symbol optimum for signed permutations on 16 supports;
   depth-three interval \(35\le M_3\le36\).
4. **ODT-008** — 44,280 exact outcomes and 272 hits; H2 PASS, O5
   PASS_WITH_ACTIVE_BRIER_BOUNDARY, O3 NO_PROMOTION.
5. **OMNI-002…008** — formal composite lineage retained as provenance; no RGΦ
   promotion.

## Conflicts

- The historical master claims ledger mixes the superseded
  \(179\le\tau_5\le212\) interval with the current
  \(186\le\tau_5\le212\) interval and repeats IDs. It must not replace the
  machine-readable canon.
- The earlier MULTIFRONT-004 ODT-008 report is superseded by the later canonical
  ODT-008 bundle.
- The 57-page superdocument is a useful synthesis but concatenates previous
  canons and is not a source of truth.
- The historical git bundle is provenance, not a competing public history.

## Canonical effect

No mainline result changes:

\[
\tau_1=45,\quad\tau_2=85,\quad\tau_3=120,\quad\tau_4=162,
\]

\[
186\le\tau_5\le212,
\qquad
V_5(x_t)=212-t\quad(89\le t\le212).
\]

Stage B2 was not executed and the 19.7 GB checkpoint payload was not recovered.
Paper I theorem content is unchanged. Every imported delta remains
`EXPERIMENTAL_ISOLATED`.

## Archival policy

Commit compact reports and genealogy to Git. Publish full bundles, datasets,
trees and figures as GitHub Release/Zenodo assets using the recorded SHA-256
identities. Do not duplicate wrappers, stale ledgers or superseded reports.
