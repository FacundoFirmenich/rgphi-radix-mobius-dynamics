#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
CERT="$ROOT/data/certificates/paper-I"
BUILD="${TMPDIR:-/tmp}/rgphi-paper-I-exact"
rm -rf "$BUILD"
mkdir -p "$BUILD/reference"
unzip -q "$CERT/paper-I-profiles.zip" -d "$BUILD/reference"
g++ -O3 -march=native -std=c++20 "$CERT/continuation_bfs.cpp" -o "$BUILD/continuation_bfs"
run(){
  local a=$1 b=$2 q=$3 h=$4 p=$5 label=$6
  "$BUILD/continuation_bfs" "$a" "$b" "$q" "$h" "$p" "$label" "$BUILD/${label}.csv"
  diff -u "$BUILD/reference/${label}.csv" "$BUILD/${label}.csv"
}
run 128 129 1100 42 22 m1_to_m2
run 1202 1203 11000 54 25 m2_to_m3
run 11156 11157 110000 48 27 m3a_to_m4
set +e
"$BUILD/continuation_bfs" 11532 11533 110000 42 26 m3b_nohit_to162 "$BUILD/m3b_nohit_to162.csv"; s=$?; test "$s" -eq 1
diff -u "$BUILD/reference/m3b_nohit_to162.csv" "$BUILD/m3b_nohit_to162.csv"
"$BUILD/continuation_bfs" 11642 11643 110000 42 26 m3c_nohit_to162 "$BUILD/m3c_nohit_to162.csv"; s=$?; test "$s" -eq 1
diff -u "$BUILD/reference/m3c_nohit_to162.csv" "$BUILD/m3c_nohit_to162.csv"
set -e
python "$ROOT/scripts/paper_i/verify_receipt.py"
echo PASS_PAPER_I_FULL_EXACT_REPLAY
