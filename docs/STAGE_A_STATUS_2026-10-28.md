# RGΦ GLOBAL-TRAP-CUT-088 — Stage A status

**Canonical date:** 28 October 2026  
**Authority:** `CANONICAL_ACTIVE / COMPUTER_ASSISTED_LARGE`  
**Compact evidence integrated:** 29 October 2026

Stage A classified all 89 first divergences from the 212-action witness:

- 23 inadmissible alternatives;
- 4 immediate terminal alternatives;
- 3 exact finite-trap basin alternatives;
- 59 residual bulk sources after the denominator-10,000 trap cut.

The joint exact search found no depth-five portal through global time 185. Therefore:

\[
\boxed{186\le\tau_5\le212.}
\]

The historical interval `179 <= tau_5 <= 212` is superseded.

## Structural cut

The three newly certified finite basins begin at:

- `4/9` at divergence depth 7;
- `5/16` at divergence depth 9;
- `1/14` at divergence depth 4.

Their exact closures and complete child tables are recorded in
`data/stage_a/RGPHI_EXACT_FIRST_DIVERGENCE_TRAPS.csv`.

## Multiscale trap-atlas evidence

| denominator bound | states | edges | SCCs | closed SCCs | safe SCCs | safe states |
|---:|---:|---:|---:|---:|---:|---:|
| 500 | 76,094 | 109,254 | 23,176 | 153 | 1,502 | 1,624 |
| 2,500 | 1,899,856 | 2,735,455 | 565,564 | 248 | 5,483 | 5,933 |
| 5,000 | 7,600,436 | 10,944,352 | 2,255,011 | 314 | 9,672 | 10,418 |
| 10,000 | 30,397,464 | 43,771,910 | 9,009,037 | 467 | 17,094 | 18,472 |

The denominator-10,000 audit has 467 closed SCCs, maximum SCC size 12. It
proves that none of the 59 residual first-divergence sources lies in a certified
finite trap contained in this denominator range. It does **not** prove that no
larger-denominator trap exists.

The exact theorem-family for finite traps remains the modular-skeleton theorem;
the multiscale atlas is a bounded, exhaustive audit rather than a global
classification of every rational trap.

## Search architecture

### Earliest-arrival stage

The 59 residual sources were injected at their true global times. The exact
first-arrival search reached time 171 with:

- 94,848,409 states in the frontier;
- 932,586,690 distinct states accumulated;
- zero portal hits.

At time 120, an independent implementation reproduced:

- 414,800 frontier states;
- 4,141,395 cumulative states;
- canonical frontier hash
  `7ff6d942f676d87528de8c495f0bb9354d58ec173096b181a55a9bba721facc6`.

### Complete level envelope

From the exact first-arrival frontier at time 171, the complete level envelope
was propagated through time 185, without subtracting historical revisits. The
final frontier has:

- 2,462,600,671 states;
- maximum observed portal height 482,677 in the hybrid stage;
- zero hits.

## Certified checkpoint

- time: 185;
- states: 2,462,600,671;
- buckets: 128;
- bytes: 19,700,805,368;
- encoding: little-endian `uint64`, key `(a << 32) | b`;
- partition: `SplitMix64(key) & 127`;
- bucket-manifest SHA-256:
  `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

The public repository contains compact evidence, source, counts, hashes and
checkers. It does not contain the 19.7 GB bucket payloads.

## Verification status

The final branch-fusion audit reproduced:

- the Stage A compact verifier: `PASS`;
- the denominator-500 atlas exactly;
- the denominator-2,500 safe-state output byte-for-byte;
- complete closure of the supplied denominator-10,000 safe-state asset;
- the checkpoint manifest identity.

The full source bundle is recorded in `data/stage_a/ASSET_MANIFEST.md`.

## Active frontier

Stage B2 must propagate the complete exact envelope over times 186–211.

- a hit gives a shorter exact witness;
- no hit through 211 proves `tau_5 = 212` and completes the Bellman ladder along the witness from time 0 through 212;
- interruption preserves only the last complete checkpoint and its certified residual.

No Stage B2 conclusion is permitted without the verified 128-bucket payload.
