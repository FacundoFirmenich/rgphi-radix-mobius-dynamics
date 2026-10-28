#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
: "${RGPHI_CHECKPOINT_ROOT:?Set RGPHI_CHECKPOINT_ROOT to the directory containing cur/b0000.bin..b0127.bin}"
: "${RGPHI_WORK_ROOT:?Set RGPHI_WORK_ROOT to a filesystem with at least 100 GiB free; 400 GiB is recommended}"
HASH_MANIFEST=${RGPHI_HASH_MANIFEST:-"$HERE/../../data/stage_b2/RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt"}
JOBS=${RGPHI_JOBS:-4}
MERGE_JOBS=${RGPHI_MERGE_JOBS:-4}
exec python3 "$HERE/run_stage_b2.py" \
  --checkpoint-root "$RGPHI_CHECKPOINT_ROOT" \
  --hash-manifest "$HASH_MANIFEST" \
  --work-root "$RGPHI_WORK_ROOT" \
  --start-time 185 --end-time 211 \
  --jobs "$JOBS" --merge-jobs "$MERGE_JOBS" \
  --minimum-free-gb 100
