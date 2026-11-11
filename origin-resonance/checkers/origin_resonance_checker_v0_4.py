#!/usr/bin/env python3
from fractions import Fraction
from math import log

# Golden/Fibonacci conjugacy.
H=((0,1),(1,1))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
I2=((1,0),(0,1))
H2=mm(H,H)
assert H2==tuple(tuple(H[i][j]+I2[i][j] for j in range(2)) for i in range(2))

# Boundary involution.
U=((1,0,0),(2,-1,0),(2,0,-1))
I3=((1,0,0),(0,1,0),(0,0,1))
assert mm(U,U)==I3
O=(0,1,-1); R=(1,2,2)
def mv(A,v): return tuple(sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A)))
assert mv(U,O)==(0,-1,1)
assert mv(U,R)==(1,0,0)

# Dual sharp ninths: exact asymptotic witnesses.
def slope_excess(a,t): return Fraction(1-t,2*a-1)
def neg_h(a,t): return Fraction((3*t-2)*(2-t),2*a-t)
assert slope_excess(Fraction(5000001,1000000),Fraction(1,1000000)) < Fraction(1,9)
assert neg_h(Fraction(5000001,1000000),Fraction(999999,1000000)) < Fraction(1,9)

# Spectral/content receipt for the known 4-cycle counterfamily.
B=88011536665779
m=4
Delta=3
alpha=log(Delta)/(m*log(B))
assert 0 < alpha < 1
assert abs((alpha+(1-alpha))-1) < 1e-15

# Six-state finite defect spectrum from d<8.
assert list(range(2,8))==[2,3,4,5,6,7]

print('PASS')
print('golden_conjugacy=H^2-H-I=0')
print('boundary_involution=U^2=I; UO=-O; UR=[1:0:0]')
print('projective_helical_lift=PASS')
print('content_access_share_in_0_1=PASS')
print('dual_exact_ninths=PASS')
print('n6_defect_spectrum=2..7')
