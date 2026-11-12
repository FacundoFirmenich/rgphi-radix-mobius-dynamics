"""Exact complete finite-base/size search using divisor theorem; no probabilistic inference."""
import argparse,json,math
from fractions import Fraction
from functools import reduce
from sympy import divisors

def universe(B,n):
    L=math.lcm(*(B**k-1 for k in range(1,n+1)))
    N=B**(n-1)*L
    d=divisors(N)
    states={Fraction(p,q) for q in d for p in d if q//2 < p < q and math.gcd(p,q)==1}
    return N,states

def T(x,B):
    y=B*x; return y-(y.numerator//y.denominator)
def S(x,B):
    y=(1-x)/x; y=T(y,B);return 1/(1+y)

def run(B,n):
    N,states=universe(B,n)
    edges={}
    for x in states:
        a,b=T(x,B),S(x,B)
        if a in states and b in states: edges[x]=(a,b)
    # remove vertices with outgoing edges into discarded vertices, to get maximal closed subset
    active=set(edges)
    while True:
        next_active={x for x in active if all(y in active for y in edges[x])}
        if len(next_active)==len(active):break
        active=next_active
    # SCC via Tarjan
    idx={};low={};stack=[];on=set();comps=[];counter=0
    def visit(v):
        nonlocal counter
        idx[v]=low[v]=counter;counter+=1;stack.append(v);on.add(v)
        for w in edges[v]:
            if w not in active:continue
            if w not in idx:
                visit(w);low[v]=min(low[v],low[w])
            elif w in on:low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v:break
            comps.append(comp)
    for x in active:
        if x not in idx:visit(x)
    closed=[c for c in comps if all(y in c for x in c for y in edges[x])]
    small=[c for c in closed if len(c)<=n]
    nonperm=[c for c in small if len({edges[x][0] for x in c})<len(c) or len({edges[x][1] for x in c})<len(c)]
    return {'B':B,'n':n,'N':str(N),'divisors':len(divisors(N)),'universe':len(states),'maximal_closed_vertices':len(active),'closed_scc':len(closed),'closed_scc_le_n':len(small),'nonpermutation_scc_le_n':len(nonperm),'witnesses':[[str(x) for x in sorted(c)] for c in nonperm[:3]]}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=5);ap.add_argument('--bases',type=int,nargs='+',default=list(range(2,9)));args=ap.parse_args()
 for b in args.bases: print(json.dumps(run(b,args.n)),flush=True)
