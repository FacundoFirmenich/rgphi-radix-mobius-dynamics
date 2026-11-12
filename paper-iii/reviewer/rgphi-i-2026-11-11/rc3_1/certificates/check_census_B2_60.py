import csv, math, json
from pathlib import Path

p = Path(__file__).with_name("exact_census_B2_60.csv")
rows = list(csv.DictReader(p.open()))
assert [int(r["B"]) for r in rows] == list(range(2, 61))

exact = [r for r in rows if r["method"] == "exact_divisor_universe"]
budget_only = [r for r in rows if r["method"] == "cycle_budget"]
coprime = [r for r in rows if math.gcd(int(r["B"]), 6) == 1]
redundant = [r for r in exact if math.gcd(int(r["B"]), 6) == 1]

assert len(rows) == 59
assert len(exact) == 47
assert len(budget_only) == 12
assert len(coprime) == 19
assert len(redundant) == 7
assert {int(r["B"]) for r in budget_only} == {23,29,31,35,37,41,43,47,49,53,55,59}
assert {int(r["B"]) for r in redundant} == {5,7,11,13,17,19,25}
assert sum(int(r["universe"] or 0) for r in exact) == 2_210_941
assert sum(int(r["closed_scc"] or 0) for r in exact) == 14
assert {int(r["B"]) for r in exact if int(r["closed_scc"] or 0) > 0} == {7,13,16,19,21,25,36,46,57}

for r in rows:
    assert int(r["nonpermutation_scc_le_n"]) == 0
    if r["method"] == "cycle_budget":
        assert math.gcd(int(r["B"]), 6) == 1
    else:
        assert r["N"] and int(r["universe"]) >= 0

print("PASS")
print("bases=2..60")
print("symbolically_excluded_coprime_to_6=19")
print("exact_divisor_universe_runs=47")
print("redundant_exact_runs_inside_symbolic_set=7")
print("cycle_budget_only=12")
print("candidate_states=2210941")
print("closed_scc=14")
print("nonpermutation_scc_le_5=0")
