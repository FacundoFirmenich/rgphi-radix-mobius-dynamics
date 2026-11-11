#include <bits/stdc++.h>
using namespace std;
vector<int> spf;
vector<long long> divisors_ll(long long n){
 vector<pair<long long,int>> fac;
 while(n>1){ long long p = n<(long long)spf.size()?spf[n]:0; if(!p){p=2;while(p*p<=n&&n%p)p++;if(p*p>n)p=n;}int e=0;while(n%p==0){n/=p;e++;}fac.push_back({p,e});}
 vector<long long> ds={1};for(auto [p,e]:fac){int sz=ds.size();long long pp=1;for(int j=1;j<=e;j++){pp*=p;for(int i=0;i<sz;i++)ds.push_back(ds[i]*pp);}}return ds;
}
int main(int argc,char**argv){int Z=argc>1?atoi(argv[1]):5000;int maxn=11*Z+10;spf.resize(maxn+1);for(int i=2;i<=maxn;i++)if(!spf[i]){spf[i]=i;if(1LL*i*i<=maxn)for(long long j=1LL*i*i;j<=maxn;j+=i)if(!spf[j])spf[j]=i;}
 long long divisor_core=0,primitive_core=0,cubic=0;
 for(long long z=2;z<=Z;z++)for(long long h=1;h<z;h++){
   if(3*h==z) continue;
   long long u=9*z-2*h,v=9*z+2*h;
   auto du=divisors_ll(u),dv=divisors_ll(v);unordered_set<long long> seen;
   for(long long x:du)for(long long y:dv){long long C=x*y;if(C<=9*z||!seen.insert(C).second)continue;if((C+z)&1)continue;long long A=(C+z)/2;if(A<=5*z)continue;long long Q=C+h;long long F=(3*h-z)*(h+z);if(F%Q)continue;divisor_core++;
     long long w=z-h,D=A+z;if(gcd(C,Q)!=1||gcd(C,3*D)!=1||gcd(A,Q)!=1||gcd(A,D)!=1)continue;primitive_core++;
     __int128 H=(__int128)z*z*z+(__int128)w*w*w;if(H%A)continue;cubic++;cout<<A<<","<<z<<","<<h<<"\n";
   }
 }
 cerr<<"Z="<<Z<<" divisor_core="<<divisor_core<<" primitive_core="<<primitive_core<<" cubic="<<cubic<<"\n";
}
