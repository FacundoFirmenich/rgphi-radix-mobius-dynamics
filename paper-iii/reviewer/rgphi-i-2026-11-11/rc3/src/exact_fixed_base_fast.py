"""Exact divisor-universe census implied by the fixed-base theorem."""
import argparse, json, math, bisect, time, sys
from fractions import Fraction
from sympy import divisors

def T(x,B):
    return Fraction((B*x.numerator)%x.denominator, x.denominator)
def S(x,B):
    z=Fraction(x.denominator-x.numerator,x.numerator)
    t=Fraction((B*z.numerator)%z.denominator,z.denominator)
    return Fraction(1,1+t)

def run(B,n):
    t0=time.time()
    L=math.lcm(*[B**k-1 for k in range(1,n+1)])
    N=B**(n-1)*L
    ds=divisors(N)
    states=[]
    for q in ds:
        lo=bisect.bisect_right(ds,q//2)
        hi=bisect.bisect_left(ds,q)
        for p in ds[lo:hi]:
            if 2*p>q and math.gcd(p,q)==1:
                states.append(Fraction(p,q))
    st=set(states)
    edges={}
    for x in st:
        a,b=T(x,B),S(x,B)
        if a in st and b in st:
            edges[x]=(a,b)
    active=set(edges)
    while True:
        nxt={x for x in active if all(y in active for y in edges[x])}
        if nxt==active: break
        active=nxt
    idx={};low={};stack=[];on=set();comps=[];counter=0
    sys.setrecursionlimit(max(10000,2*len(active)+100))
    def visit(v):
        nonlocal counter
        idx[v]=low[v]=counter;counter+=1;stack.append(v);on.add(v)
        for w in edges[v]:
            if w not in active: continue
            if w not in idx:
                visit(w);low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v: break
            comps.append(comp)
    for x in active:
        if x not in idx: visit(x)
    closed=[c for c in comps if all(y in c for x in c for y in edges[x])]
    small=[c for c in closed if len(c)<=n]
    nonperm=[c for c in small if len({edges[x][0] for x in c})<len(c) or len({edges[x][1] for x in c})<len(c)]
    return {'B':B,'n':n,'N':str(N),'divisors':len(ds),'universe':len(st),'maximal_closed_vertices':len(active),'closed_scc':len(closed),'closed_scc_le_n':len(small),'nonpermutation_scc_le_n':len(nonperm),'witnesses':[[str(x) for x in sorted(c)] for c in nonperm[:3]],'seconds':round(time.time()-t0,3)}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=5);ap.add_argument('--bases',type=int,nargs='+',required=True);args=ap.parse_args()
    for B in args.bases:
        print(json.dumps(run(B,args.n)),flush=True)
