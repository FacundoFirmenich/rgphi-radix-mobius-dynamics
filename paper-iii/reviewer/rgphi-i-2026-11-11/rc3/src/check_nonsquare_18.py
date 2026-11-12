#!/usr/bin/env python3
from math import isqrt
sq={m:{(x*x)%m for x in range(m)} for m in (4,5,11,17)}
for j in range(1,19):
    q=403*j*j+15314*j+190969
    assert isqrt(q)**2 != q
    if j%2: m=4
    elif j in (4,8,14,18): m=5
    elif j in (2,12,16): m=11
    else: assert j in (6,10); m=17
    assert q%m not in sq[m]
print('PASS nonsquare_18')
