#!/usr/bin/env python3
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]
m=json.loads((R/'METRICS.json').read_text())
forms=list(csv.DictReader((R/'02_QUOTIENT/DIOPHANTINE_NORMAL_FORMS.csv').open()))
links=list(csv.DictReader((R/'02_QUOTIENT/CLASS_TO_NORMAL_FORM.csv').open()))
elim=list(csv.DictReader((R/'02_QUOTIENT/ELIMINATION_LEDGER.csv').open()))
assert len(forms)==m['normal_forms']
assert len(links)==m['surviving_classes']
assert len(elim)==m['eliminated_classes']
assert len(links)+len(elim)==m['input_classes']==560
assert sum(int(x['class_count']) for x in forms)==len(links)
assert {x['normal_form'] for x in links}=={x['form_id'] for x in forms}
print('PASS')
print(f"input_classes={m['input_classes']}")
print(f"eliminated_classes={m['eliminated_classes']}")
print(f"normal_forms={m['normal_forms']}")
print('five_state_rigidity=OPEN_PARTIAL')