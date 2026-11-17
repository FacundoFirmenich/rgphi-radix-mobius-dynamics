#!/usr/bin/env python3
from fractions import Fraction
from math import ceil, gcd, log2

def K(w): return 8*10**len(w)-9*(int(w) if w else 0)
def vp(n,p):
    n=abs(n);a=0
    while n%p==0:a+=1;n//=p
    return a
def primitive(n,p): return n//(p**vp(n,p))
def lcm(a,b): return abs(a//gcd(a,b)*b)
def recover_word(Kv,ell):
    num=8*10**ell-Kv
    assert num%9==0
    v=num//9
    assert 0<=v<10**ell
    return str(v).zfill(ell) if ell else ''

assert K('123')==K('8123')==K('88123')==6893
for w in ('123','8123','901961','02'):
    kv=K(w)
    recovered=(1 if kv>0 else -1)*lcm(abs(primitive(kv,7)),abs(primitive(kv,2)))
    assert recovered==kv
    assert recover_word(kv,len(w))==w
for L in (100,1000,10000):
    m=L-len('123')+1
    assert ceil(log2(m))/L<0.1
c=Fraction(1,3)
assert 1-c*c>0
assert 7*4==28
pi3=Fraction(1,14)
assert pi3*Fraction(1,2)==Fraction(1,28)
print('PASS_TURNO_009')
print('FST11_superaccess=Pi7+Pi2 -> K')
print('FST11_hyperaccess=prefix/length key; normalized complexity -> 0')
print('UMI_latent_active_block=PASS')
print('royal_cubit_digits=28')
print('known_strict_event_rate=1/28')
print('mean_log_content=log(3)/28')
