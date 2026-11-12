#!/usr/bin/env python3
from math import gcd
B=88_011_536_665_779
states={'x0':(406,731),'x1':(712,731),'x2':(712,1265),'x3':(1218,1265),'x4':(406,557)}
cycle=[('S','x3',3396175881191,3),('T','x0',48881920501102,1),('S','x1',2348622467204,1),('T','x2',49536928147062,1)]
def mm(A,C): return [[A[0][0]*C[0][0]+A[0][1]*C[1][0],A[0][0]*C[0][1]+A[0][1]*C[1][1]],[A[1][0]*C[0][0]+A[1][1]*C[1][0],A[1][0]*C[0][1]+A[1][1]*C[1][1]]]
def mv(A,v): return (A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])
M=[[1,0],[0,1]];D=1
for g,x,k,d in cycle:
    p,q=states[x]
    A=[[B,-k],[0,1]] if g=='T' else [[1,0],[1-B-k,B]]
    assert gcd(*(mv(A,(p,q))))==d
    M=mm(A,M);D*=d
v=states['x3'];assert mv(M,v)==(D*v[0],D*v[1]);assert D==3
tr=M[0][0]+M[1][1];det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det==B**4 and tr==3+B**4//3 and tr*tr-4*det==(B**4//3-3)**2
print('PASS projective_content_spectral_cycle')
