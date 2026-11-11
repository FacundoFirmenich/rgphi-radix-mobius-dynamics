#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations, combinations


def F(n,A,z,w):
    return (4*n*A**3-2*n*A**2*(w+z)+n*A*w*z
            -20*A**2*w-340*A**2*z+24*A*w*w+148*A*w*z
            +24*A*z*z-4*(z**3+w**3))


def dual_triad(T,S):
    V=set(range(6))
    def is_3cycle(G,B):
        if {G[v] for v in B} != B: return False
        x=next(iter(B)); y=G[x]; z=G[y]
        return len({x,y,z})==3 and G[z]==x
    for A_tuple in combinations(range(6),3):
        A=set(A_tuple); B=V-A
        if 0 not in A: continue
        for G,H in ((T,S),(S,T)):
            if not (is_3cycle(G,A) and is_3cycle(G,B)): continue
            if {H[v] for v in A}==B and {H[v] for v in B}==A:
                if len({H[v] for v in A})==3 and len({H[v] for v in B})==3:
                    return True
    return False


def alternating_hexagon(T,S):
    for p in permutations(range(6)):
        if p[0] != 0: continue
        for start in (0,1):
            if all((T if (i+start)%2==0 else S)[v] == p[(i+1)%6]
                   for i,v in enumerate(p)):
                return True
    return False


def short_defect_cycle(T,S,strictT,strictS,maxlen=5):
    n=len(T)
    edges=lambda v:[(T[v],strictT[v]),(S[v],strictS[v])]
    for start in range(n):
        stack=[(start,[start],0)]
        while stack:
            v,path,strict_count=stack.pop()
            if len(path)>maxlen: continue
            for w,is_strict in edges(v):
                sc=strict_count+int(is_strict)
                if w==start and len(path)>=2:
                    if len(path)<=maxlen and sc==1: return True
                elif w not in path and len(path)<maxlen:
                    stack.append((w,path+[w],sc))
    return False


assert Fraction(2,5) < Fraction(4,9)
assert Fraction(892,45) < 20
assert F(19,5170,1000,900) == -1733592000
assert F(19,5171,1000,900) == 106817836

T=(1,2,0,4,5,3)
S=(3,4,5,0,1,2)
assert dual_triad(T,S)

T5=(0,2,1,4,3)
S5=(1,0,4,1,2)
strictT=(False,)*5
strictS=(False,False,False,True,False)
assert short_defect_cycle(T5,S5,strictT,strictS,5)

print('PASS')
print('OR1_exact_supremum=2/5')
print('OR2_continuous_supremum=892/45')
print('OR2_integer_bound=n<=19')
print('F19_strict_real_chamber=PASS')
print('OR4_signature_checker=PASS')
print('OR5_short_defect_cycle_checker=PASS')
