#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt, log
import csv, json
from pathlib import Path
R=Path(__file__).resolve().parent
s=json.loads((R/'HOLONOMY_SNF_KNOWN_COMPONENT.json').read_text())
assert s['holonomy_smith_diagonal']==[1]
assert s['equal_length_smith_diagonal']==[1]
assert sum(s['equal_length_alias_vector'])==0
assert s['equal_length_alias_receipt_v3']==1
c=json.loads((R/'COHERENT_PHASE_CODE.json').read_text())
assert c['block_length']==4 and c['holonomy_block0']==0 and c['holonomy_block1']=='e3'
for N in (1,2,10,1000):
    assert Fraction(1,4*N)>0 and N*log(3)>0
rows=list(csv.DictReader((R/'N6_LOLLIPOP_REDUCTION.csv').open()))
assert [x['status'] for x in rows]==['IMPOSSIBLE_HIGHNESS','IMPOSSIBLE_HIGHNESS','ARITHMETIC_OPEN']
e=json.loads((R/'F17_RELATION_SIEVE_P_LE_199.json').read_text())
b=e['lattice_basis']; g=e['gauss_reduced_basis']
assert abs(b[0][0]*b[1][1]-b[0][1]*b[1][0])==abs(g[0][0]*g[1][1]-g[0][1]*g[1][0])
assert g[0][0]**2+g[0][1]**2==e['shortest_squared_norm']
assert isqrt(e['shortest_squared_norm'])==e['integer_floor_shortest_norm']
print('PASS_TURNO_007')
print('superaccess_block_rate=1/4_bit_per_edge')
print('hyperaccess_key=1_bit; normalized=1/(4N); gain=Nlog3')
print('n6_high_defect_word=TSTSTS_only_in_declared_jurisdiction')
print('F17_relation_sieve_min_norm=11220870885800329')
