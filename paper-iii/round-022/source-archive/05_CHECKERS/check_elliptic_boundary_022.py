#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction
from math import gcd
A,C,D,n,m,x,Y=sp.symbols('A C D n m x Y')
z=2*A-C
w=2*A-D
F=4*n*A**3-2*n*A**2*(w+z)+n*A*w*z-20*A**2*w-340*A**2*z+24*A*w**2+148*A*w*z+24*A*z**2-4*(z**3+w**3)
G=4*C**3+4*D**3+(n+148)*A*C*D-4*A**2*C-324*A**2*D
assert sp.expand(F-G)==0
quad=4*(1+m**3)*x**2+(n+148)*m*x-(4+324*m)
Yexpr=8*(1+m**3)*x+(n+148)*m
Q=5184*m**4+64*m**3+(n+148)**2*m**2+5184*m+64
assert sp.rem(sp.expand(Yexpr**2-Q),quad,x)==0
# n=17 regression
AA,zz,ww=64233,11741,1138
CC,DD=2*AA-zz,2*AA-ww
assert (CC,DD)==(116725,127328)
assert 9*AA < 5*CC < 5*DD < 10*AA
assert gcd(CC,DD)==23
mm=Fraction(DD,CC);xx=Fraction(CC,AA)
yy=8*(1+mm**3)*xx+165*mm
qq=5184*mm**4+64*mm**3+165**2*mm**2+5184*mm+64
assert yy**2==qq
print('PASS')
print('boundary_cubic_transform=PASS')
print('boundary_quartic_birational_identity=PASS')
print('n17_regression=PASS')
