#!/usr/bin/env python3
import csv,json
from pathlib import Path
R=Path(__file__).resolve().parent

c=list(csv.DictReader((R/'KNOWN_COMPONENT_CYCLES.csv').open()))
assert len(c)==6
assert sum(int(x['strict_cycle']) for x in c)==1
assert {x['word'] for x in c if x['strict_cycle']=='1'}=={'T S T S'}

s=list(csv.DictReader((R/'SIX_STATE_SKELETON_COUNTS.csv').open()))
assert len(s)==3
assert all(int(x['normalized_marked_skeletons'])==720 for x in s)
assert sum(int(x['normalized_marked_skeletons']) for x in s)==2160
assert sum(int(x['defect_decorated_profiles']) for x in s)==8640
assert {x['word']:int(x['alternating_hexagon_hits']) for x in s}=={'TTTSSS':0,'TTSTSS':0,'TSTSTS':720}
assert all(int(x['dual_triad_hits'])==0 for x in s)

j=json.loads((R/'F17_P_R_LOCAL_GLOBAL.json').read_text())
assert j['good_reduction_certificates']['7']['R_in_subgroup_P'] is False
assert j['good_reduction_certificates']['83']['log_R_base_P']==44
assert j['gcd_A_CplusD']==22873516239

h=json.loads((R/'KNOWN_ALIAS_HYPERACCESS.json').read_text())
assert h['uniform_path_entropy_bits']==1.0
assert h['uniform_terminal_entropy_bits']==1.0
assert h['full_word_observer_entropy_bits']==0.0

print('PASS_TURNO_006')
print('holonomy_rank_known_component=1')
print('equal_length_alias_rank=1')
print('relative_hyperaccess_alias=1_bit')
print('six_state_skeletons=2160; decorated=8640')
print('dual_triad_high_defect=0')
print('alternating_hexagon=TSTSTS_only')
print('R_not_integer_multiple_of_P=PASS_mod7')
