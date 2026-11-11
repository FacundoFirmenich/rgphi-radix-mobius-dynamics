#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

struct Rat {
    std::int64_t n, d;
    Rat(std::int64_t a=0, std::int64_t b=1) {
        assert(b != 0);
        if (b < 0) { a = -a; b = -b; }
        auto g = std::gcd(a < 0 ? -a : a, b);
        n = a/g; d = b/g;
    }
};

static Rat T(const Rat& x, std::int64_t B) {
    std::int64_t q = (B*x.n)/x.d;
    return Rat(B*x.n-q*x.d, x.d);
}
static Rat S(const Rat& x, std::int64_t B) {
    assert(2*x.n >= x.d && x.n != 0);
    std::int64_t un = x.d-x.n, ud=x.n;
    std::int64_t q=(B*un)/ud;
    std::int64_t rn=B*un-q*ud;
    return Rat(ud,ud+rn);
}
static bool eq(const Rat& a,const Rat& b){return a.n==b.n&&a.d==b.d;}
static std::int64_t qnum(const Rat& x){return x.d;}
static std::int64_t qden(const Rat& x){return x.d-x.n;}
static bool q_gt(const Rat& x, std::int64_t tn, std::int64_t td){
    return qnum(x)*td > tn*qden(x);
}

int main(int argc,char** argv){
    std::uint64_t rows=0;
    for(int r=3;r<=12;r++){
        std::int64_t B=std::int64_t{1}<<r;
        Rat v(B+1,2*B+1), s=S(v,B), t1=T(v,B), t2=T(t1,B);
        assert(eq(s,Rat(B+1,B+2)));
        assert(eq(t1,Rat(B/2,2*B+1)));
        assert(eq(t2,Rat(7*B/4+1,2*B+1)));
        std::int64_t q0n=2*B+1,q0d=B;
        std::int64_t qttn=2*B+1,qttd=B/4;
        std::int64_t qsn=B+2,qsd=1;
        std::int64_t lown=q0n*qttd+qttn*q0d, lowd=2*q0d*qttd;
        std::int64_t midn=qttn*qsd+qsn*qttd, midd=2*qttd*qsd;
        for(std::int64_t phase=0;phase<B;phase++){
            auto kT=std::gcd(phase-1<0?1-phase:phase-1,B);
            auto kS=std::gcd(phase,B);
            char act=kS>kT?'S':'T';
            assert(act==(phase%2==0?'S':'T'));
            assert(q_gt(s,lown,lowd));
            assert(!q_gt(t1,lown,lowd));
            assert(q_gt(t2,lown,lowd));
            assert(q_gt(s,midn,midd));
            assert(!q_gt(t1,midn,midd));
            assert(!q_gt(t2,midn,midd));
            assert(!q_gt(s,qsn,qsd));
            assert(!q_gt(t1,qsn,qsd));
            assert(!q_gt(t2,qsn,qsd));
            rows+=3;
        }
    }
    std::vector<char> expected={'S','T','S','S','T','T'};
    for(int t=0;t<6;t++){
        int kT=std::gcd(std::abs(t-1),6), kS=std::gcd(t,6);
        char a=kS>kT?'S':'T';
        assert(a==expected.at(t));
    }
    assert(expected[0]!=expected[1]);
    assert(expected[0]!=expected[4]);
    assert(expected[2]!=expected[5]);
    Rat parent(61913,88527);
    assert(eq(T(parent,10),Rat(87968,88527)));
    assert(eq(S(parent,10),Rat(61913,80401)));
    std::string out = argc>1 ? argv[1] : "P2_EXTERNAL_REPLICATION_RECEIPT.json";
    std::ofstream f(out);
    f << "{\n"
      << "  \"status\": \"PASS_EXTERNAL_RUNNER_CLEANROOM\",\n"
      << "  \"implementation\": \"standalone C++17; no generator imports\",\n"
      << "  \"power2_rows_verified\": " << rows << ",\n"
      << "  \"power2_bases_verified\": 10,\n"
      << "  \"crt6_rows_verified\": 6,\n"
      << "  \"rgphi_transitions_verified\": 2,\n"
      << "  \"independent_team_validation\": false,\n"
      << "  \"scope\": \"symbolic arithmetic and finite theorem audit; archived Bellman certificates are not recomputed\"\n"
      << "}\n";
    std::cout << "PASS_EXTERNAL_RUNNER_CLEANROOM rows=" << rows << "\n";
}
