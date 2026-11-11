#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

R=88011536665779
M=223336848698040
X=[Fraction(406,731),Fraction(712,731),Fraction(712,1265),Fraction(1218,1265),Fraction(406,557)]
TM=[1,0,3,2,4]
SM=[4,2,1,0,0]

def T(B,x):
    y=B*x
    return y-(y.numerator//y.denominator)

def S(B,x):
    z=(1-x)/x
    return 1/(1+T(B,z))

assert M == __import__('math').lcm(731,1265,557,406,712,1218)
assert [R%m for m in (731,1265,557,406,712,1218)] == [171,254,1,349,179,1161]
assert all(Fraction(1,2)<x<1 for x in X)
assert len(set(X))==5

for t in range(1001):
    B=R+t*M
    assert [T(B,x) for x in X] == [X[j] for j in TM]
    assert [S(B,x) for x in X] == [X[j] for j in SM]
    assert gcd(B,1218)==3
    assert gcd(B,731)==gcd(B,1265)==gcd(B,557)==1
    assert gcd(B,406)==gcd(B,712)==1

assert len(set(TM))==5
assert len(set(SM))==4
assert SM.count(0)==2 and 3 not in SM

print('PASS')
print('family_rows=1001')
print('minimal_nonpermutation_cardinality=5')
print('branch=DF015-0007-B2')
print('global_all_high_permutation_rigidity=REFUTED')
print('DF015-0015=OPEN_WITH_SYMBOLIC_SUBCASE_AND_FINITE_AUDIT')
