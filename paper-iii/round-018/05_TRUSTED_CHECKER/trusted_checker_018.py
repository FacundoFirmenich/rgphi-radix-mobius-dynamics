#!/usr/bin/env python3
from pathlib import Path
import csv,json,subprocess,sys,math
R=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(R/'03_MULTI_STRICT/checkers/trusted_checker_multi_strict_018.py')],check=True)
b=json.loads((R/'02_COUNTERGRAPH/FIXED_STATE_BASE_CLASS.json').read_text())
assert b['B0']==88011536665779 and b['modulus']==223336848698040
rows=list(csv.DictReader((R/'02_COUNTERGRAPH/SAME_GRAPH_SEARCH_Q1_LE_10000_D_LE_30000.csv').open()))
assert len(rows)==1 and rows[0]['A']=='406' and rows[0]['C']=='712'
s=json.loads((R/'04_SECONDARY_DF015_0015/METRICS.json').read_text())
assert s['admissible_divisor_candidates']==213800681 and s['first_cycle_survivors']==587 and s['second_cycle_survivors']==0
print('PASS_ROUND_018')
print('countergraph_base_class=PASS')
print('small_height_state_tuple_audit=UNIQUE_IN_JURISDICTION')
print('DF015_0015=OPEN_REDUCED')
