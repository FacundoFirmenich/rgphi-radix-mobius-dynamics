#include <bits/stdc++.h>
using namespace std;
static inline uint64_t pack(uint64_t a,uint64_t b){ if(a>=0x100000000ULL||b>=0x100000000ULL){cerr<<"PACK_OVERFLOW "<<a<<"/"<<b<<"\n"; exit(3);} return (a<<32)|b; }
static inline pair<uint64_t,uint64_t> unpack(uint64_t k){return {k>>32,k&0xffffffffULL};}
static inline uint64_t mix64(uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);} 
struct FlatSet{
 vector<uint64_t> t; size_t mask,sz=0; FlatSet(int pow2):t(1ULL<<pow2,0),mask(t.size()-1){}
 bool insert(uint64_t k){size_t i=mix64(k)&mask; while(1){uint64_t q=t[i]; if(q==k)return false; if(q==0){t[i]=k;sz++; if(sz*10>t.size()*8){cerr<<"LOAD_EXCEEDED "<<sz<<"/"<<t.size()<<"\n"; exit(4);} return true;} i=(i+1)&mask;}}
};
static inline bool term(uint64_t a,uint64_t b){static const pair<uint32_t,uint32_t>x[]={{2,11},{9,11},{0,1},{1,1},{1,2},{1,3},{2,3},{3,4},{4,5},{5,6},{7,8},{7,9},{7,10},{4,11},{7,11},{7,12},{2,13},{5,13},{6,13},{7,13},{8,13},{11,13},{11,20}};for(auto [p,q]:x)if(a==p&&b==q)return 1;return 0;}
static inline uint64_t Tk(uint64_t key){auto[a,b]=unpack(key); __uint128_t z=(__uint128_t)10*a; uint64_t d=z/b,r=(uint64_t)(z-(__uint128_t)d*b),g=gcd(r,b); return pack(r/g,b/g);} 
static inline bool Sk(uint64_t key,uint64_t& out){auto[a,b]=unpack(key); if(!a||2*a<b)return 0; __uint128_t z=(__uint128_t)10*(b-a); uint64_t d=(uint64_t)(z/a); __uint128_t B=(__uint128_t)10*b-(__uint128_t)(9+d)*a; if(!B||B>=0x100000000ULL)return 0; uint64_t bb=(uint64_t)B,g=gcd(a,bb); out=pack(a/g,bb/g); return 1;}
static inline bool hit(uint64_t key,uint64_t Q){auto[a,b]=unpack(key); return (__uint128_t)b>(__uint128_t)Q*(b-a);} 
static inline bool viable(uint64_t key,int rem,uint64_t Q){auto[a,b]=unpack(key); int e=(rem+1)/2; __uint128_t mb=b; if(e>=64)return true; mb<<=e; return mb>Q;}
int main(int argc,char**argv){ if(argc<8){cerr<<"a b Q prefix maxTotal forbid tablePow [report]\n";return 2;} uint64_t a=stoull(argv[1]),b=stoull(argv[2]),Q=stoull(argv[3]); int prefix=stoi(argv[4]),H=stoi(argv[5]); bool forbid=stoi(argv[6]); int tp=stoi(argv[7]); int report=argc>8?stoi(argv[8]):10;
 FlatSet seen(tp); vector<uint64_t> cur,nxt; cur.push_back(pack(a,b)); seen.insert(cur[0]); uint64_t pruned=0; size_t maxfront=1; uint64_t maxb=0;
 for(int d=0;prefix+d<=H;d++){int total=prefix+d; for(uint64_t k:cur) if(hit(k,Q)){auto[x,y]=unpack(k);cout<<"FOUND total="<<total<<" endpoint="<<x<<"/"<<y<<" seen="<<seen.sz<<" pruned="<<pruned<<"\n";return 0;} if(total==H)break; int rem=H-(total+1); nxt.clear(); nxt.reserve(cur.size()*2);
   for(uint64_t k:cur){uint64_t ys[2];int n=0;ys[n++]=Tk(k);uint64_t s;if(Sk(k,s))ys[n++]=s; for(int i=0;i<n;i++){auto[x,y]=unpack(ys[i]); if((forbid&&x==39&&y==59)||term(x,y))continue; if(!viable(ys[i],rem,Q)){pruned++;continue;} if(seen.insert(ys[i]))nxt.push_back(ys[i]);}}
   cur.swap(nxt); maxfront=max(maxfront,cur.size()); if(report&&((d+1)%report==0||cur.empty())){maxb=0;for(auto k:cur)maxb=max(maxb,unpack(k).second);cerr<<"total="<<total+1<<" front="<<cur.size()<<" seen="<<seen.sz<<" pruned="<<pruned<<" maxb="<<maxb<<" load="<<(double)seen.sz/seen.t.size()<<"\n";} if(cur.empty())break;
 }
 cout<<"NO_HIT total<="<<H<<" seen="<<seen.sz<<" pruned="<<pruned<<" maxfront="<<maxfront<<"\n";
}
