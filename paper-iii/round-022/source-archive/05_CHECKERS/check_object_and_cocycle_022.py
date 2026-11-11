#!/usr/bin/env python3
from math import gcd
import json
from pathlib import Path

R=Path(__file__).resolve().parents[1]
D=json.loads((R/'02_SPECTRAL_CERTIFICATE/COUNTERFAMILY_CYCLE_CERTIFICATE.json').read_text())
B=D['base']
states={k:tuple(v) for k,v in D['states'].items()}

def mm(A,B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def mv(M,v):
    return (M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1])
def A(k): return [[B,-k],[0,1]]
def C(k): return [[1,0],[1-B-k,B]]

M=[[1,0],[0,1]]
prod=1
for edge in D['cycle']:
    p,q=states[edge['state']]
    if edge['generator']=='T':
        assert edge['digit']==B*p//q
        assert edge['defect']==gcd(q,B)
        E=A(edge['digit'])
    else:
        assert edge['digit']==B*(q-p)//p
        assert edge['defect']==gcd(p,B)
        E=C(edge['digit'])
    prod*=edge['defect']
    M=mm(E,M)
assert M==D['matrix_product']
assert prod==D['defect_product']==3
v=tuple(D['eigenvector'])
assert mv(M,v)==(prod*v[0],prod*v[1])
tr=M[0][0]+M[1][1]
det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det==B**4
assert tr==prod+B**4//prod
assert tr*tr-4*det==(B**4//prod-prod)**2
print('PASS')
print('projective_content_cocycle=PASS')
print('cycle_spectral_identity=PASS')
print('counterfamily_STST_cycle_defect=3')
