#!/usr/bin/env python3
from fractions import Fraction
from functools import reduce
from math import gcd,lcm

n=17
O=(0,1,-1)
P=(64233,116725,127328)
R=(1,0,0)
Q_EXPECT=(84507535659963098565309,369204931320206918906825,-66883811065922949873056)

def F(X):
    A,C,D=map(Fraction,X)
    return 4*C**3+4*D**3+(n+148)*A*C*D-4*A*A*C-324*A*A*D

def grad(X):
    A,C,D=map(Fraction,X)
    return ((n+148)*C*D-8*A*C-648*A*D,12*C*C+(n+148)*A*D-4*A*A,12*D*D+(n+148)*A*C-324*A*A)

def canon(X):
    X=tuple(Fraction(x) for x in X);den=1
    for x in X:den=lcm(den,x.denominator)
    a=[int(x*den) for x in X];g=reduce(gcd,[abs(x) for x in a if x]);a=[x//g for x in a]
    for x in a:
        if x:
            if x<0:a=[-y for y in a]
            break
    return tuple(a)

def third(X,Y):
    X=canon(X);Y=canon(Y)
    if X!=Y:
        fp=F(tuple(X[i]+Y[i] for i in range(3)));fm=F(tuple(X[i]-Y[i] for i in range(3)))
        c12=(fp+fm)/2;c21=(fp-fm)/2
        return canon(tuple(c12*X[i]-c21*Y[i] for i in range(3)))
    g=grad(X);V=None
    for e in [(1,0,0),(0,1,0),(0,0,1)]:
        c=(g[1]*e[2]-g[2]*e[1],g[2]*e[0]-g[0]*e[2],g[0]*e[1]-g[1]*e[0])
        cr=(X[1]*c[2]-X[2]*c[1],X[2]*c[0]-X[0]*c[2],X[0]*c[1]-X[1]*c[0])
        if c!=(0,0,0) and cr!=(0,0,0):V=c;break
    fp=F(tuple(X[i]+V[i] for i in range(3)));fm=F(tuple(X[i]-V[i] for i in range(3)))
    a=(fp+fm)/2;b=(fp-fm)/2
    return canon(tuple(b*X[i]-a*V[i] for i in range(3)))

def add(X,Y):return third(third(X,Y),O)
Q=add(add(R,R),P)
assert Q==Q_EXPECT and F(Q)==0
assert gcd(abs(Q[0]),abs(Q[1]+Q[2]))==22873516239

def inv(a,p):return pow(a%p,-1,p)
def norm(X,p):
    X=tuple(x%p for x in X)
    for x in X:
        if x:return tuple(y*inv(x,p)%p for y in X)
    raise ValueError

def Fp(X,p):
    A,C,D=X;return (4*C**3+4*D**3+(n+148)*A*C*D-4*A*A*C-324*A*A*D)%p

def gp(X,p):
    A,C,D=X;return ((n+148)*C*D-8*A*C-648*A*D,12*C*C+(n+148)*A*D-4*A*A,12*D*D+(n+148)*A*C-324*A*A)

def thirdp(X,Y,p):
    X=norm(X,p);Y=norm(Y,p)
    if X!=Y:
        fp=Fp(tuple((X[i]+Y[i])%p for i in range(3)),p);fm=Fp(tuple((X[i]-Y[i])%p for i in range(3)),p)
        h=inv(2,p);c12=(fp+fm)*h%p;c21=(fp-fm)*h%p
        return norm(tuple((c12*X[i]-c21*Y[i])%p for i in range(3)),p)
    g=tuple(x%p for x in gp(X,p));V=None
    for e in [(1,0,0),(0,1,0),(0,0,1)]:
        c=((g[1]*e[2]-g[2]*e[1])%p,(g[2]*e[0]-g[0]*e[2])%p,(g[0]*e[1]-g[1]*e[0])%p)
        cr=((X[1]*c[2]-X[2]*c[1])%p,(X[2]*c[0]-X[0]*c[2])%p,(X[0]*c[1]-X[1]*c[0])%p)
        if c!=(0,0,0) and cr!=(0,0,0):V=c;break
    fp=Fp(tuple((X[i]+V[i])%p for i in range(3)),p);fm=Fp(tuple((X[i]-V[i])%p for i in range(3)),p)
    h=inv(2,p);a=(fp+fm)*h%p;b=(fp-fm)*h%p
    return norm(tuple((b*X[i]-a*V[i])%p for i in range(3)),p)

def addp(X,Y,p):return thirdp(thirdp(X,Y,p),O,p)
def points(p):
    out=set()
    for C in range(p):
        for D in range(p):
            if Fp((1,C,D),p)==0:out.add(norm((1,C,D),p))
    for D in range(p):
        if Fp((0,1,D),p)==0:out.add(norm((0,1,D),p))
    if Fp((0,0,1),p)==0:out.add(norm((0,0,1),p))
    return out

def order(X,p,N):
    cur=norm(O,p)
    for k in range(1,N+1):
        cur=addp(cur,X,p)
        if cur==norm(O,p):return k

def logR(p,N):
    cur=norm(O,p)
    for k in range(1,N+1):
        cur=addp(cur,P,p)
        if cur==norm(R,p):return k
        if cur==norm(O,p):return None

for p,N,op,orr,lg in [(7,10,5,10,None),(83,89,89,89,44)]:
    assert len(points(p))==N
    assert order(P,p,N)==op and order(R,p,N)==orr and logR(p,N)==lg
    assert addp(addp(R,R,p),P,p)==norm(O,p)

print('PASS_F17_LOCAL_GLOBAL')
