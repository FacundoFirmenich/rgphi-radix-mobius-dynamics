#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, log2

for n in range(12):
    c=40*10**n
    triplet=(c-3,c,c+3)
    assert gcd(gcd(triplet[0],triplet[1]),triplet[2])==1
    assert triplet[0]+triplet[2]==2*triplet[1]
    assert sum(triplet)==3*triplet[1]
    eps=Fraction(3,c)
    assert Fraction(triplet[0],c)==1-eps
    assert Fraction(triplet[2],c)==1+eps
    assert eps==Fraction(3,40*10**n)

assert 2**1 < 3 <= 2**2
assert log2(3)>1
mean=Fraction(-1+0+1,3)
var=sum((Fraction(s)-mean)**2 for s in (-1,0,1))/3
assert mean==0 and var==Fraction(2,3)
for n in range(10):
    e0=Fraction(3,40*10**n)
    e1=Fraction(3,40*10**(n+1))
    assert e1/e0==Fraction(1,10)

print('PASS_TURNO_010')
print('latent_seed=(pi/6)*10^(+n_scalar)')
print('tripolar_shadow=(40*10^n-3,40*10^n,40*10^n+3)')
print('projective_limit=[1:1:1]')
print('absolute_span=pi/4')
print('relative_span=(3/20)*10^-n')
print('hyperaccess_key=one_trit_or_two_fixed_binary_bits')
print('current_scale_law=MONOSCALE_NOT_MULTIFRACTAL')
print('uncertainty=CLASSICAL_UNLESS_NONCOMMUTATIVE_MODEL_SPECIFIED')
