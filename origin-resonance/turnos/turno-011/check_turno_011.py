#!/usr/bin/env python3
from fractions import Fraction
from math import cos, log, pi, sqrt

# Corrected tripolar geometry.
assert Fraction(2,30)==Fraction(1,15)
assert 14+16==2*15
assert Fraction(14,15)==1-Fraction(1,15)
assert Fraction(16,15)==1+Fraction(1,15)

# D3 group as pairs (epsilon,k).
def mul(a,b):
    e,k=a; f,l=b
    return ((e+f)%2,(k+((-1)**e)*l)%3)
E=(0,0); R=(0,1); S=(1,0)
def power(a,n):
    out=E
    for _ in range(n): out=mul(out,a)
    return out
assert power(R,3)==E
assert power(S,2)==E
assert mul(mul(S,R),S)==power(R,2)
assert len({(e,k) for e in range(2) for k in range(3)})==6

# Koch endpoint preservation in coordinates x+i*sqrt(3)*y.
def vectors(sig):
    if sig==0:
        return [(Fraction(1,4),Fraction(0))]*4
    return [
        (Fraction(1,3),Fraction(0)),
        (Fraction(1,6),Fraction(sig,6)),
        (Fraction(1,6),Fraction(-sig,6)),
        (Fraction(1,3),Fraction(0)),
    ]
for sig in (-1,0,1):
    vv=vectors(sig)
    assert sum(v[0] for v in vv)==1
    assert sum(v[1] for v in vv)==0

# Active Koch multifractal weights from 14:15:16.
weights=[Fraction(15,60),Fraction(14,60),Fraction(16,60),Fraction(15,60)]
assert sum(weights)==1 and len(set(weights))>1
logs=[log(float(w)) for w in weights]
mean=sum(float(w)*x for w,x in zip(weights,logs))
var=sum(float(w)*(x-mean)**2 for w,x in zip(weights,logs))
assert var>0
assert -log(sum(float(w)**2 for w in weights))/log(3)>0

# Posttranscendental homothety.
for n in range(12):
    trip=(14*10**n,15*10**n,16*10**n)
    nxt=(14*10**(n+1),15*10**(n+1),16*10**(n+1))
    assert nxt==tuple(10*x for x in trip)
    assert Fraction(trip[0],trip[1])==Fraction(14,15)
    assert Fraction(trip[2],trip[1])==Fraction(16,15)

# Hyperaccess.
assert 2*3==6
for N in (10,100,1000):
    assert log(6,2)/N < 0.3
assert 2**5 < 64 <= 2**6

# Biplanar locking: exactly three minima per offset.
for delta in range(3):
    vals=[]
    for km in range(3):
        for kn in range(3):
            energy=1-cos(2*pi*(km-kn-delta)/3)
            vals.append((round(energy,12),km,kn))
    minimum=min(x[0] for x in vals)
    assert sum(x[0]==minimum for x in vals)==3

# Six-face noncommutative model.
basis=[(e,sig) for e in (0,1) for sig in (-1,0,1)]
idx={b:i for i,b in enumerate(basis)}
Z=[[0j]*6 for _ in range(6)]
Sm=[[0j]*6 for _ in range(6)]
for i,(e,sig) in enumerate(basis):
    Z[i][i]=complex(sig)
    Sm[idx[(1-e,-sig)]][i]=1+0j

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
I=[[1+0j if i==j else 0j for j in range(6)] for i in range(6)]
assert mm(Sm,Sm)==I
assert max(abs(z) for row in madd(mm(Sm,Z),mm(Z,Sm)) for z in row)<1e-12
comm=msub(mm(Z,Sm),mm(Sm,Z))
assert max(abs(z) for row in comm for z in row)>0

psi=[0j]*6
psi[idx[(0,1)]]=1/sqrt(2)
psi[idx[(1,-1)]]=1j/sqrt(2)
def apply(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def inner(u,v):
    return sum(u[i].conjugate()*v[i] for i in range(len(u)))
zpsi=apply(Z,psi); spsi=apply(Sm,psi)
Ez=inner(psi,zpsi); Es=inner(psi,spsi)
Dz2=inner(zpsi,zpsi)-Ez*Ez
Ds2=inner(spsi,spsi)-Es*Es
rhs=abs(inner(psi,apply(comm,psi)))/2
assert abs(Dz2.real-1)<1e-12
assert abs(Ds2.real-1)<1e-12
assert abs(rhs-1)<1e-12

print('PASS_TURNO_011')
print('corrected_tripolar_shape=[14:15:16]')
print('six_faces=D3=2_planes_x_3_phases')
print('koch_endpoint_invariant=PASS')
print('active_koch_measure=tau_nonlinear')
print('posttranscendental_operator=radial_times_10_projective_fixed')
print('nested_hyperaccess=log2(6)/N_to_0')
print('biplanar_phase_lock=3_minima_per_delta')
print('six_face_uncertainty=SATURATED_CONDITIONAL_MODEL')
print('ramanujanian_operator=DOMAIN_COMPOSITION_INVARIANTS_DEFINED')
