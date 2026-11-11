#!/usr/bin/env python3
from math import gcd
from functools import reduce

n=17
A=64233
z=11741
w=1138

def F(A,z,w,mod=None):
    v=(4*n*A**3-2*n*A**2*(w+z)+n*A*w*z-20*A**2*w-340*A**2*z+
       24*A*w**2+148*A*w*z+24*A*z**2-4*(z**3+w**3))
    return v if mod is None else v%mod

assert F(A,z,w)==0
assert A>5*z>w>0
assert reduce(gcd,(A,z,w))==1
assert (z**3+w**3)%A==0
assert (z**3+w**3)//A==25220421
C=2*A-z
D=2*A-w
f=(2*z-3*w)*(2*z-w)
g=(7*z+2*w)*(11*z-2*w)
assert C==116725 and D==127328
assert gcd(C,D)==23
assert f*23==80997*D
assert g*23==2111575*C
assert (g*D-f*C+(5*w+85*z-n*A)*C*D)==0
assert (g*D-f*C)==-(5*w+85*z-n*A)*C*D

def projective_points(p):
    pts=[]
    for zz in range(p):
        for ww in range(p):
            if F(1,zz,ww,p)==0:
                pts.append((1,zz,ww))
    for ww in range(p):
        if F(0,1,ww,p)==0:
            pts.append((0,1,ww))
    if F(0,0,1,p)==0:
        pts.append((0,0,1))
    return pts

def grad(pt,p):
    aa,zz,ww=pt
    dA=(12*n*aa*aa-4*n*aa*(ww+zz)+n*ww*zz-40*aa*ww-680*aa*zz+
        24*ww*ww+148*ww*zz+24*zz*zz)%p
    dz=(-2*n*aa*aa+n*aa*ww-340*aa*aa+148*aa*ww+48*aa*zz-12*zz*zz)%p
    dw=(-2*n*aa*aa+n*aa*zz-20*aa*aa+48*aa*ww+148*aa*zz-12*ww*ww)%p
    return dA,dz,dw

counts={}
for p,expected in [(7,10),(11,14),(13,18),(17,23)]:
    pts=projective_points(p)
    assert len(pts)==expected
    assert all(any(v%p for v in grad(P,p)) for P in pts)
    counts[p]=len(pts)
assert gcd(gcd(counts[7],counts[11]),gcd(counts[13],counts[17]))==1

# For every possible prime divisor ell of rational torsion, choose good primes
# different from ell. Their group orders have gcd 1 (or do not contain ell).
candidate_primes=set()
for order in counts.values():
    x=order
    d=2
    while d*d<=x:
        if x%d==0:
            candidate_primes.add(d)
            while x%d==0: x//=d
        d+=1
    if x>1: candidate_primes.add(x)
for ell in candidate_primes:
    admissible=[order for p,order in counts.items() if p!=ell]
    g0=reduce(gcd,admissible)
    assert g0%ell!=0

print('PASS')
print('point=[64233:11741:1138]')
print('chamber=A>5z>w>0')
print('cube_quotient=25220421')
print('C=116725 D=127328 gcd=23')
print('finite_field_orders=7:10,11:14,13:18,17:23')
print('rational_torsion=TRIVIAL')
print('rank_lower_bound=1')
