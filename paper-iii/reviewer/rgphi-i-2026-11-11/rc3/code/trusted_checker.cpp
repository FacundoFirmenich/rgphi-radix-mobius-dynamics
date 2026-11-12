#include <bits/stdc++.h>
using namespace std; using i128=__int128_t;
struct R{long long p,q;};
const long long B0=88011536665779LL, M=223336848698040LL;
R X[5]={{406,731},{712,731},{712,1265},{1218,1265},{406,557}};
int TM[5]={1,0,3,2,4}, SM[5]={4,2,1,0,0};
long long mod(i128 a,long long m){long long r=(long long)(a%m);return r<0?r+m:r;}
bool tedge(long long B,int i,int j){long long g=gcd(X[i].q,B);return X[i].q/g==X[j].q && mod((i128)(B/g)*X[i].p,X[j].q)==X[j].p;}
bool sedge(long long B,int i,int j){long long h=gcd(X[i].p,B);long long ci=X[i].q-X[i].p,cj=X[j].q-X[j].p;return X[i].p/h==X[j].p && mod((i128)(B/h)*ci,X[j].p)==cj;}
int main(){for(int t=0;t<=1000;t++){long long B=B0+M*t;for(int i=0;i<5;i++){if(gcd(X[i].p,X[i].q)!=1||2*X[i].p<=X[i].q||X[i].p>=X[i].q)return 1;if(!tedge(B,i,TM[i])||!sedge(B,i,SM[i]))return 2;}}
cout<<"PASS C++ counterfamily_1001\n";}
