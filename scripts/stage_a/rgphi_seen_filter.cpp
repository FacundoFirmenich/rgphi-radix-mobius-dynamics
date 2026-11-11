#include <array>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

namespace fs = std::filesystem;

static void write_le64(std::ostream &os, std::uint64_t x) {
    std::array<unsigned char,8> b{};
    for (int i=0;i<8;i++) b[i]=static_cast<unsigned char>((x>>(8*i))&0xffU);
    os.write(reinterpret_cast<const char*>(b.data()),8);
}
static bool read_le64(std::istream &is,std::uint64_t &x) {
    std::array<unsigned char,8> b{};
    is.read(reinterpret_cast<char*>(b.data()),8);
    if (is.gcount()==0) return false;
    if (is.gcount()!=8) throw std::runtime_error("truncated uint64 record");
    x=0; for(int i=0;i<8;i++) x|=static_cast<std::uint64_t>(b[i])<<(8*i);
    return true;
}
struct Reader {
    std::ifstream in;
    std::uint64_t v=0,prev=0;
    bool valid=false,have_prev=false;
    explicit Reader(const fs::path&p):in(p,std::ios::binary) {
        if(!in) throw std::runtime_error("cannot open "+p.string());
        valid=next();
    }
    bool next() {
        std::uint64_t x;
        if(!read_le64(in,x)){valid=false;return false;}
        if(have_prev && x<=prev) throw std::runtime_error("input not strictly sorted unique");
        prev=x;have_prev=true;v=x;valid=true;return true;
    }
};
int main(int argc,char**argv){
    try{
        fs::path cand,seen,out_new,out_seen,metrics;
        for(int i=1;i<argc;i++){
            std::string k=argv[i];
            auto val=[&](){if(++i>=argc)throw std::runtime_error("missing value");return std::string(argv[i]);};
            if(k=="--candidate")cand=val();
            else if(k=="--seen")seen=val();
            else if(k=="--new")out_new=val();
            else if(k=="--seen-out")out_seen=val();
            else if(k=="--metrics")metrics=val();
            else throw std::runtime_error("unknown option "+k);
        }
        if(cand.empty()||seen.empty()||out_new.empty()||out_seen.empty())
            throw std::runtime_error("required: --candidate --seen --new --seen-out");
        Reader c(cand),s(seen);
        fs::create_directories(out_new.parent_path());
        fs::create_directories(out_seen.parent_path());
        auto nt=out_new;nt+=".tmp"; auto st=out_seen;st+=".tmp";
        std::ofstream no(nt,std::ios::binary|std::ios::trunc),so(st,std::ios::binary|std::ios::trunc);
        if(!no||!so) throw std::runtime_error("cannot create outputs");
        std::uint64_t new_count=0,seen_in=0,seen_out=0,overlap=0,cand_count=0;
        while(c.valid||s.valid){
            if(!s.valid || (c.valid && c.v<s.v)){
                write_le64(no,c.v);write_le64(so,c.v);new_count++;seen_out++;cand_count++;c.next();
            } else if(!c.valid || s.v<c.v){
                write_le64(so,s.v);seen_in++;seen_out++;s.next();
            } else {
                write_le64(so,s.v);seen_in++;seen_out++;cand_count++;overlap++;c.next();s.next();
            }
        }
        no.close();so.close();fs::rename(nt,out_new);fs::rename(st,out_seen);
        if(!metrics.empty()){
            std::ofstream m(metrics);
            m<<"{\n"
             <<"  \"candidate_unique\": "<<cand_count<<",\n"
             <<"  \"seen_input\": "<<seen_in<<",\n"
             <<"  \"overlap_seen\": "<<overlap<<",\n"
             <<"  \"new_frontier\": "<<new_count<<",\n"
             <<"  \"seen_output\": "<<seen_out<<"\n"
             <<"}\n";
        }
        return 0;
    }catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<"\n";return 1;}
}
