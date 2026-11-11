#!/usr/bin/env python3
import sympy as sp
A,z,w,n=sp.symbols('A z w n')
C=2*A-z
D=2*A-w
f=(2*z-3*w)*(2*z-w)
g=(7*z+2*w)*(11*z-2*w)
F=(4*n*A**3-2*n*A**2*(w+z)+n*A*w*z-20*A**2*w-340*A**2*z+
   24*A*w**2+148*A*w*z+24*A*z**2-4*(z**3+w**3))
identity=sp.expand(g*D-f*C+(5*w+85*z-n*A)*C*D+F)
assert identity==0
print('PASS')
print('identity=gD-fC+(5w+85z-nA)CD=-F_n')
print('coprime_completion=SYMBOLIC')
