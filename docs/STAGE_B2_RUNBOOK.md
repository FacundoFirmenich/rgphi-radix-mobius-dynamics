# RGΦ Stage B2 production runbook

## Scientific objective

Continue the exact complete level envelope from the certified Stage-A frontier at global time 185 through time 211.

- Any hit at times 186–211 gives a new exact upper bound below 212.
- No hit through time 211 proves \(\tau_5=212\).
- Together with the complete first-divergence cut, a no-hit result promotes the Bellman ladder to \(0\le t\le212\).

## Input identity

The run must start from exactly:

- 2,462,600,671 states;
- 128 raw buckets `b0000.bin` … `b0127.bin`;
- 19,700,805,368 bytes;
- little-endian `uint64`, key `(a << 32) | b`;
- partition `SplitMix64(key) & 127`;
- hash-manifest SHA-256
  `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

The lightweight Stage-A bundle contains the manifest and hashes, not these 19.7 GB of payloads.

## Locate the checkpoint

```bash
scripts/stage_b2/locate_checkpoint.sh /mnt /srv /data /home /root
```

A valid candidate reports 128 buckets. Its byte total must then pass the validator.

## Validate

Hash-level validation:

```bash
python scripts/stage_b2/validate_checkpoint.py /path/to/checkpoint \
  --hash-manifest data/stage_b2/RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt \
  --mode hash --output CHECKPOINT_READINESS.json
```

Full structural validation additionally checks strict sorting, uniqueness, primitiveness, and bucket partition:

```bash
python scripts/stage_b2/validate_checkpoint.py /path/to/checkpoint \
  --hash-manifest data/stage_b2/RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt \
  --mode full --output CHECKPOINT_READINESS_FULL.json
```

## Storage

The source alone is 19.7 GB. A level can require source, raw sorted runs, merge intermediates, and destination simultaneously.

- less than 100 GiB free: runner refuses by default;
- 200 GB: potentially viable with deletion discipline;
- 400 GB: recommended.

## Execute

```bash
export RGPHI_CHECKPOINT_ROOT=/path/to/checkpoint-parent
export RGPHI_WORK_ROOT=/path/to/large-fast-volume/rgphi-stage-b2
export RGPHI_JOBS=4
export RGPHI_MERGE_JOBS=4
scripts/stage_b2/run_stage_b2.sh
```

The runner:

1. validates all 128 source hashes;
2. compiles the exact C++ worker/merger;
3. creates destination-partitioned sorted runs;
4. checks the portal before every pruning operation;
5. applies only terminal and rigorous remaining-time viability pruning;
6. performs exact multiway merge and deduplication;
7. commits each level atomically;
8. writes per-level manifests and an append-only ledger;
9. stops with a hit receipt or a `NO_HIT_THROUGH_211` certificate.

Known finite-trap states may be supplied as an optional packed `--safe-bin`. Omitting this optional pruning is correctness-preserving but can increase the frontier.

## Smoke test

```bash
python scripts/stage_b2/smoke_test.py
```

The smoke test compiles the production binary, propagates a small exact 128-bucket frontier, and compares the result with an independent in-memory implementation.

## Interruption semantics

Only directories named `level_NNN` are committed levels. `level_NNN.tmp` is incomplete and may be removed and rebuilt. The previous committed source level is never deleted unless `--delete-previous-generated` is explicitly supplied.
