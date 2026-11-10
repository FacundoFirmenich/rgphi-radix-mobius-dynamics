#!/usr/bin/env python3
from pathlib import Path
import csv, json, collections, gzip

R = Path(__file__).resolve().parent

with gzip.open(R / "ADJUDICATION_560_CLASSES.csv.gz", "rt", newline="") as fh:
    rows = list(csv.DictReader(fh))
assert len(rows) == 560
counts = collections.Counter(x["status"] for x in rows)
assert counts == collections.Counter({
    "STATE_COLLISION": 432,
    "STRICT_FIBRE_CONFLICT": 60,
    "UNREDUCED_INJECTIVITY_CONFLICT": 34,
    "CYCLE_BUDGET_CONFLICT": 10,
    "SURVIVES_TO_NORMAL_FORM": 24,
})

with gzip.open(R / "DIOPHANTINE_NORMAL_FORMS_12.json.gz", "rt") as fh:
    forms = json.load(fh)
assert len(forms) == 12
assert all(sorted(x["factors"]) == [2, 3] for x in forms)
assert len({x["form_id"] for x in forms}) == 12
surv = [x for x in rows if x["status"] == "SURVIVES_TO_NORMAL_FORM"]
assert len(surv) == 24 and all(x["normal_form_id"] for x in surv)

print("PASS")
print("source_classes=560")
print("state_collision=432")
print("strict_fibre_conflict=60")
print("unreduced_injectivity_conflict=34")
print("cycle_budget_conflict=10")
print("exact_survivors=24")
print("structural_normal_forms=12")
print("five_state_rigidity=OPEN_PARTIAL")
