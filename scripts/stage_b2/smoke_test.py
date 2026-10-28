#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math, shutil, struct, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE/"_smoke"
if ROOT.exists(): shutil.rmtree(ROOT)
CK=ROOT/"checkpoint"; CUR=CK/"cur"; CUR.mkdir(parents=True)
REC=struct.Struct("<Q")
BUCKETS=128
STATES={(586,805),(528,857),(1229,2269),(1073,1333),(534,1567)}

def pack(a,b): return (a<<32)|b
def mix64(x):
    m=(1<<64)-1;x=(x+0x9e3779b97f4a7c15)&m;x=((x^(x>>30))*0xbf58476d1ce4e5b9)&m;x=((x^(x>>27))*0x94d049bb133111eb)&m;return x^(x>>31)
def T(a,b):
    r=(10*a)%b
    if not r:return (0,1)
    g=math.gcd(r,b);return r//g,b//g
def S(a,b):
    if not a or 2*a<b:return None
    r=(10*(b-a))%a;d=a+r;g=math.gcd(a,d);return a//g,d//g
def hit(a,b):return a<b and b>1_100_000*(b-a)
def viable(b,remaining): return (b << ((remaining+1)//2))>1_100_000
TERMINAL={(2,11),(9,11),(0,1),(1,1),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(7,8),(7,9),(7,10),(4,11),(7,11),(7,12),(2,13),(5,13),(6,13),(7,13),(8,13),(11,13),(11,20)}
by=[[] for _ in range(BUCKETS)]
for a,b in STATES: by[mix64(pack(a,b))&127].append(pack(a,b))
lines=[]
for i,v in enumerate(by):
    p=CUR/f"b{i:04d}.bin";p.write_bytes(b"".join(REC.pack(x) for x in sorted(v)))
    lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  cur/{p.name}")
manifest=ROOT/"hashes.txt";manifest.write_text("\n".join(lines)+"\n")
cmd=[sys.executable,str(HERE/"run_stage_b2.py"),"--checkpoint-root",str(CK),"--hash-manifest",str(manifest),"--work-root",str(ROOT/"work"),"--start-time","83","--end-time","90","--jobs","2","--merge-jobs","2","--minimum-free-gb","0","--allow-noncanonical","--full-checkpoint-audit"]
subprocess.run(cmd,check=True)
front=set(STATES)
for t in range(83,90):
    nxt=set()
    for a,b in front:
        for y in (T(a,b),S(a,b)):
            if y is None or hit(*y) or y in TERMINAL or not viable(y[1],211-(t+1)):continue
            nxt.add(y)
    front=nxt
final=ROOT/"work"/"level_090"
got=set()
for p in sorted(final.glob("b????.bin")):
    data=p.read_bytes();got.update((x>>32,x&0xffffffff) for (x,) in struct.iter_unpack("<Q",data))
assert got==front,(len(got),len(front))
print(json.dumps({"status":"PASS","final_time":90,"states":len(got)},indent=2))
