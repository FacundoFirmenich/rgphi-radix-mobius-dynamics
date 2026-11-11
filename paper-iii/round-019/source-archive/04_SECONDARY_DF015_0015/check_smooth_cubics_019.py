#!/usr/bin/env python3
import sympy as sp
A,z,w,n=sp.symbols('A z w n')
F=4*n*A**3-2*n*A**2*(w+z)+n*A*w*z-20*A**2*w-340*A**2*z+24*A*w**2+148*A*w*z+24*A*z**2-4*(z**3+w**3)
for nv in range(1,20):
    Fn=sp.expand(F.subs(n,nv))
    assert Fn.subs({A:0,z:1,w:-1})==0
    parts=[sp.diff(Fn,v) for v in (A,z,w)]
    for var in (A,z,w):
        G=sp.groebner(parts+[var-1],A,z,w,order='lex',domain=sp.QQ)
        assert any(p.as_expr()==1 for p in G.polys), (nv,var,G)
print('PASS')
print('smooth_plane_cubics=19/19')
print('rational_base_point=[0:1:-1]')
print('DF015_0015=OPEN_ELLIPTIC_REDUCED')
