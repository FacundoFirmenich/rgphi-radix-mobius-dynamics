#!/usr/bin/env bash
set -euo pipefail
# Locate a complete Stage-A t=185 checkpoint on a local machine or mounted volume.
if [ "$#" -gt 0 ]; then
  ROOTS=("$@")
else
  ROOTS=(/mnt /srv /data /home /root)
fi
for root in "${ROOTS[@]}"; do
  [ -e "$root" ] || continue
  find "$root" -type f -name 'b0000.bin' -size +100M -print 2>/dev/null | while read -r f; do
    d=$(dirname "$f")
    n=$(find "$d" -maxdepth 1 -type f -name 'b????.bin' | wc -l)
    bytes=$(find "$d" -maxdepth 1 -type f -name 'b????.bin' -printf '%s\n' | awk '{s+=$1} END{print s+0}')
    if [ "$n" -eq 128 ]; then
      printf 'candidate=%s buckets=%s bytes=%s\n' "$d" "$n" "$bytes"
    fi
  done
done
