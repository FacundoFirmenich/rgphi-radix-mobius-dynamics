#!/usr/bin/env python3
"""Branch-only integrity checker for resonance watch ledgers; no theorem promotion."""
import csv, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def rows(filename):
    with (root/'ledgers'/filename).open(newline='',encoding='utf-8') as handle:
        return list(csv.DictReader(handle))
curves=rows('ELLIPTIC_ALL_19_STATUS.csv')
assert len(curves)==19
assert [int(r['curve_n']) for r in curves]==list(range(1,20))
assert all(r['smooth']=='TRUE' and r['rational_origin']=='[0:1:-1]' for r in curves)
assert [int(r['curve_n']) for r in curves if r['uniform_slope_chamber_survey_H10000']=='ONE_HIT']==[17]
r17=curves[16]
assert r17['rank_Q_known']=='AT_LEAST_ONE' and r17['torsion_Q_known']=='TRIVIAL'
assert r17['known_point_gcd_C_D']=='23'
assert curves[18]['F19_arithmetic_admissibility'].startswith('OPEN')
cycles=rows('CYCLE_CONTENT_RECEIPTS_5STATE.csv')
assert len(cycles)==6
assert sum(int(r['Delta'])>1 for r in cycles)==1
strict=next(r for r in cycles if int(r['Delta'])>1)
assert (strict['m'],strict['Delta'],strict['strict_edges'])==('4','3','1')
assert strict['log_radial_pitch']=='log(3)'
assert strict['alpha_normalized']=='log(3)/(4*log(B_k))'
assert all(r['log_radial_pitch']=='0' and r['alpha_normalized']=='0' for r in cycles if int(r['Delta'])==1)
watch=json.loads((root/'ledgers'/'SURVEILLANCE_ENDPOINT_STATUS.json').read_text(encoding='utf-8'))
assert watch['six_state']['OR19_preregistered_defects']==[2,3,4,5,6,7]
assert watch['six_state']['OR4_DUAL_TRIAD']=='NOT_TRIGGERED'
assert watch['six_state']['OR5_SHORT_DEFECT_CYCLE']=='NOT_TRIGGERED_FOR_N_GE_6'
assert watch['canonical_branch']=='main'
print('RESONANCE WATCH PASS: 19 uniform curves, 6 exact five-state cycles, frozen prospective endpoints preserved')
