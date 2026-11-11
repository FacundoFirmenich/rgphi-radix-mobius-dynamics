from math import gcd,lcm
from fractions import Fraction
import sympy as sp, csv, time

def Tfrac(x,B):
    p,q=x.numerator,x.denominator
    return Fraction((B*p)%q,q)
def Sfrac(x,B):
    p,q=x.numerator,x.denominator
    y=Fraction(q-p,p)
    t=Tfrac(y,B)
    return Fraction(1,1+t)

def coprime_divisor_pairs_from_factors(fs):
    pairs=[(1,1)]
    for prime,e in fs.items():
        opts=[(1,1)]
        pp=1
        for a in range(1,e+1):
            pp*=prime
            opts.append((pp,1)); opts.append((1,pp))
        pairs=[(p*a,q*b) for p,q in pairs for a,b in opts]
    return pairs

def omega_factors(B,nmax):
    fs={}
    # B^(n-1)
    for p,e in sp.factorint(B).items(): fs[p]=max(fs.get(p,0),(nmax-1)*e)
    # lcm_{k<=n}(B^k-1)
    for k in range(1,nmax+1):
        for p,e in sp.factorint(B**k-1).items(): fs[p]=max(fs.get(p,0),e)
    return fs

def audit(B,nmax=5):
    fs=omega_factors(B,nmax)
    st=[]
    for p,q in coprime_divisor_pairs_from_factors(fs):
        if p<q and 2*p>q: st.append(Fraction(p,q))
    idx={x:i for i,x in enumerate(st)}
    outs={}; valid=[]
    for i,x in enumerate(st):
        tx=Tfrac(x,B); sx=Sfrac(x,B)
        if Fraction(1,2)<tx<1 and Fraction(1,2)<sx<1 and tx in idx and sx in idx:
            outs[i]=(idx[tx],idx[sx]); valid.append(i)
    V=set(valid); adj={i:[j for j in outs[i] if j in V] for i in valid}
    index=0; stack=[]; on=set(); ind={}; low={}; comps=[]
    def strong(v):
        nonlocal index
        ind[v]=low[v]=index; index+=1; stack.append(v); on.add(v)
        for w in adj[v]:
            if w not in ind: strong(w); low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],ind[w])
        if low[v]==ind[v]:
            C=[]
            while True:
                w=stack.pop(); on.remove(w); C.append(w)
                if w==v: break
            comps.append(C)
    for v in valid:
        if v not in ind: strong(v)
    closed=[]
    for comp in comps:
        C=set(comp)
        if len(C)<=nmax and all(i in outs and outs[i][0] in C and outs[i][1] in C for i in C):
            t=[outs[i][0] for i in comp]; s=[outs[i][1] for i in comp]
            nonperm=(len(set(t))<len(comp) or len(set(s))<len(comp))
            closed.append((len(comp),nonperm))
    return len(st),len(closed),max([a for a,b in closed],default=0),min([a for a,b in closed if b],default=None)

rows=[]
for B in range(2,51):
    t=time.time(); nst,nc,maxc,nmin=audit(B,5); sec=time.time()-t
    rows.append((B,nst,nc,maxc,'' if nmin is None else nmin,round(sec,4)))
    print(rows[-1], flush=True)
with open('/mnt/data/FIXED_B_N5_AUDIT_B2_50.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['B','candidate_states','closed_components_size_le_5','max_closed_component_size','nonpermutation_nmin_le_5','seconds']); w.writerows(rows)
print('DONE')
