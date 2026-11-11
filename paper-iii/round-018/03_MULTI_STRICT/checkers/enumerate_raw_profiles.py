from collections import deque
import itertools,time,json

def strongly(T,S):
 for st in range(5):
  seen={st};q=[st]
  while q:
   u=q.pop()
   for v in (T[u],S[u]):
    if v not in seen:seen.add(v);q.append(v)
  if len(seen)<5:return False
 return True

def diam(T,S):
 mx=0
 for st in range(5):
  d=[-1]*5;d[st]=0;q=deque([st])
  while q:
   u=q.popleft()
   for v in (T[u],S[u]):
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  if -1 in d:return 99
  mx=max(mx,max(d))
 return mx

def crossing(T,S):
 for i in range(5):
  j=T[i]
  if j!=i and S[j]==i:return True
  j=S[i]
  if j!=i and T[j]==i:return True
 return False

def cycles(T,S):
 out=[];keys=set()
 for st in range(5):
  def dfs(u,verts,es):
   for g,v in ((0,T[u]),(1,S[u])):
    e=(u,g,v)
    if v==st:
     c=es+[e];key=min(tuple(c[k:]+c[:k]) for k in range(len(c)))
     if key not in keys:keys.add(key);out.append(c)
    elif v not in verts:dfs(v,verts|{v},es+[e])
  dfs(st,{st},[])
 return out

def gen_ham(word):
 BT=[None]*5;BS=[None]*5;cy=[]
 for i,ch in enumerate(word):
  j=(i+1)%5;g=0 if ch=='T' else 1;cy.append((i,g,j));(BT if g==0 else BS)[i]=j
 for alts in itertools.product(range(5),repeat=5):
  T=BT.copy();S=BS.copy()
  for i,a in enumerate(alts):
   if T[i] is None:T[i]=a
   else:S[i]=a
  yield tuple(T),tuple(S),cy

def gen_core(word):
 BT=[None]*5;BS=[None]*5;cy=[]
 for i,ch in enumerate(word):
  j=(i+1)%4;g=0 if ch=='T' else 1;cy.append((i,g,j));(BT if g==0 else BS)[i]=j
 free=[]
 for i in range(4):free.append((i,1 if BT[i] is not None else 0))
 free +=[(4,0),(4,1)]
 for vals in itertools.product(range(5),repeat=6):
  T=BT.copy();S=BS.copy()
  for (i,g),v in zip(free,vals):(T if g==0 else S).__setitem__(i,v)
  yield tuple(T),tuple(S),cy

profiles=set(); maps=0; basepass=0
for kind,word,gen,L in [('H','TSTSS',gen_ham,5),('C','TSTS',gen_core,4)]:
 for strict_idx in range(L):
  sg=0 if word[strict_idx]=='T' else 1;ss=strict_idx;marked=(sg,ss)
  for f1 in (2,3):
   for T,S,basecy in gen(word):
    maps+=1
    if not strongly(T,S) or crossing(T,S) or diam(T,S)<=2:continue
    cs=cycles(T,S); ced=[];eligible=[True]*10;okmarked=True
    for c in cs:
     ids={(g,a) for a,g,b in c};mt=sum(g==0 for a,g,b in c);ms=len(c)-mt;ced.append((ids,mt,ms))
     if marked in ids and min(mt,ms)<2:okmarked=False;break
     if min(mt,ms)<2:
      for g,a in ids:eligible[2*a+g]=False
    if not okmarked:continue
    basepass+=1
    for e in range(10):
     g2=e%2;s2=e//2
     if (g2,s2)==marked or not eligible[e]:continue
     if any(marked in ids and (g2,s2) in ids for ids,_,__ in ced):continue
     for f2 in (2,3):
      profiles.add((T,S,tuple(sorted(((sg,ss,f1),(g2,s2,f2))))))
print('maps',maps,'basepass',basepass,'labeled unique profiles',len(profiles))
open('/tmp/raw_multistrict_profiles.json','w').write(json.dumps([{'T':x[0],'S':x[1],'strict':x[2]} for x in profiles]))
