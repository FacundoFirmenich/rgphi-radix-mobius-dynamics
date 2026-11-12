#!/usr/bin/env python3
"""RC3 branch-only watch receipt integrity: no execution of upstream full census, no claim promotion."""
import csv, json, math
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
def read(name):
    with (root / 'ledgers' / name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

new = read('RC3_B2_60_BOUNDED_WATCH.csv')
old = read('OR20_FIXED_BASE_2_40_MONODROMY.csv')
watch = json.loads((root / 'ledgers' / 'SURVEILLANCE_ENDPOINT_STATUS.json').read_text(encoding='utf-8'))
assert [int(r['B']) for r in new] == list(range(2, 61))
exact = [r for r in new if r['method'] == 'exact_divisor_universe']
budget = [r for r in new if r['method'] == 'cycle_budget']
assert len(exact) == 47 and len(budget) == 12
assert sum(int(r['candidate_universe_enumerated']) for r in exact) == 2210941
assert sum(int(r['closed_scc_enumerated']) for r in exact) == 14
assert all(int(r['nonpermutation_scc_le_5']) == 0 for r in new)
assert all(math.gcd(int(r['B']), 6) == 1 for r in budget)
assert all(not r['candidate_universe_enumerated'] and not r['closed_scc_enumerated'] for r in budget)
assert all(r['closed_scc_count_authority'] == 'NOT_ENUMERATED_CYCLE_BUDGET_ONLY' for r in budget)

historical = {}
for row in old:
    B = int(row['B'])
    historical[B] = historical.get(B, 0) + 1
    states = [Fraction(v) for v in row['states_sorted'].split('|')]
    Ts = [int(v) for v in row['T_targets'].split('|')]
    Ss = [int(v) for v in row['S_targets'].split('|')]
    assert len(states) == len(Ts) == len(Ss)
    for i, x in enumerate(states):
        p, q = x.numerator, x.denominator
        yT = Fraction((B*p) % q, q)
        z = Fraction(q-p, p)
        yS = Fraction(1, 1 + Fraction((B*z.numerator) % z.denominator, z.denominator))
        assert yT == states[Ts[i]] and yS == states[Ss[i]], (B, x)

for row in new:
    B = int(row['B'])
    if B <= 40:
        assert int(row['historical_B2_40_closed_scc']) == historical.get(B, 0)
        if row['method'] == 'exact_divisor_universe':
            assert int(row['closed_scc_enumerated']) == historical.get(B, 0)
assert len([r for r in exact if int(r['B']) <= 40]) == 34
skipped = {int(r['B']): historical.get(int(r['B']), 0) for r in budget}
assert {k:v for k,v in skipped.items() if v} == {29:1, 31:3, 37:2}
assert 14 + sum(skipped.values()) == 20
assert watch['canonical_head'] == 'b5fcdc4b50faedeae00de9fb46d04e3113295de1'
assert watch['newest_canonical_audit']['closed_scc_lower_bound_combined_sources'] == 20
assert watch['six_state']['OR4_DUAL_TRIAD'] == 'NOT_TRIGGERED'
assert watch['six_state']['OR5_SHORT_DEFECT_CYCLE'] == 'NOT_TRIGGERED_FOR_N_GE_6'
assert watch['six_state']['OR19_preregistered_defects'] == [2,3,4,5,6,7]
assert watch['six_state']['OR19_realized_defects'] == 'NOT_ENUMERATED'
assert len(read('ELLIPTIC_ALL_19_STATUS.csv')) == 19
assert len(read('CYCLE_CONTENT_RECEIPTS_5STATE.csv')) == 6
print('PASS RC3 branch surveillance: 59 base dispositions, 47 exact / 12 budget; 14 enumerated SCC + 6 known skipped SCC >= 20; OR4/OR5/OR19 frozen')
