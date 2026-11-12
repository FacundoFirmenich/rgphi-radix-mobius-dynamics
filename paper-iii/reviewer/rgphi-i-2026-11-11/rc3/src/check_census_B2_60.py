import csv,math
from pathlib import Path
p=Path(__file__).with_name('exact_census_B2_60.csv')
rows=list(csv.DictReader(p.open()))
assert [int(r['B']) for r in rows]==list(range(2,61))
for r in rows:
    B=int(r['B'])
    assert int(r['nonpermutation_scc_le_n'])==0
    if r['method']=='cycle_budget':
        assert math.gcd(B,6)==1
    else:
        assert r['method']=='exact_divisor_universe'
        assert r['N'] and int(r['universe'])>=0
print('PASS')
print('bases=2..60')
print('nonpermutation_scc_le_5=0')
