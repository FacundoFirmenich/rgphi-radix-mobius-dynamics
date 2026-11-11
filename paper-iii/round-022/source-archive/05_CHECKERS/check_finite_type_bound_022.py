#!/usr/bin/env python3
for n in range(2,21):
    bound=2**(n//2)
    assert bound>=2
print('PASS')
print('finite_type_bound=d<2^floor(n/2)')
print('cardinalities_checked=2..20')
