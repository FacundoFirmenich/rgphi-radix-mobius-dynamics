from fractions import Fraction
import csv, math, itertools, collections, json

class WDSU:
 def __init__(self,n): self.p=list(range(n)); self.w=[Fraction(1) for _ in range(n)] # x_i = w_i*x_parent
 def find(self,x):
  if self.p[x]!=x:
   p=self.p[x]; r=self.find(p); self.w[x]*=self.w[p]; self.p[x]=r
  return self.p[x]
 def weight(self,x): self.find(x); return self.w[x]
 def union_rel(self,i,j,f): # x_i = f*x_j
  ri=self.find(i); rj=self.find(j); wi=self.w[i]; wj=self.w[j]
  if ri==rj: return wi==f*wj
  # set root_i under root_j: wi*x_ri = f*wj*x_rj => x_ri=f*wj/wi*x_rj
  self.p[ri]=rj; self.w[ri]=f*wj/wi; return True

def parse_edges(s):
 out=[]
 for part in s.split('|'):
  g=0 if part[0]=='T' else 1; rest=part[1:];out.append((g,int(rest.split(':')[0]),int(rest.split('r')[1])))
 return out

def normalize_ineq(coeff,b,mult):
 # Fractions -> integer primitive, don't multiply by negative
 dens=[x.denominator for x in coeff]+[b.denominator]
 l=1
 for d in dens:l=math.lcm(l,d)
 ints=[int(x*l) for x in coeff]; bi=int(b*l); mi=[x*l for x in mult]
 g=0
 for x in ints+[bi]:g=math.gcd(g,abs(x))
 if g>1: ints=[x//g for x in ints];bi//=g;mi=[x/g for x in mi]
 return tuple(Fraction(x) for x in ints),Fraction(bi),tuple(mi)

def dedup(ineqs):
 best={}
 for c,b,m in ineqs:
  c,b,m=normalize_ineq(c,b,m)
  if c not in best or b<best[c][0]:best[c]=(b,m)
 return [(c,b,m) for c,(b,m) in best.items()]

def fm_infeasible(A,b):
 n=len(A[0]); m0=len(A)
 ineq=[]
 for i,(row,bi) in enumerate(zip(A,b)):
  mult=[Fraction(0)]*m0;mult[i]=1
  ineq.append((tuple(map(Fraction,row)),Fraction(bi),tuple(mult)))
 ineq=dedup(ineq)
 for k in range(n):
  pos=[];neg=[];zero=[]
  for c,bi,m in ineq:
   if c[k]>0:pos.append((c,bi,m))
   elif c[k]<0:neg.append((c,bi,m))
   else:zero.append((c,bi,m))
  new=list(zero)
  if pos and neg:
   for cp,bp,mp in pos:
    ap=cp[k]
    for cn,bn,mn in neg:
     an=cn[k]
     # (-an)*pos + ap*neg
     cc=tuple((-an)*cp[j]+ap*cn[j] for j in range(n))
     bb=(-an)*bp+ap*bn
     mm=tuple((-an)*mp[j]+ap*mn[j] for j in range(m0))
     new.append((cc,bb,mm))
  # if only one sign, inequalities involving k can be satisfied by +/- infinity, discard
  ineq=dedup(new)
  # immediate contradiction
  for c,bi,m in ineq:
   if all(x==0 for x in c) and bi<0:return True,m,bi,ineq
  if len(ineq)>200000: print('blow',k,len(ineq));return None,None,None,ineq
 return False,None,None,ineq

def build(r):
 T=tuple(map(int,r['T'].split(',')));S=tuple(map(int,r['S'].split(',')));strict=parse_edges(r['strict_edges']);sd={(g,s):f for g,s,f in strict}
 pd=WDSU(5);qd=WDSU(5)
 for i in range(5):
  if not qd.union_rel(i,T[i],Fraction(sd.get((0,i),1))):return 'REL_CONFLICT',None
  if not pd.union_rel(i,S[i],Fraction(sd.get((1,i),1))):return 'REL_CONFLICT',None
 # roots and variables
 proots=sorted({pd.find(i) for i in range(5)});qroots=sorted({qd.find(i) for i in range(5)})
 idx={('p',r):i for i,r in enumerate(proots)};idx.update({('q',r):len(proots)+i for i,r in enumerate(qroots)})
 # forced state collision exact same coordinate ratios? State equality if p_i/q_i same, not simply same roots. check later not needed FM
 A=[];b=[];labels=[]
 nv=len(proots)+len(qroots)
 for i in range(5):
  pr=pd.find(i);qr=qd.find(i);wp=pd.weight(i);wq=qd.weight(i);ip=idx[('p',pr)];iq=idx[('q',qr)]
  row=[Fraction(0)]*nv;row[ip]=-wp;A.append(row);b.append(Fraction(-1));labels.append(f'p{i}>=1')
  row=[Fraction(0)]*nv;row[ip]=wp;row[iq]=-wq;A.append(row);b.append(Fraction(-1));labels.append(f'q{i}-p{i}>=1')
  row=[Fraction(0)]*nv;row[ip]=-2*wp;row[iq]=wq;A.append(row);b.append(Fraction(-1));labels.append(f'2p{i}-q{i}>=1')
 return 'OK',(A,b,labels,pd,qd,T,S,strict,idx)

rows=list(csv.DictReader(open('/tmp/raw_multistrict_canonical.csv')))
st=collections.Counter();certs=[];feas=[]
for r in rows:
 status,data=build(r)
 if status!='OK':st[status]+=1;continue
 A,b,labels,*rest=data
 inf,mult,bi,last=fm_infeasible(A,b)
 if inf:
  st['INFEAS']+=1
  used=[(labels[i],str(v)) for i,v in enumerate(mult) if v]
  certs.append({'id':r['id'],'strict_edges':r['strict_edges'],'T':r['T'],'S':r['S'],'rhs':str(bi),'terms':used})
 elif inf is False:
  st['FM_NOT_INFEAS']+=1;feas.append(r)
 else:st['UNKNOWN']+=1
print(st,'feas',len(feas))
print('first certs');print(json.dumps(certs[:5],indent=2))
open('/tmp/multistrict_farkas.json','w').write(json.dumps(certs,indent=2))
