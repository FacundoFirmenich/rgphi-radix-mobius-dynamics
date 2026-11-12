#!/usr/bin/env python3
"""Read-only, branch-scoped RC3.1 census-accounting audit.

Requires a Git clone containing the pinned canonical RC3.1 commit and the
resonance branch. It checks archived CSV/JSON consistency against historical
resonance receipts; it DOES NOT re-enumerate divisor universes, certify
mathematical proofs, modify 'main', or promote any canonical claim.
"""
import argparse
import csv
import hashlib
import io
import json
import math
import subprocess
from collections import Counter
from pathlib import Path

CANONICAL = "30c5a5242c8fdc1eab4e37ee807b7837780b2985"
RESONANCE = "research/origin-resonance-001"
PREFIX = "paper-iii/reviewer/rgphi-i-2026-11-11/rc3_1/certificates/"
CANONICAL_CSV_BLOB = "286f540cccf21bcda008454ebb69712da591aae4"
CANONICAL_SUMMARY_BLOB = "a36016d55f48952573fa5a69c606539a6d089df8"

parser = argparse.ArgumentParser()
parser.add_argument("--repo", default=".", help="local clone with both refs")
args = parser.parse_args()
repo = Path(args.repo).resolve()

def archived(ref, path):
    return subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{ref}:{path}"]
    )

def verify_git_blob(data, expected):
    calculated = hashlib.sha1(
        b"blob " + str(len(data)).encode() + bytes([0]) + data
    ).hexdigest()
    assert calculated == expected, (calculated, expected)

def parse_csv(data):
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))

raw = archived(CANONICAL, PREFIX + "exact_census_B2_60.csv")
summary_raw = archived(CANONICAL, PREFIX + "EXACT_CENSUS_B2_60_SUMMARY.json")
verify_git_blob(raw, CANONICAL_CSV_BLOB)
verify_git_blob(summary_raw, CANONICAL_SUMMARY_BLOB)
rows = parse_csv(raw)
summary = json.loads(summary_raw.decode())
prior = parse_csv(archived(
    RESONANCE, "origin-resonance/ledgers/RC3_B2_60_BOUNDED_WATCH.csv"
))
elliptic = parse_csv(archived(
    RESONANCE, "origin-resonance/ledgers/ELLIPTIC_ALL_19_STATUS.csv"
))
cycles = parse_csv(archived(
    RESONANCE, "origin-resonance/ledgers/CYCLE_CONTENT_RECEIPTS_5STATE.csv"
))
state = json.loads(archived(
    RESONANCE, "origin-resonance/ledgers/SURVEILLANCE_ENDPOINT_STATUS.json"
))

assert [int(r["B"]) for r in rows] == list(range(2, 61))
assert all(int(r["n"]) == 5 for r in rows)
assert len(prior) == len(rows) == 59
exact = [r for r in rows if r["method"] == "exact_divisor_universe"]
budget = [r for r in rows if r["method"] == "cycle_budget"]
coprime = [r for r in rows if math.gcd(int(r["B"]), 6) == 1]
redundant = [r for r in exact if math.gcd(int(r["B"]), 6) == 1]
excluded = [r for r in budget if math.gcd(int(r["B"]), 6) == 1]
assert len(coprime) == 19 and len(rows) - len(coprime) == 40
assert len(exact) == 47 and len(budget) == 12
assert len(redundant) == 7 and len(excluded) == 12
assert {int(r["B"]) for r in redundant} == {5, 7, 11, 13, 17, 19, 25}
assert {int(r["B"]) for r in budget} == {
    23, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59
}
assert sum(int(r["universe"]) for r in exact) == 2_210_941
assert sum(int(r["closed_scc"]) for r in exact) == 14
assert all(int(r["nonpermutation_scc_le_n"]) == 0 for r in rows)
assert all(r["universe"] == "" and r["closed_scc"] == "" for r in budget)
assert all(int(r["closed_scc"]) == int(r["closed_scc_le_n"]) for r in exact)
assert Counter(int(r["B"]) for r in exact if int(r["closed_scc"])) == Counter({
    7:1, 13:1, 16:1, 19:1, 21:1, 25:1, 36:1, 46:1, 57:1
})

for row, older in zip(rows, prior):
    assert row["B"] == older["B"] and row["method"] == older["method"]
    assert row["n"] == older["n"]
    if row["method"] == "exact_divisor_universe":
        assert int(row["universe"]) == int(older["candidate_universe_enumerated"])
        assert int(row["closed_scc"]) == int(older["closed_scc_enumerated"])
    else:
        assert older["closed_scc_count_authority"] == "NOT_ENUMERATED_CYCLE_BUDGET_ONLY"
        assert older["closed_scc_enumerated"] == ""
historical = {
    int(r["B"]): int(r["historical_B2_40_closed_scc"])
    for r in prior
    if r["B"] in {"29", "31", "37"}
}
assert historical == {29:1, 31:3, 37:2}
assert sum(historical.values()) == 6
assert 14 + sum(historical.values()) == 20  # lower bound, NOT global census

assert summary["bases"] == 59
assert summary["mathematical_partition"] == {
    "symbolically_ruled_out_gcd_B_6_eq_1": 19,
    "remaining_bases": 40
}
assert summary["computational_methods"] == {
    "exact_divisor_universe_runs": 47,
    "redundant_exact_runs_inside_symbolic_set": 7,
    "cycle_budget_only": 12
}
assert summary["candidate_states_total_across_exact_runs"] == 2_210_941
assert summary["closed_scc_total_across_exact_runs"] == 14
assert summary["nonpermutation_scc_le_5"] == 0

assert [int(r["curve_n"]) for r in elliptic] == list(range(1, 20))
assert elliptic[16]["known_point_gcd_C_D"] == "23"
assert elliptic[16]["coprime_integral_multiples"] == "OPEN_NOT_ENUMERATED"
assert elliptic[18]["F19_arithmetic_admissibility"].startswith("OPEN")
assert len(cycles) == 6
assert Counter(int(r["Delta"]) for r in cycles) == Counter({1:5, 3:1})
strict = [r for r in cycles if int(r["Delta"]) == 3]
assert len(strict) == 1
assert (strict[0]["word_forward"], strict[0]["m"]) == ("TSTS", "4")
assert strict[0]["log_radial_pitch"] == "log(3)"
assert strict[0]["alpha_normalized"] == "log(3)/(4*log(B_k))"

six = state["six_state"]
assert six["OR4_DUAL_TRIAD"] == "NOT_TRIGGERED"
assert six["OR4_ALTERNATING_HEXAGON"] == "NOT_TRIGGERED"
assert six["OR5_SHORT_DEFECT_CYCLE"] == "NOT_TRIGGERED_FOR_N_GE_6"
assert six["OR19_preregistered_defects"] == [2, 3, 4, 5, 6, 7]
assert six["OR19_realized_defects"] == "NOT_ENUMERATED"
assert state["structural"]["general_hyperaccess_identification"] == "NOT_CLAIMED"

print("PASS branch-only RC3.1 accounting: 59=19+40=47+12; overlap=7; candidates=2210941; enumerated SCC=14; historical SCC>=6; combined lower bound>=20")
print("UNCHANGED endpoints: OR4/OR5 NOT_TRIGGERED; OR19 NOT_ENUMERATED; elliptic F1..F19 and original six cycle receipts retained")
print("SCOPE: archived cross-check only; NOT full 47-base re-enumeration or independent proof certification")
