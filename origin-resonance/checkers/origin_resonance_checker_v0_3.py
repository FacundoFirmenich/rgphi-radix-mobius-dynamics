#!/usr/bin/env python3
import sys
from fractions import Fraction
from math import gcd
from functools import reduce
from itertools import combinations, permutations
import sympy as sp
sys.set_int_max_str_digits(0)

A,z,w,n=sp.symbols('A z w n')
F=4*n*A**3-2*n*A**2*(w+z)+n*A*w*z-20*A**2*w-340*A**2*z+24*A*w**2+148*A*w*z+24*A*z**2-4*(z**3+w**3)
F0=sp.expand(F.subs(n,0))
assert sp.expand(sp.diff(F,n)-A*(-2*A+w)*(-2*A+z))==0
assert sp.expand(F0.subs(A,0)+4*(w+z)*(w**2-w*z+z**2))==0
assert sp.expand(F0.subs(z,2*A)+4*(-11*A+w)*(-2*A+w)*(7*A+w))==0
assert sp.expand(F0.subs(w,2*A)+4*(-3*A+z)*(-2*A+z)*(-A+z))==0
assert F.subs({A:1,z:2,w:2})==0
assert F.subs({A:0,z:1,w:-1})==0

def Fp(P,p=83):
 a,b,c=P; nn=17
 return (4*nn*a**3-2*nn*a*a*(c+b)+nn*a*c*b-20*a*a*c-340*a*a*b+24*a*c*c+148*a*c*b+24*a*b*b-4*(b**3+c**3))%p
def grad(P,p=83):
 a,b,c=P;nn=17
 return ((12*nn*a*a-4*nn*a*(c+b)+nn*c*b-40*a*c-680*a*b+24*c*c+148*c*b+24*b*b)%p,
         (-2*nn*a*a+nn*a*c-340*a*a+148*a*c+48*a*b-12*b*b)%p,
         (-2*nn*a*a+nn*a*b-20*a*a+48*a*c+148*a*b-12*c*c)%p)
def points(p=83):
 out=[]
 for b in range(p):
  for c in range(p):
   if Fp((1,b,c),p)==0:out.append((1,b,c))
 for c in range(p):
  if Fp((0,1,c),p)==0:out.append((0,1,c))
 if Fp((0,0,1),p)==0:out.append((0,0,1))
 return out
pts=points(83)
assert len(pts)==89
assert all(any(x%83 for x in grad(P,83)) for P in pts)
assert 83+1-len(pts)==-5

N=17;O=(0,1,-1);P=(64233,11741,1138)
def lcm(a,b):return abs(a*b)//gcd(a,b)
def norm(P):
 vals=[Fraction(x) for x in P];L=1
 for x in vals:L=lcm(L,x.denominator)
 q=[x.numerator*(L//x.denominator) for x in vals];g=reduce(gcd,[abs(x) for x in q if x]);q=[x//g for x in q]
 for x in q:
  if x:
   if x<0:q=[-v for v in q]
   break
 return tuple(q)
def FF(P):
 a,b,c=P;nn=N
 return 4*nn*a**3-2*nn*a*a*(c+b)+nn*a*c*b-20*a*a*c-340*a*a*b+24*a*c*c+148*a*c*b+24*a*b*b-4*(b**3+c**3)
def G(P):
 a,b,c=P;nn=N
 return (12*nn*a*a-4*nn*a*(c+b)+nn*c*b-40*a*c-680*a*b+24*c*c+148*c*b+24*b*b,
 -2*nn*a*a+nn*a*c-340*a*a+148*a*c+48*a*b-12*b*b,
 -2*nn*a*a+nn*a*b-20*a*a+48*a*c+148*a*b-12*c*c)
def H(P):
 a,b,c=P;nn=N
 return ((24*nn*a-4*nn*(c+b)-40*c-680*b,-4*nn*a+nn*c-680*a+148*c+48*b,-4*nn*a+nn*b-40*a+48*c+148*b),
 (-4*nn*a+nn*c-680*a+148*c+48*b,48*a-24*b,nn*a+148*a),
 (-4*nn*a+nn*b-40*a+48*c+148*b,nn*a+148*a,48*a-24*c))
def third(P,Q):
 P=norm(P);Q=norm(Q)
 if P!=Q:
  V=tuple(Q[i]-P[i] for i in range(3));gg=G(P);t=Fraction(sum(gg[i]*V[i] for i in range(3)),FF(V))
  return norm([Fraction(P[i])+t*V[i] for i in range(3)])
 gg=G(P);V=(gg[1]*P[2]-gg[2]*P[1],gg[2]*P[0]-gg[0]*P[2],gg[0]*P[1]-gg[1]*P[0]);hh=H(P);bb=Fraction(sum(V[i]*hh[i][j]*V[j] for i in range(3) for j in range(3)),2);t=-bb/Fraction(FF(V))
 return norm([Fraction(P[i])+t*V[i] for i in range(3)])
def add(P,Q):return third(third(P,Q),O)
Q=O
for _ in range(44):Q=add(Q,P)
P2=add(P,P);P4=add(P2,P2)
M={44:Q,48:add(Q,P4),88:add(Q,Q)}
M[96]=add(M[48],M[48])
summary={}
for k,Q in M.items():
 a,b,c=Q;S=b**3+c**3
 summary[k]=(a>5*b>c>0,a//gcd(a,S))
assert summary=={44:(True,4),48:(False,4),88:(False,4),96:(False,4)}
a,b,c=M[44]
ainv=pow(a%83,-1,83)
assert (1,b*ainv%83,c*ainv%83)==(1,2,2)
assert 2*44==88==89-1==83+5

def dual_triad(T,S):
 V=set(range(6))
 def cyc(G,B):
  if {G[v] for v in B}!=B:return False
  x=next(iter(B));y=G[x];zz=G[y]
  return len({x,y,zz})==3 and G[zz]==x
 for At in combinations(range(6),3):
  AA=set(At);BB=V-AA
  if 0 not in AA:continue
  for GG,HH in ((T,S),(S,T)):
   if cyc(GG,AA) and cyc(GG,BB) and {HH[v] for v in AA}==BB and {HH[v] for v in BB}==AA:
    if len({HH[v] for v in AA})==3 and len({HH[v] for v in BB})==3:return True
 return False
def alt_hex(T,S):
 for pp in permutations(range(6)):
  if pp[0]!=0:continue
  for st in (0,1):
   if all((T if (i+st)%2==0 else S)[v]==pp[(i+1)%6] for i,v in enumerate(pp)):return True
 return False
survivors=[
((5,2,1,4,3,0),(1,0,4,1,2,5)),((0,5,1,4,3,2),(1,0,4,1,2,5)),
((0,2,5,4,3,1),(1,0,4,1,2,5)),((0,2,1,5,3,4),(1,0,4,1,2,5)),
((0,2,1,4,5,3),(1,0,4,1,2,5)),((0,2,1,4,3,5),(5,0,4,1,2,1)),
((0,2,1,4,3,5),(1,5,4,1,2,0)),((0,2,1,4,3,5),(1,0,5,1,2,4)),
((0,2,1,4,3,5),(1,0,4,5,2,1)),((0,2,1,4,3,5),(1,0,4,1,5,2))]
assert sum(dual_triad(*x) for x in survivors)==0
assert sum(alt_hex(*x) for x in survivors)==0
print('PASS')
print('pencil_base_locus=PASS')
print('F17_F83_points=89 trace=-5')
print('44P_mod83=R 2R=-P')
print('88=2*44=89-1=83+5')
print('multiples_44_48_88_96=',summary)
print('n6_signatures=0/10,0/10')
