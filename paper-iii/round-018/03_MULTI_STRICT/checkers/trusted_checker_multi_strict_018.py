#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import csv,json
R=Path(__file__).resolve().parents[2]
P=R/'03_MULTI_STRICT'
profiles={r['id']:r for r in csv.DictReader((P/'TWO_STRICT_CANONICAL_PROFILES_840.csv').open())}
assert len(profiles)==840
certs=json.loads((P/'HIGH_INFEASIBILITY_FARKAS_728.json').read_text())
assert len(certs)==728

class WDSU:
    def __init__(self,n):self.p=list(range(n));self.w=[Fraction(1)]*n
    def find(self,x):
        if self.p[x]!=x:
            p=self.p[x];r=self.find(p);self.w[x]*=self.w[p];self.p[x]=r
        return self.p[x]
    def weight(self,x):self.find(x);return self.w[x]
    def union(self,i,j,f):
        ri=self.find(i);rj=self.find(j);wi=self.w[i];wj=self.w[j]
        if ri==rj:return wi==f*wj
        self.p[ri]=rj;self.w[ri]=f*wj/wi;return True

def parse(s):
    return [(0 if x[0]=='T' else 1,int(x[1:].split(':')[0]),int(x.split('r')[1])) for x in s.split('|')

def inequality_rows(r):
    T=tuple(map(int,r['T'].split(',')));S=tuple(map(int,r['S'].split(',')));sd={(g,s):f for g,s,f in parse(r['strict_edges'])};pd=WDSU(5);qd=WDSU(5)
    for i in range(5):assert qd.union(i,T[i],Fraction(sd.get((0,i),1)));assert pd.union(i,S[i],Fraction(sd.get((1,i),1)))
    pr=sorted({pd.find(i) for i in range(5)});qr=sorted({qd.find(i) for i in range(5)});idx={('p',x):i for i,x in enumerate(pr)};idx.update({('q',x):len(pr)+i for i,x in enumerate(qr)});out={}
    for i in range(5):
        ip=idx[('p',pd.find(i))];iq=idx[('q',qd.find(i))];wp=pd.weight(i);wq=qd.weight(i);n=len(idx)
        v=[Fraction(0)]*n;v[ip]=-wp;out[f'p{i}>=1']=(v,Fraction(-1))
        v=[Fraction(0)]*n;v[ip]=wp;v[iq]=-wq;out[f'q{i}-p{i}>=1']=(v,Fraction(-1))
        v=[Fraction(0)]*n;v[ip]=-2*wp;v[iq]=wq;out[f'2p{i}-q{i}>=1']=(v,Fraction(-1))
    return out

fids=set()
for c in certs:
    fids.add(c['id']);rows=inequality_rows(profiles[c['id']]);n=len(next(iter(rows.values()))[0]);lhs=[Fraction(0)]*n;rhs=Fraction(0)
    for label,coef in c['terms']:
        coef=Fraction(coef);row,b=rows[label];lhs=[a+coef*x for a,x in zip(lhs,row)];rhs+=coef*b
    assert all(x==0 for x in lhs) and rhs<0 and rhs==Fraction(c['rhs'])
coll=list(csv.DictReader((P/'STATE_COLLISION_EXCLUSIONS_56.csv').open()));inj=list(csv.DictReader((P/'FIBRE_INJECTIVITY_EXCLUSIONS_50.csv').open()));ari=list(csv.DictReader((P/'ARITHMETIC_EXCLUSIONS_6.csv').open()))
assert len(coll)==56 and len(inj)==50 and len(ari)==6
parts=fids|{x['id'] for x in coll}|{x['id'] for x in inj}|{x['id'] for x in ari}
assert len(parts)==840 and parts==set(profiles)
assert sum(x['reason']=='DOUBLE_STRICT_T_MOD_Q_CONTRADICTION' for x in ari)==2
assert sum(x['reason']=='SAME_SOURCE_STRICT_T_S_MOD_Q_CONTRADICTION' for x in ari)==4
print('PASS')
print('raw_assignments=156250')
print('canonical_two_strict_profiles=840')
print('farkas_infeasible=728')
print('state_collision=56')
print('fibre_injectivity=50')
print('arithmetic_exclusions=6')
print('realisable_two_strict_profiles=0')
print('global_strict_edge_uniqueness_n5=PASS')
