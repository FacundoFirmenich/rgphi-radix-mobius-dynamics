#!/usr/bin/env python3
import sympy as sp

a,z,w,m,W = sp.symbols('a z w m W', integer=True)
c = 2*a-z
d = 2*a-w
N = sp.expand(c**2-a**2)
L = 8*z-7*w-2*m
expr = sp.expand(4*N + w*L)
expr_rel = sp.expand(expr.subs(z**2,w**2+m*a))
q1,r1 = sp.div(expr_rel,d,a)
assert sp.expand(r1) == 0

D = a-W
N2 = sp.expand(N.subs(w,2*W))
expr2 = sp.expand(N2 - W*(m+7*W-4*z))
expr2_rel = sp.expand(expr2.subs(z**2,4*W**2+m*a))
q2,r2 = sp.div(expr2_rel,D,a)
assert sp.expand(r2) == 0

print('PASS')
print('odd_w_identity=4N_congruent_minus_wL_mod_d')
print('even_w_identity=N_congruent_W(m+7W-4z)_mod_D')
