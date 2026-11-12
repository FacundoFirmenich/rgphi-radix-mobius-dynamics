#!/usr/bin/env python3
from fractions import Fraction
from math import gcd,lcm
B0=88_011_536_665_779
M=223_336_848_698_040
F=[Fraction(406,731),Fraction(712,731),Fraction(712,1265),Fraction(1218,1265),Fraction(406,557)]
TM=[1,0,3,2,4]; SM=[4,2,1,0,0]
def T(B,x): return Fraction((B*x.numerator)%x.denominator,x.denominator)
def S(B,x):
    c=Fraction(x.denominator-x.numerator,x.numerator)
    t=Fraction((B*c.numerator)%c.denominator,c.denominator)
    return Fraction(1,1+t)
assert M==lcm(731,1265,557,712,1218)
for t in range(1001):
    B=B0+t*M
    assert [T(B,x) for x in F]==[F[j] for j in TM]
    assert [S(B,x) for x in F]==[F[j] for j in SM]
    assert [gcd(B,x.denominator) for x in F]==[1,1,1,1,1]
    assert [gcd(B,x.numerator) for x in F]==[1,1,1,3,1]
    for s in range(5):
        seen={s};todo=[s]
        while todo:
            i=todo.pop()
            for j in (TM[i],SM[i]):
                if j not in seen: seen.add(j);todo.append(j)
        assert len(seen)==5
assert 1161%406==349
for a,m in ((171,731),(254,1265),(349,406),(179,712)): assert a*a%m==1
print('PASS counterfamily_1001')
print('five_independent_CRT_congruences=PASS')
print('involutive_fibres=PASS')
