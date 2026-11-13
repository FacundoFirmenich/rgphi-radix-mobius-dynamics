#!/usr/bin/env python3
"""Read-only HA-005 resonance audit. Never writes to the canonical tree.

Usage:
  python check_ha005_resonance_watch.py --math-only
  python check_ha005_resonance_watch.py --canonical-root /path/to/main --resonance-root /path/to/resonance

The complete mode audits file integrity and reported partitions, NOT the
arithmetic elimination proof. Replay canonical certificate checkers separately.
"""
import argparse
import csv
import hashlib
import itertools
import json
import pathlib
import re
import zipfile

EXPECTED = {
    "ha004_high_survivors": 102,
    "profiles_with_component_nullstellensatz": 80,
    "component_certificates": 160,
    "finite_divisor_cases": 278,
    "residual_profiles": 22,
    "residual_direct_strip": 15,
    "residual_forced_zero_primitive": 7,
    "arithmetically_eliminated": 102,
    "minimal_rank2_2_3_jurisdiction_realizations": 0,
    "status": "CLOSED_GLOBAL_NO_GO",
}
FROZEN = {
    "origin-resonance/prospective/OR4_N6_HEXAGONAL_SIGNATURE.md": "3ecbbe9b43f2df7a30c7ee1041a954fddf982d18",
    "origin-resonance/prospective/OR5_FIVE_DEFECT_CELL.md": "002cb51dd108ce61869cab787c62e3cc2b1f0fac",
    "origin-resonance/prospective/OR19_N6_DEFECT_SPECTRUM.md": "7fc806667931e625fbe1bc1f9a7cfcea6da7c35a",
}


def verify_six_cycle_budget():
    admissible = []
    for t in range(1, 7):
        for s in range(1, 7 - t):
            for k in range(1, t + s + 1):
                for factors in itertools.combinations_with_replacement(range(2, 8), k):
                    product = 1
                    for f in factors:
                        product *= f
                    if product < (1 << min(t, s)):
                        admissible.append((t, s, factors))
    assert admissible
    assert max(len(item[2]) for item in admissible) == 2
    assert {item[2] for item in admissible if len(item[2]) == 2} == {(2, 2), (2, 3)}
    assert {item[:2] for item in admissible if len(item[2]) == 2} == {(3, 3)}
    assert {item[:2] for item in admissible if len(item[2]) == 1 and item[2][0] in (4, 5, 6, 7)} == {(3, 3)}
    return len(admissible)


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--math-only", action="store_true")
    ap.add_argument("--canonical-root", type=pathlib.Path)
    ap.add_argument("--resonance-root", type=pathlib.Path)
    args = ap.parse_args()
    n = verify_six_cycle_budget()
    print(f"PASS_EXACT_SIX_CYCLE_BUDGET admissible_profiles={n}")
    if args.math_only:
        return
    if args.canonical_root is None or args.resonance_root is None:
        ap.error("complete mode requires both --canonical-root and --resonance-root")
    canon = args.canonical_root
    resonance = args.resonance_root
    for path, sha in FROZEN.items():
        assert git_blob_sha((resonance / path).read_bytes()) == sha, f"frozen test changed: {path}"
    print("PASS_FROZEN_OR4_OR5_OR19")

    src = canon / "paper-iii/ha-005"
    summary = json.loads((src / "data/HA005_MINIMAL_RANK2_NO_GO_SUMMARY.json").read_text())
    assert summary == EXPECTED, "HA005 summary differs from certified snapshot"
    assert 839 == 383 + 354 + summary["profiles_with_component_nullstellensatz"] + summary["residual_profiles"]
    assert 102 == summary["profiles_with_component_nullstellensatz"] + summary["residual_profiles"]
    assert 22 == summary["residual_direct_strip"] + summary["residual_forced_zero_primitive"]
    output = (src / "checks/MASTER_VERIFY_OUTPUT.txt").read_text()
    for marker in ("PASS_HA005_PRIMARY", "PASS_HA005_INDEPENDENT", "PASS_HA005_AUXILIARY", "PASS_HA005_MASTER"):
        assert re.search(rf"(?m)^{marker}$", output), f"missing source-attested result: {marker}"
    print("PASS_REPORTED_PARTITION_AND_SOURCE_LOG (not independent proof replay)")

    bundle = src / "HA005_CHECKER_CERTIFICATE_BUNDLE.zip"
    checksum_line = (src / (bundle.name + ".sha256")).read_text().strip().split()
    assert len(checksum_line) == 2 and checksum_line[1] == bundle.name
    assert hashlib.sha256(bundle.read_bytes()).hexdigest() == checksum_line[0]
    with zipfile.ZipFile(bundle) as archive:
        assert archive.testzip() is None, "archive CRC failed"
    print("PASS_ARCHIVE_SHA256_AND_CRC (checkers inside not executed)")

    with (resonance / "origin-resonance/ledgers/ELLIPTIC_ALL_19_STATUS.csv").open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert [int(row["curve_n"]) for row in rows] == list(range(1, 20))
    assert all(row["smooth"] == "TRUE" and row["rational_origin"] == "[0:1:-1]" for row in rows)
    assert rows[16]["known_point_gcd_C_D"] == "23"
    assert rows[16]["coprime_integral_multiples"] == "OPEN_NOT_ENUMERATED"
    assert rows[18]["F19_arithmetic_admissibility"] == "OPEN_NO_ADMISSIBLE_WITNESS_ESTABLISHED"
    print("PASS_19_CURVE_CONTINUITY_AND_OPEN_BOUNDS")

    with (resonance / "origin-resonance/ledgers/CYCLE_CONTENT_RECEIPTS_5STATE.csv").open(newline="") as fh:
        cycles = list(csv.DictReader(fh))
    assert len(cycles) == 6
    assert sum(int(row["Delta"]) == 3 for row in cycles) == 1
    strict = next(row for row in cycles if int(row["Delta"]) == 3)
    assert (strict["word_forward"], strict["m"], strict["log_radial_pitch"], strict["alpha_normalized"]) == (
        "TSTS", "4", "log(3)", "log(3)/(4*log(B_k))")
    assert all(row["log_radial_pitch"] == "0" and row["alpha_normalized"] == "0"
               for row in cycles if int(row["Delta"]) == 1)
    print("PASS_SIX_HISTORICAL_CYCLE_RECEIPTS")
    print("PASS_HA005_RESONANCE_DOCUMENTARY_CHECK; arithmetic no-go NOT independently replayed")


if __name__ == "__main__":
    main()
