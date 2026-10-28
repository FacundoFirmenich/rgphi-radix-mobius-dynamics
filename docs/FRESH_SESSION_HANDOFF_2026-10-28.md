# RGΦ fresh-session handoff — 28 October 2026

## Read this first

The mainline question is:

\[
\text{Does a depth-five hit exist at a time }186\le t\le211,
\text{ or is }\tau_5=212?
\]

Do not restart from serial late-branch searches. Stage A already performed the global first-divergence reduction and exact search through time 185.

## Canonical facts

- System: \(T_B(x)=\{Bx\}\), \(H(x)=1/(1+x)\), \(S_B=H\circ T_B\circ H^{-1}\).
- Benchmark: \(B=10\), seed \(17/19\), \(\kappa=11\).
- Exact: \(\tau_1=45,\tau_2=85,\tau_3=120,\tau_4=162\).
- Open: \(186\le\tau_5\le212\).
- Exact witness: 212 actions, endpoint \(1350416/1350417\).
- Bellman suffix: \(V_5(x_t)=212-t\) for \(89\le t\le212\).
- Stage A partition: \(23+4+3+59=89\).
- No hit through time 185.

## Required Stage-B2 input

- 128 files `b0000.bin` … `b0127.bin`;
- total 19,700,805,368 bytes;
- 2,462,600,671 packed primitive states;
- little-endian `uint64`, key `(a<<32)|b`;
- bucket rule `SplitMix64(key)&127`;
- manifest hash:
  `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

The payloads were not located in the previous execution environment. Do not substitute a historical September checkpoint.

## Commands

```bash
scripts/stage_b2/locate_checkpoint.sh /mnt /srv /data /home /root

python scripts/stage_b2/validate_checkpoint.py /path/to/checkpoint \
  --hash-manifest data/stage_b2/RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt \
  --mode full \
  --output CHECKPOINT_READINESS_FULL.json

export RGPHI_CHECKPOINT_ROOT=/path/to/checkpoint-parent
export RGPHI_WORK_ROOT=/large/volume/rgphi-stage-b2
export RGPHI_JOBS=4
export RGPHI_MERGE_JOBS=4
scripts/stage_b2/run_stage_b2.sh
```

Use at least 100 GiB free; 400 GB is recommended.

## Trust conditions

- target check before pruning;
- exact rational arithmetic only;
- no beam, sampling or probabilistic membership;
- level-local deduplication, not historical-state suppression;
- transactional commit of all 128 destination buckets;
- previous level retained until verification;
- immediate hit receipt;
- final no-hit certificate only after time 211 is complete.

## Branch authority

U5-HD/HM/BQ/ODT remains `EXPERIMENTAL_ISOLATED`. RGΦ-GEN and Artin–Kummer remain parallel. They may not alter the canonical interval or interpret the benchmark physically.

## Paper I

Paper I may proceed independently. It claims exact nonnested first-hit targets through depth four and robustness intervals. It must not claim a resolved \(\tau_5\), global trap classification or physical implications.

## Stop conditions

If the payloads remain unavailable:

- preserve the blocker receipt;
- do not infer Stage B2;
- either recover the original data or preregister a full regeneration from the 59 residual sources;
- keep the interval \(186\le\tau_5\le212\).
