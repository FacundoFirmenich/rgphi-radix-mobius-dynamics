#!/usr/bin/env python3
"""Independent, finite RC3 checker replay for the resonance branch.

Tests only the archived five-state counterfamily and one exact cycle identity.
Does NOT certify a six-state catalogue, elliptic arithmetic, or hyperaccess.
"""
from fractions import Fraction
from math import gcd, lcm, prod

B0 = 88_011_536_665_779
STEP = 223_336_848_698_040
PQ = ((406, 731), (712, 731), (712, 1265), (1218, 1265), (406, 557))
T_TARGET = (1, 0, 3, 2, 4)
S_TARGET = (4, 2, 1, 0, 0)
X = tuple(Fraction(p, q) for p, q in PQ)
assert STEP == lcm(731, 1265, 557, 712, 1218)

def maps(B, p, q):
    t = Fraction(B * p % q, q)
    r = q - p
    s = Fraction(p, p + (B * r % p))
    return t, s

def reduced_edge_content(B, i, generator):
    p, q = PQ[i]
    return gcd(B, q if generator == 'T' else p)

for k in range(1001):
    B = B0 + k * STEP
    for i, (p, q) in enumerate(PQ):
        assert gcd(p, q) == 1 and q // 2 < p < q
        t, s = maps(B, p, q)
        assert (t, s) == (X[T_TARGET[i]], X[S_TARGET[i]])
        assert reduced_edge_content(B, i, 'T') == 1
        assert reduced_edge_content(B, i, 'S') == (3 if i == 3 else 1)
    for start in range(5):
        reached, pending = {start}, [start]
        while pending:
            i = pending.pop()
            for j in (T_TARGET[i], S_TARGET[i]):
                if j not in reached:
                    reached.add(j)
                    pending.append(j)
        assert len(reached) == 5

# Exhaust all generator-labelled simple cycles, identifying cyclic rotations.
cycles = set()
for initial in range(5):
    def walk(vertices, generators):
        i = vertices[-1]
        for g, target in (('T', T_TARGET[i]), ('S', S_TARGET[i])):
            if target == initial:
                vs = tuple(vertices)
                gs = tuple(generators + [g])
                representations = [(vs[j:] + vs[:j], gs[j:] + gs[:j]) for j in range(len(vs))]
                cycles.add(min(representations))
            elif target not in vertices and len(vertices) < len(PQ):
                walk(vertices + [target], generators + [g])
    walk([initial], [])

receipts = sorted((len(vertices), ''.join(labels),
                   prod(reduced_edge_content(B0, vertex, label)
                        for vertex, label in zip(vertices, labels)))
                  for vertices, labels in cycles)
assert receipts == sorted([
    (2, 'TT', 1), (4, 'TSTS', 3), (2, 'SS', 1),
    (2, 'SS', 1), (2, 'TT', 1), (1, 'T', 1),
]), receipts

# Exact projective monodromy of x3 -> x0 -> x1 -> x2 -> x3.
def edge_matrix(B, generator, i):
    p, q = PQ[i]
    if generator == 'T':
        return ((B, -(B * p // q)), (0, 1))
    return ((1, 0), (1 - B - (B * (q - p) // p), B))

def mul(A, C):
    return tuple(tuple(sum(A[r][k] * C[k][c] for k in range(2))
                       for c in range(2)) for r in range(2))

M = ((1, 0), (0, 1))
Delta = 1
for vertex, generator in ((3, 'S'), (0, 'T'), (1, 'S'), (2, 'T')):
    A = edge_matrix(B0, generator, vertex)
    p, q = PQ[vertex]
    transformed = (A[0][0] * p + A[0][1] * q, A[1][0] * p + A[1][1] * q)
    d = gcd(*transformed)
    assert d == reduced_edge_content(B0, vertex, generator)
    Delta *= d
    M = mul(A, M)
assert Delta == 3
p, q = PQ[3]
assert (M[0][0] * p + M[0][1] * q, M[1][0] * p + M[1][1] * q) == (3*p, 3*q)
det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
tr = M[0][0] + M[1][1]
assert det == B0**4 and B0 % 3 == 0
assert tr == 3 + B0**4 // 3
assert tr**2 - 4*det == (B0**4 // 3 - 3)**2

print('PASS resonance independent RC3 archive replay: 1001 five-state members; 6 exact simple cycles; Delta 3, m 4; spectral monodromy')
print('NO NEW ENDPOINT: OR4/OR5 n>=6 not triggered; OR19 n=6 unenumerated; elliptic 19-curves unchanged')
