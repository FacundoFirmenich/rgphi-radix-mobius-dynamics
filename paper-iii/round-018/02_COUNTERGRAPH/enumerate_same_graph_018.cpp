#include <bits/stdc++.h>
using namespace std; using i128=__int128_t;
long long eg(long long a,long long b,long long&x,long long&y){if(!b){x=1;y=0;return a;}long long x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
long long invmod(long long a,long long m){long long x,y;if(eg(a,m,x,y)!=1)return -1;x%=m;if(x<0)x+=m;return x;}
pair<long long,long long> crt2(long long a,long long m,long long b,long long n){ long long x,y; long long g=eg(m,n,x,y); if((b-a)%g) return {-1,-1}; long long l=m/g*n; long long t=(long long)((i128)((b-a)/g) * x % (n/g)); long long r=(a+(i128)m*t)%l; if(r<0)r+=l; return {r,l}; }
vector<int> roots1mod(int n, const vector<int>&spf){int x=n; vector<pair<int,int>> pp; while(x>1){int p=spf[x],pe=1,e=0;while(x%p==0){x/=p;pe*=p;e++;}pp.push_back({pe,e});}
 vector<pair<long long,long long>> sols={{0,1}};
 for(auto [pe,e]:pp){int p=spf[pe]; vector<int> local; if(p!=2){local={1,pe-1};} else if(e==1){local={1};} else if(e==2){local={1,3};} else {local={1,pe-1,1+pe/2,pe/2-1};}
  vector<pair<long long,long long>> ns; for(auto [a,m]:sols)for(int b:local)ns.push_back(crt2(a,m,b,pe)); sols.swap(ns);
 }
 vector<int> r; for(auto [a,m]:sols){int v=(int)(a%n); if(v!=1) r.push_back(v);} sort(r.begin(),r.end()); r.erase(unique(r.begin(),r.end()),r.end()); return r;}
bool crt_cons(const vector<pair<long long,long long>>&c){for(int i=0;i<(int)c.size();i++)for(int j=0;j<i;j++){long long g=gcd(c[i].second,c[j].second);if((c[i].first-c[j].first)%g)return false;}return true;}
bool check(const array<long long,5>&p,const array<long long,5>&q, vector<pair<long long,long long>>&con){array<int,5>T={0,2,1,4,3},S={1,0,4,1,2}; con.clear(); set<pair<long long,long long>>st;
 for(int i=0;i<5;i++){if(!(p[i]<q[i]&&2*p[i]>q[i])||gcd(p[i],q[i])!=1)return false;if(!st.insert({p[i],q[i]}).second)return false;}
 for(int i=0;i<5;i++){
  int j=T[i]; if(q[i]!=q[j])return false; long long iv=invmod(p[i],q[i]); if(iv<0)return false; long long res=(long long)((i128)p[j]*iv%q[i]); if(gcd(res,q[i])!=1)return false;con.push_back({res,q[i]});
  j=S[i]; long long h=(i==3?3:1); if(p[i]!=h*p[j])return false; long long ci=q[i]-p[i],cj=q[j]-p[j],iv2=invmod(ci,p[i]);if(iv2<0)return false; long long rs=(long long)((i128)h*cj%p[i]*iv2%p[i]);if(gcd(rs,p[i])!=h)return false;con.push_back({rs,p[i]});
 }
 return crt_cons(con);
}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):15000; vector<int>spf(3*N+1); for(int i=2;i<=3*N;i++)if(!spf[i]){spf[i]=i;if((long long)i*i<=3*N)for(long long j=1LL*i*i;j<=3*N;j+=i)if(!spf[j])spf[j]=i;} for(int i=2;i<=3*N;i++)if(!spf[i])spf[i]=i;
 vector<vector<int>> R2(3*N+1);for(int m=2;m<=3*N;m++)R2[m]=roots1mod(m,spf);
 long long cand=0,hits=0; cout<<"A,C,Q0,Q1,D,k,B0,M\n";
 for(int Q1=2;Q1<=N;Q1++)for(int b:R2[Q1])for(int A=Q1/2+1;A<Q1;A++)if(gcd(A,Q1)==1){int C=1LL*b*A%Q1;if(C<=Q1/2||C==A||1LL*b*C%Q1!=A)continue;for(int bs:R2[A]){int a0=1LL*bs*(Q1-A)%A;if(a0==0||1LL*bs*a0%A!=(Q1-A)%A)continue;long long Q0=A+a0;for(int k:{-2,-1}){long long D=3*Q0+1LL*k*A;if(D<2||D>3LL*N)continue;array<long long,5>p={A,A,C,3LL*A,C},q={Q0,Q1,Q1,D,D};vector<pair<long long,long long>>con;cand++;if(!check(p,q,con))continue;
 long long r=0,m=1; bool ok=true; for(auto [aa,n]:con){long long g=std::gcd(m,n); if((aa-r)%g){ok=false;break;} long long m1=m/g,n1=n/g; long long inv=invmod(m1%n1,n1); long long t=(long long)((i128)((aa-r)/g%n1+n1)%n1*inv%n1); r=(long long)(((i128)m*t+r)%(m*n1)); m*=n1; if(r<0)r+=m;} if(!ok)continue;
 cout<<A<<","<<C<<","<<Q0<<","<<Q1<<","<<D<<","<<k<<","<<r<<","<<m<<"\n";hits++;}}}
 cerr<<"cand="<<cand<<" hits="<<hits<<"\n";
}
