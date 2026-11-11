#include <bits/stdc++.h>
using namespace std;
long long R=88011536665779LL,M=223336848698040LL;
long long modmul(long long a,long long b,long long m){return (__int128)a*b%m;}
int main(){
 long long mods[]={731,1265,557,406,712,1218};
 long long res[]={171,254,1,349,179,1161};
 for(int i=0;i<6;i++) if(R%mods[i]!=res[i]) return 1;
 if(modmul(171,406,731)!=712||modmul(171,712,731)!=406)return 2;
 if(modmul(254,712,1265)!=1218||modmul(254,1218,1265)!=712)return 3;
 if(modmul(349,325,406)!=151||modmul(349,151,406)!=325)return 4;
 if(modmul(179,19,712)!=553||modmul(179,553,712)!=19)return 5;
 if(modmul(387,47,406)!=325)return 6;
 for(int t=0;t<=1000;t++){
   __int128 B=(__int128)R+(__int128)t*M;
   for(int i=0;i<6;i++)if((long long)(B%mods[i])!=res[i])return 7;
 }
 cout<<"PASS\nCRT progression t=0..1000 verified\n";
}
