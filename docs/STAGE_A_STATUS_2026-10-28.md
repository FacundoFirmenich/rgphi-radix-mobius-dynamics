# RGΦ GLOBAL-TRAP-CUT-088 — Stage A status

**Canonical date:** 28 October 2026

Stage A classified all 89 first divergences from the 212-action witness:

- 23 inadmissible alternatives;
- 4 immediate terminal alternatives;
- 3 finite-trap basin alternatives;
- 59 residual bulk sources.

The joint exact search found no depth-five portal through global time 185. Therefore:

\[
\boxed{186\le\tau_5\le212.}
\]

The prior public interval `179 <= tau_5 <= 212` is superseded.

## Certified checkpoint

- time: 185;
- states: 2,462,600,671;
- buckets: 128;
- bytes: 19,700,805,368;
- encoding: little-endian `uint64`, key `(a << 32) | b`;
- partition: `SplitMix64(key) & 127`;
- bucket-manifest SHA-256:
  `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

The lightweight evidence object contains the checkpoint identity, metrics and hashes. It does not contain the 19.7 GB bucket payloads.

## Active frontier

Stage B2 must propagate the complete exact envelope over times 186–211.

- a hit gives a shorter exact witness;
- no hit through 211 proves `tau_5 = 212` and completes the Bellman ladder along the witness from time 0 through 212.
