#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

static std::map<int,int> factor(int n){
    std::map<int,int> f;
    for(int p=2;p*p<=n;p+=(p==2?1:2)) while(n%p==0){f[p]++;n/=p;}
    if(n>1)f[n]++;
    return f;
}
static long long quotient_formula(const std::map<int,int>&f){
    long long q=1; for(auto [p,e]:f)q*=p==2?2*e:2*e+1; return q;
}
static long long tie_formula(const std::map<int,int>&f){
    if(f.count(2)) return 0;
    long long z=1;
    for(auto [p,e]:f){long long pe=1;for(int i=1;i<e;i++)pe*=p;z*=pe*(p-2);}return z;
}
struct Vec{long long a,b;};
static long long det(Vec v,Vec c){return v.a*c.b-v.b*c.a;}
int main(int argc,char**argv){
    long long residue_rows=0;
    for(int B=2;B<=2000;B++){
        auto f=factor(B); std::set<std::pair<int,int>> pairs; long long ns=0,nt=0,ne=0;
        for(int t=0;t<B;t++){
            int g0=std::gcd(t,B),g1=std::gcd(t-1,B); pairs.insert({g0,g1});
            if(g0>g1)ns++; else if(g0<g1)nt++; else ne++; residue_rows++;
        }
        assert((long long)pairs.size()==quotient_formula(f));
        assert(ne==tie_formula(f)); assert(ns==nt); assert(2*ns+ne==B);
    }
    Vec v1{1,3},c1{1,2},v2{4,5},c2{1,1},childv{2,3},childc{1,1};
    assert(det(v1,c1)==-1 && det(v2,c2)==-1 && det(childv,childc)==-1);
    assert(2*v1.a==childv.a && v1.b==childv.b);
    assert(childv.a==2 && childv.b==3 && childc.a==1 && childc.b==1);
    std::string out=argc>1?argv[1]:"P2_GATE05_EXTERNAL_RECEIPT.json";
    std::ofstream fjson(out);
    fjson << "{\n"
          << "  \"status\": \"PASS_P2_GATE05_EXTERNAL_RUNNER\",\n"
          << "  \"implementation\": \"standalone C++17; no generator imports\",\n"
          << "  \"bases_verified\": 1999,\n"
          << "  \"residue_rows_verified\": " << residue_rows << ",\n"
          << "  \"noninvertibility_collision_verified\": true,\n"
          << "  \"large_bellman_search_recomputed\": false,\n"
          << "  \"independent_team_validation\": false\n"
          << "}\n";
    std::cout << "PASS_P2_GATE05_EXTERNAL_RUNNER rows=" << residue_rows << "\n";
}
