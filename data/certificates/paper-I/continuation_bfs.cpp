#include <bits/stdc++.h>
using namespace std;

static inline uint64_t pack(uint64_t a,uint64_t b){
    if(a>=0x100000000ULL||b>=0x100000000ULL){
        cerr<<"PACK_OVERFLOW "<<a<<"/"<<b<<"\n"; exit(3);
    }
    return (a<<32)|b;
}
static inline pair<uint64_t,uint64_t> unpack(uint64_t k){return {k>>32,k&0xffffffffULL};}
static inline uint64_t mix64(uint64_t x){
    x+=0x9e3779b97f4a7c15ULL;
    x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
    x=(x^(x>>27))*0x94d049bb133111ebULL;
    return x^(x>>31);
}
struct FlatSet{
    vector<uint64_t> t; size_t mask,sz=0;
    explicit FlatSet(int p):t(1ULL<<p,0),mask(t.size()-1){}
    bool insert(uint64_t k){
        size_t i=mix64(k)&mask;
        while(true){
            uint64_t q=t[i];
            if(q==k) return false;
            if(q==0){t[i]=k;sz++; if(sz*10>t.size()*7){cerr<<"LOAD_EXCEEDED\n";exit(4);} return true;}
            i=(i+1)&mask;
        }
    }
};
static inline bool terminal(uint64_t a,uint64_t b){
    static const pair<uint32_t,uint32_t> x[]={
        {2,11},{9,11},{0,1},{1,1},{1,2},{1,3},{2,3},{3,4},{4,5},{5,6},
        {7,8},{7,9},{7,10},{4,11},{7,11},{7,12},{2,13},{5,13},{6,13},
        {7,13},{8,13},{11,13},{11,20}
    };
    for(auto [p,q]:x) if(a==p&&b==q) return true;
    return false;
}
static inline uint64_t T(uint64_t key){
    auto [a,b]=unpack(key); __uint128_t z=(__uint128_t)10*a;
    uint64_t d=(uint64_t)(z/b), r=(uint64_t)(z-(__uint128_t)d*b), g=std::gcd(r,b);
    return pack(r/g,b/g);
}
static inline bool S(uint64_t key,uint64_t& out){
    auto [a,b]=unpack(key); if(a==0||2*a<b) return false;
    __uint128_t z=(__uint128_t)10*(b-a); uint64_t d=(uint64_t)(z/a);
    __uint128_t B=(__uint128_t)10*b-(__uint128_t)(9+d)*a;
    if(B==0||B>=0x100000000ULL) return false;
    uint64_t bb=(uint64_t)B,g=std::gcd(a,bb); out=pack(a/g,bb/g); return true;
}
static inline bool hit(uint64_t key,uint64_t Q){
    auto [a,b]=unpack(key); return a<b && (__uint128_t)b>(__uint128_t)Q*(b-a);
}
static inline uint64_t comm_hash(const vector<uint64_t>& v){
    uint64_t h=0;
    for(uint64_t k:v) h ^= mix64(k+0xd6e8feb86659fd93ULL);
    return h;
}
int main(int argc,char**argv){
    if(argc<8){cerr<<"sa sb Q max_local_depth table_pow label output_csv\n";return 2;}
    uint64_t sa=stoull(argv[1]), sb=stoull(argv[2]), Q=stoull(argv[3]);
    int H=stoi(argv[4]), tp=stoi(argv[5]); string label=argv[6], outp=argv[7];
    FlatSet seen(tp); vector<uint64_t> cur{pack(sa,sb)}, nxt; seen.insert(cur[0]);
    ofstream out(outp); out<<"label,local_depth,frontier_size,seen_size,max_denominator,frontier_xor_hash,hit_count,first_hit_state\n";
    for(int d=0; d<=H; ++d){
        uint64_t maxb=0; vector<uint64_t> hits;
        for(uint64_t k:cur){ auto [a,b]=unpack(k); maxb=max(maxb,b); if(hit(k,Q)) hits.push_back(k); }
        string first=""; if(!hits.empty()){auto [a,b]=unpack(hits[0]); first=to_string(a)+"/"+to_string(b);}        
        out<<label<<","<<d<<","<<cur.size()<<","<<seen.sz<<","<<maxb<<","<<hex<<setw(16)<<setfill('0')<<comm_hash(cur)<<dec<<","<<hits.size()<<","<<first<<"\n";
        if(!hits.empty()){
            cout<<"FOUND label="<<label<<" depth="<<d<<" state="<<first<<" seen="<<seen.sz<<"\n"; return 0;
        }
        if(d==H) break;
        nxt.clear(); nxt.reserve(cur.size()*2);
        for(uint64_t k:cur){
            uint64_t ys[2]; int n=0; ys[n++]=T(k); uint64_t s; if(S(k,s)) ys[n++]=s;
            for(int i=0;i<n;i++){
                auto [a,b]=unpack(ys[i]);
                if(terminal(a,b)) continue;
                if(seen.insert(ys[i])) nxt.push_back(ys[i]);
            }
        }
        cur.swap(nxt);
        if(d<5 || (d+1)%10==0) cerr<<label<<" d="<<d+1<<" front="<<cur.size()<<" seen="<<seen.sz<<"\n";
        if(cur.empty()) break;
    }
    cout<<"NO_HIT label="<<label<<" depth<="<<H<<" seen="<<seen.sz<<"\n"; return 1;
}
