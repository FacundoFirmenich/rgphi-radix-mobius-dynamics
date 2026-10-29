#include <bits/stdc++.h>
using namespace std;
struct State{uint32_t a,b;};
static inline uint64_t pack(uint32_t a,uint32_t b){return (uint64_t(a)<<32)|b;}
static inline pair<uint32_t,uint32_t> red(uint64_t a,uint64_t b){uint64_t g=std::gcd(a,b);return {(uint32_t)(a/g),(uint32_t)(b/g)};}
static const set<uint64_t> terminals=[](){set<uint64_t>s;pair<uint32_t,uint32_t>x[]={{2,11},{9,11},{0,1},{1,1},{1,2},{1,3},{2,3},{3,4},{4,5},{5,6},{7,8},{7,9},{7,10},{4,11},{7,11},{7,12},{2,13},{5,13},{6,13},{7,13},{8,13},{11,13},{11,20}};for(auto [a,b]:x)s.insert(pack(a,b));return s;}();
static inline vector<pair<uint32_t,uint32_t>> children(uint32_t a,uint32_t b){
 vector<pair<uint32_t,uint32_t>> v; v.reserve(2);
 uint64_t z=10ULL*a;uint32_t d=z/b;auto t=red(z-(uint64_t)d*b,b);v.push_back(t);
 if(a && 2ULL*a>=b){z=10ULL*(b-a);d=z/a;uint64_t br=10ULL*b-(uint64_t)(9+d)*a;v.push_back(red(a,br));}
 return v;
}
struct Row{int depth;string parent,target,wact,aact,alt;};
int main(int argc,char**argv){
 int D=argc>1?stoi(argv[1]):2500; string chain=argc>2?argv[2]:"/mnt/data/rgphi_global/full_predecessor_chain.csv"; string outdir=argc>3?argv[3]:"/mnt/data/rgphi_global/out2500"; filesystem::create_directories(outdir);
 size_t side=(size_t)D+1, grid=side*side; vector<int32_t> direct(grid,-1); vector<State> st; st.reserve((size_t)(0.31*D*D));
 for(uint32_t b=2;b<=(uint32_t)D;b++)for(uint32_t a=1;a<b;a++)if(std::gcd(a,b)==1 && !terminals.count(pack(a,b))){direct[(size_t)b*side+a]=st.size();st.push_back({a,b});}
 uint32_t N=st.size(); cerr<<"states="<<N<<"\n";
 vector<array<int32_t,2>> adj(N); vector<uint8_t> deg(N,0),hasout(N,0),hasterm(N,0); uint64_t E=0;
 vector<uint32_t> indeg_rev(N,0);
 for(uint32_t i=0;i<N;i++){adj[i]={-3,-3};auto cs=children(st[i].a,st[i].b);for(auto [a,b]:cs){if(terminals.count(pack(a,b))){hasterm[i]=1;continue;}if(a>0&&a<b&&b<=(uint32_t)D){int32_t j=direct[(size_t)b*side+a];if(j>=0){adj[i][deg[i]++]=j;indeg_rev[j]++;E++;continue;}}hasout[i]=1;}}
 cerr<<"edges="<<E<<"\n";
 // reverse CSR
 vector<uint64_t> roff(N+1,0);for(uint32_t i=0;i<N;i++)roff[i+1]=roff[i]+indeg_rev[i];vector<uint32_t> rcur(N);for(uint32_t i=0;i<N;i++)rcur[i]=roff[i];vector<uint32_t> redges(E);for(uint32_t i=0;i<N;i++)for(int k=0;k<deg[i];k++){uint32_t j=adj[i][k];redges[rcur[j]++]=i;}
 // first pass iterative dfs postorder
 vector<uint8_t> color(N,0);vector<uint32_t> order;order.reserve(N);vector<pair<uint32_t,uint8_t>> stack;stack.reserve(1<<20);
 for(uint32_t s=0;s<N;s++)if(!color[s]){stack.push_back({s,0});color[s]=1;while(!stack.empty()){auto &fr=stack.back();uint32_t u=fr.first;if(fr.second<deg[u]){uint32_t v=adj[u][fr.second++];if(!color[v]){color[v]=1;stack.push_back({v,0});}}else{order.push_back(u);color[u]=2;stack.pop_back();}}}
 // second pass
 vector<int32_t> comp(N,-1);vector<uint32_t> csize;vector<uint32_t> stk;stk.reserve(1<<20);int32_t C=0;
 for(auto it=order.rbegin();it!=order.rend();++it){uint32_t s=*it;if(comp[s]>=0)continue;uint32_t sz=0;comp[s]=C;stk.push_back(s);while(!stk.empty()){uint32_t u=stk.back();stk.pop_back();sz++;for(uint64_t p=roff[u];p<roff[u+1];p++){uint32_t v=redges[p];if(comp[v]<0){comp[v]=C;stk.push_back(v);}}}csize.push_back(sz);C++;}
 cerr<<"scc="<<C<<"\n";
 // component data and unique edges
 vector<uint8_t> coutside(C,0),cterm(C,0);vector<uint64_t> cpairs;cpairs.reserve(E);
 for(uint32_t i=0;i<N;i++){int32_t ci=comp[i];if(hasout[i])coutside[ci]=1;if(hasterm[i])cterm[ci]=1;for(int k=0;k<deg[i];k++){int32_t cj=comp[adj[i][k]];if(ci!=cj)cpairs.push_back((uint64_t(uint32_t(ci))<<32)|uint32_t(cj));}}
 sort(cpairs.begin(),cpairs.end());cpairs.erase(unique(cpairs.begin(),cpairs.end()),cpairs.end());
 vector<uint32_t> coff(C+1,0),cindeg(C,0);for(auto x:cpairs){uint32_t u=x>>32,v=(uint32_t)x;coff[u+1]++;cindeg[v]++;}for(int i=0;i<C;i++)coff[i+1]+=coff[i];vector<uint32_t> ccur=coff,cedge(cpairs.size());for(auto x:cpairs){uint32_t u=x>>32,v=(uint32_t)x;cedge[ccur[u]++]=v;}
 deque<uint32_t> dq;for(int i=0;i<C;i++)if(!cindeg[i])dq.push_back(i);vector<uint32_t> topo;topo.reserve(C);while(!dq.empty()){auto u=dq.front();dq.pop_front();topo.push_back(u);for(uint32_t p=coff[u];p<coff[u+1];p++){auto v=cedge[p];if(--cindeg[v]==0)dq.push_back(v);}}
 if(topo.size()!=size_t(C)){cerr<<"condensation cycle error\n";return 3;}
 vector<uint8_t> safe(C,0),closed(C,0);for(int c=0;c<C;c++)closed[c]=(!coutside[c] && coff[c]==coff[c+1]);for(auto it=topo.rbegin();it!=topo.rend();++it){uint32_t u=*it;bool ok=!coutside[u];for(uint32_t p=coff[u];p<coff[u+1]&&ok;p++)ok=safe[cedge[p]];safe[u]=ok;}
 uint64_t safestates=0;int safec=0,closedc=0;for(int c=0;c<C;c++){if(safe[c]){safec++;safestates+=csize[c];}if(closed[c])closedc++;}
 cerr<<"safe_scc="<<safec<<" safe_states="<<safestates<<" closed="<<closedc<<"\n";
 // component state aggregates
 vector<uint32_t> cmaxden(C,0),cq_a(C,0),cq_b(C,1);vector<vector<uint32_t>> members(C);for(int c=0;c<C;c++)members[c].reserve(csize[c]);
 for(uint32_t i=0;i<N;i++){int c=comp[i];members[c].push_back(i);cmaxden[c]=max(cmaxden[c],st[i].b);uint64_t den=st[i].b-st[i].a;if((__uint128_t)st[i].b*cq_b[c]>(__uint128_t)cq_a[c]*den){cq_a[c]=st[i].b;cq_b[c]=den;}}
 // emit all exact safe states for downstream basin reuse
 {ofstream sf(outdir+"/D2500_safe_states.csv");sf<<"a,b,scc,closed_scc\n";for(uint32_t i=0;i<N;i++){int c=comp[i];if(safe[c])sf<<st[i].a<<","<<st[i].b<<","<<c<<","<<(int)closed[c]<<"\n";}}
 // parse chain
 ifstream fin(chain);string line;getline(fin,line);vector<Row> rows;while(getline(fin,line)){if(line.empty())continue;vector<string>v;string x;stringstream ss(line);while(getline(ss,x,','))v.push_back(x);Row r{stoi(v[0]),v[2],v[1],v[3],v[5],v[7]};rows.push_back(r);}
 ofstream fo(outdir+"/first_divergence_D2500_classification.csv");fo<<"depth,parent,target,witness_action,alternate_action,alternate_state,class,closure_size,scc_count,closed_scc_count,max_q_num,max_q_den,max_den\n";
 map<string,int> counts;vector<int> finite_depths,terminal_depths,inad;
 for(auto&r:rows){string cls;uint64_t closuresz=0;int nscc=0,nclosed=0;uint32_t mqa=0,mqb=1,mden=0;
   if(r.alt=="inadmissible"||r.alt.empty()){cls="INADMISSIBLE";inad.push_back(r.depth);}else{auto pos=r.alt.find('/');uint32_t a=stoul(r.alt.substr(0,pos)),b=stoul(r.alt.substr(pos+1));if(terminals.count(pack(a,b))){cls="TERMINAL";terminal_depths.push_back(r.depth);}else if(b>(uint32_t)D||a>=b||direct[(size_t)b*side+a]<0){cls="OUTSIDE_D2500";}else{int32_t ci=comp[direct[(size_t)b*side+a]];if(!safe[ci])cls="UNRESOLVED_ESCAPES_D2500";else{cls="FINITE_TRAP_BASIN";finite_depths.push_back(r.depth);vector<uint8_t> seen(C,0);vector<uint32_t>s2{(uint32_t)ci};seen[ci]=1;while(!s2.empty()){uint32_t u=s2.back();s2.pop_back();nscc++;closuresz+=csize[u];mden=max(mden,cmaxden[u]);if((__uint128_t)cq_a[u]*mqb>(__uint128_t)mqa*cq_b[u]){mqa=cq_a[u];mqb=cq_b[u];}if(closed[u])nclosed++;for(uint32_t p=coff[u];p<coff[u+1];p++){auto v=cedge[p];if(!seen[v]){seen[v]=1;s2.push_back(v);}}}}}}
   counts[cls]++;fo<<r.depth<<","<<r.parent<<","<<r.target<<","<<r.wact<<","<<r.aact<<","<<r.alt<<","<<cls<<","<<closuresz<<","<<nscc<<","<<nclosed<<","<<mqa<<","<<mqb<<","<<mden<<"\n";
 }
 ofstream js(outdir+"/D2500_classification_summary.json");js<<"{\n  \"status\":\"PASS\",\n  \"D\":"<<D<<",\n  \"states\":"<<N<<",\n  \"edges\":"<<E<<",\n  \"SCCs\":"<<C<<",\n  \"closed_mod_terminal_SCCs\":"<<closedc<<",\n  \"safe_SCCs\":"<<safec<<",\n  \"safe_states\":"<<safestates<<",\n  \"class_counts\":{\n";int ii=0;for(auto&[k,v]:counts){js<<"    \""<<k<<"\":"<<v<<(++ii==(int)counts.size()?"\n":",\n");}js<<"  },\n  \"finite_depths\":[";for(size_t i=0;i<finite_depths.size();i++)js<<(i?",":"")<<finite_depths[i];js<<"],\n  \"terminal_depths\":[";for(size_t i=0;i<terminal_depths.size();i++)js<<(i?",":"")<<terminal_depths[i];js<<"],\n  \"inadmissible_depths\":[";for(size_t i=0;i<inad.size();i++)js<<(i?",":"")<<inad[i];js<<"]\n}\n";
 cout<<"PASS D="<<D<<" states="<<N<<" edges="<<E<<" SCCs="<<C<<" safe_states="<<safestates<<"\n";
}
