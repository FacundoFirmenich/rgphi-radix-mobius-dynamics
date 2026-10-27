#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import csv,json,subprocess
base=Path(__file__).resolve().parent
thr=json.load((base/'RGPHI_THRESHOLD_ROBUSTNESS_RESULT.json').open())
assert thr['status']=='PASS'
assert Fraction(thr['simultaneous_tau1_tau4_robustness']['lower_inclusive'])==Fraction(106197,10000)
assert Fraction(thr['simultaneous_tau1_tau4_robustness']['upper_exclusive'])==Fraction(11643,1000)
assert Fraction(thr['simultaneous_three_level_nonnesting_robustness']['lower_inclusive'])==Fraction(106197,10000)
assert Fraction(thr['simultaneous_three_level_nonnesting_robustness']['upper_exclusive'])==Fraction(1101,100)
trap=json.load((base/'RGPHI_TRAP_CLASSIFICATION_AUDIT_RESULT.json').open())
assert trap['status']=='PASS'
assert trap['closed_sccs']==153 and trap['finite_forward_closures']==1502
assert trap['denominator_formula_checks']==7145037
assert trap['C8']['present'] and trap['C8']['orders']=={'13':6,'11':2}
claims=list(csv.DictReader((base/'RGPHI_PAPER_I_CLAIM_EVIDENCE_MATRIX.csv').open()))
assert len(claims)==10
assert all(r['status'] in {'CLOSED','PROVISIONAL','OPEN'} for r in claims)
pdf=base/'RGPHI_PAPER_I_SUBMISSION_DRAFT_v1.pdf'
assert pdf.exists() and pdf.stat().st_size>100000
try:
    pages=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
    assert 'Pages:' in pages
except FileNotFoundError:
    pass
print('PASS')
