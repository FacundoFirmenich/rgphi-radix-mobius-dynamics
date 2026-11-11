#!/usr/bin/env python3
from pathlib import Path
import csv, json

R = Path(__file__).resolve().parent
m = json.loads((R / 'METRICS.json').read_text())
a = list(csv.DictReader((R / 'FORM_ADJUDICATION_20.csv').open()))
b = list(csv.DictReader((R / 'REMAINING_ARITHMETIC_BRANCHES.csv').open()))
assert len(a) == 20
assert sum(x['status'] == 'CLOSED_SYMBOLIC' for x in a) == 7
assert sum(x['status'] == 'OPEN_REDUCED' for x in a) == 13
assert len(b) == 15
assert {x['form_id'] for x in b} == {x['form_id'] for x in a if x['status'] == 'OPEN_REDUCED'}
assert m['input_forms'] == 20 and m['closed_forms'] == 7 and m['remaining_forms'] == 13
print('PASS')
print('input_forms=20')
print('closed_forms=7')
print('remaining_forms=13')
print('remaining_arithmetic_branches=15')
print('five_state_rigidity=OPEN_PARTIAL')
