#include <bits/stdc++.h>
using namespace std; using i128=__int128_t; using u128=__uint128_t;
bool is_square_i128(i128 x, unsigned long long &r){if(x<0)return false; long double xd=(long double)x; unsigned long long y=(unsigned long long)sqrtl(xd); while((i128)y*y<x)y++; while((i128)y*y>x)y--; if((i128)y*y==x){r=y;return true;}return false;}
string s128(i128 x){if(x==0)return"0";bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
long long gcdll(long long a,long long b){return b?gcdll(b,a%b):abs(a);} 
int main(int argc,char**argv){int H=argc>1?atoi(argv[1]):5000; long long tests=0,hits=0,chamber=0; cout<<"n,a,b,sign,A_num,A_den,w_num,w_den\n";
for(int nv=1;nv<=19;nv++){
 for(int b=1;b<=H;b++) for(int aa=1;5LL*aa<2LL*b;aa++) if(gcd(aa,b)==1){ // 0<m<0.4
  tests++; i128 A=aa,B=b,N=nv;
  i128 val=-48*A*A*A*A +(8*N+1952)*A*A*A*B +(N*N+200*N+10960)*A*A*B*B -(8*N*N+1328*N+72000)*A*B*B*B +(16*N*N+1600*N+102400)*B*B*B*B;
  unsigned long long y; if(!is_square_i128(val,y))continue; hits++;
  // coefficients scaled: a2 denominator b^3; a1 b^2; solve Avar=(-a1 +/- sqrtD)/(2a2)
  // Let a2n=4a^3-24a^2b+(2n+20)ab^2-4nb^3, a1n=-12a^2-(n+100)ab+320b^2.
  i128 a2n=4*A*A*A-24*A*A*B+(2*N+20)*A*B*B-4*N*B*B*B;
  i128 a1n=-12*A*A-(N+100)*A*B+320*B*B;
  // a2=a2n/b^3, a1=a1n/b^2, sqrtD=y/b^2 => X=(-a1n +/- y)*b/(2a2n)
  for(int sg: {-1,1}){
   i128 xn=(-a1n+sg*(i128)y)*B, xd=2*a2n; if(xd==0||xn==0)continue; if(xd<0){xd=-xd;xn=-xn;} if(xn<=0)continue;
   // w=mX-1=(a*xn-b*xd)/(b*xd)
   i128 wn=A*xn-B*xd, wd=B*xd; if(wn<=0||wn>=wd)continue; if(xn<=5*xd)continue;
   chamber++;
   long long g1=std::gcd((long long)llabs((long long)xn),(long long)llabs((long long)xd)); // outputs may fit 64 for H
   long long g2=std::gcd((long long)llabs((long long)wn),(long long)llabs((long long)wd));
   cout<<nv<<","<<aa<<","<<b<<","<<sg<<","<<s128(xn/g1)<<","<<s128(xd/g1)<<","<<s128(wn/g2)<<","<<s128(wd/g2)<<"\n";
  }
 }
}
cerr<<"H="<<H<<" tests="<<tests<<" quartic_square="<<hits<<" chamber_points="<<chamber<<"\n";
}
