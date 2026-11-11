#!/usr/bin/env python3
"""OR21 exact finite-state checks (branch-only, no global classification).
Derived from canonical Round017 five-state counterfamily and OR20 B=19 control.
Python 3 standard library; SymPy optional for the characteristic polynomial.
"""
from fractions import Fraction
from math import gcd, prod
R, M = 88011536665779, 223336848698040
F = [(406,731),(712,731),(712,1265),(1218,1265),(406,557)]
T_INDEX=[1,0,3,2,4]
S_INDEX=[4,2,1,0,0]

def maps(v,B):
    p,q=v
    assert gcd(p,q)==1 and 2*p>q>p
    k=B*p//q
    t=(B*p-k*q,q)
    dt=gcd(*t)
    t=(t[0]//dt,t[1]//dt)
    k=B*(q-p)//p
    z=(p,(1-B-k)*p+B*q)
    ds=gcd(*z)
    s=(z[0]//ds,z[1]//ds)
    assert dt==gcd(B,q) and ds==gcd(B,p)
    return (t,dt),(s,ds)

def check_family(B):
    for i,v in enumerate(F):
        (t,dt),(s,ds)=maps(v,B)
        assert t==F[T_INDEX[i]] and s==F[S_INDEX[i]]
        assert dt==1 and ds==(3 if i==3 else 1)

def cycles():
    E=[[(T_INDEX[i],1,"T"),(S_INDEX[i],3 if i==3 else 1,"S")]
       for i in range(5)]
    result=[]
    for root in range(5):
        def visit(v,seen,pr,labs):
            for j,d,label in E[v]:
                if j==root:result.append((tuple(seen),pr*d,labs+label))
                elif j>root and j not in seen:visit(j,seen+[j],pr*d,labs+label)
        visit(root,[root],1,"")
    return result

def main():
    for n in range(3):check_family(R+n*M)
    c=cycles()
    assert len(c)==6
    assert any(len(nodes)==4 and d==3 for nodes,d,_ in c)
    assert any(d==1 for _,d,_ in c)
    assert all(d**4<=3**len(nodes) for nodes,d,_ in c)
    pi=[Fraction(2,7),Fraction(3,14),Fraction(1,7),Fraction(1,14),Fraction(2,7)]
    assert sum(pi)==1
    for j in range(5):
        assert sum(pi[i]*Fraction((T_INDEX[i]==j)+(S_INDEX[i]==j),2)
                   for i in range(5))==pi[j]
    assert pi[3]/2==Fraction(1,28)
    assert 3**29<R<3**30 and R%3==0
    control=[(5,9),(5,6)]
    for i,v in enumerate(control):
        (t,dt),(s,ds)=maps(v,19)
        assert t==v and s==control[1-i] and dt==ds==1
    try:
        import sympy as sy
        z,l=sy.symbols("z l")
        A=sy.zeros(5)
        for i in range(5):
            A[i,T_INDEX[i]]+=1
            A[i,S_INDEX[i]]+=z if i==3 else 1
        polynomial=l**5-l**4-4*l**3+3*l**2+3*l-1-(l-1)*z
        assert sy.expand((l*sy.eye(5)-A).det()-polynomial)==0
    except ImportError:
        print("SymPy unavailable: polynomial test skipped; finite checks PASS")
    print("OR21 PASS: 5-state family n=0,1,2; 6 simple cycles;"
          " max pitch log(3)/4; pi; log drift log(3)/28; B=19 control")

if __name__=="__main__":
    main()
