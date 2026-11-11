import json,itertools,csv
raw=json.load(open('/tmp/raw_multistrict_profiles.json'))
perms=list(itertools.permutations(range(5)))
def canon(T,S,strict):
 best=None
 for perm in perms:
  inv=[0]*5
  for old,new in enumerate(perm):inv[new]=old
  for sw in (0,1):
   A,B=(S,T) if sw else (T,S)
   nA=[];nB=[]
   for ns in range(5):
    os=inv[ns];nA.append(perm[A[os]]);nB.append(perm[B[os]])
   st=tuple(sorted(((1-g if sw else g),perm[s],f) for g,s,f in strict))
   key=(tuple(nA),tuple(nB),st)
   if best is None or key<best:best=key
 return best
D={}
for r in raw:
 k=canon(tuple(r['T']),tuple(r['S']),tuple(tuple(x) for x in r['strict']))
 D[k]=D.get(k,0)+1
print('canonical',len(D))
rows=[]
for i,(k,n) in enumerate(sorted(D.items(),key=lambda kv:repr(kv[0])),1):
 T,S,st=k;rows.append({'id':f'RMS{i:04d}','T':','.join(map(str,T)),'S':','.join(map(str,S)),'strict_edges':'|'.join(f'{"T" if g==0 else "S"}{s}:r{f}' for g,s,f in st),'labeled_origins':n})
with open('/tmp/raw_multistrict_canonical.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
