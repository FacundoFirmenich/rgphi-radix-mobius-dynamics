#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from functools import reduce


def F(n,A,z,w):
    return (4*n*A**3-2*n*A**2*(w+z)+n*A*w*z
            -20*A**2*w-340*A**2*z+24*A*w*w+148*A*w*z
            +24*A*z*z-4*(z**3+w**3))

n=17; A=64233; z=11741; w=1138
assert F(n,A,z,w)==0
assert A>5*z>w>0
assert reduce(gcd,(A,z,w))==1
assert (z**3+w**3)//A==25220421
C=2*A-z; D=2*A-w; d=gcd(C,D)
f=(2*z-3*w)*(2*z-w)
g=(7*z+2*w)*(11*z-2*w)
assert (C,D,d)==(116725,127328,23)
assert g*D-f*C+(5*w+85*z-n*A)*C*D==0
assert g%(C//d)==0
assert f%(D//d)==0
assert Fraction(f,D).denominator==d
assert Fraction(g,C).denominator==d
assert Fraction(f,D)==Fraction(80997,23)
assert Fraction(g,C)==Fraction(2111575,23)
assert 17 < 19 < 23

quartic_hits=[
(2,473,1382),(2,983,5623),(7,1201,6434),(8,1892,6349),
(9,747,2054),(12,94,331),(17,10,91),(17,159,793)]
assert len(quartic_hits)==8
assert sum(1 for x in quartic_hits if x[0]==17)==2

print('PASS')
print('OR6_active_index=17 envelope_index=19')
print('OR7_common_obstruction=23')
print('defect_completion=C/d|g,D/d|f')
print('reduced_defect_denominators=23,23')
print('prime_ladder_status=POSTHOC_LOW_AUTHORITY')
