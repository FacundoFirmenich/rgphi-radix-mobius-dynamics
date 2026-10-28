#include <algorithm>
#include <array>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <optional>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
#include <openssl/evp.h>

namespace fs = std::filesystem;

static constexpr std::uint64_t Q_TARGET = 1'100'000ULL;
static constexpr std::size_t BUCKETS = 128;

struct Args {
    std::string mode;
    fs::path src;
    fs::path run_root;
    fs::path run_dir;
    fs::path out;
    fs::path safe_bin;
    int src_bucket = -1;
    int dst_bucket = -1;
    int source_time = -1;
    int fanin = 64;
    std::size_t buffer_keys = 65536;
    bool delete_inputs = false;
};

static std::uint64_t splitmix64(std::uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

static std::uint64_t pack(std::uint32_t a, std::uint32_t b) {
    return (static_cast<std::uint64_t>(a) << 32) | static_cast<std::uint64_t>(b);
}
static std::pair<std::uint32_t,std::uint32_t> unpack(std::uint64_t k) {
    return {static_cast<std::uint32_t>(k >> 32), static_cast<std::uint32_t>(k)};
}

static void write_le64(std::ostream &os, std::uint64_t x) {
    std::array<unsigned char,8> b{};
    for (int i=0;i<8;i++) b[i] = static_cast<unsigned char>((x >> (8*i)) & 0xffU);
    os.write(reinterpret_cast<const char*>(b.data()), 8);
}
static bool read_le64(std::istream &is, std::uint64_t &x) {
    std::array<unsigned char,8> b{};
    is.read(reinterpret_cast<char*>(b.data()), 8);
    if (is.gcount()==0) return false;
    if (is.gcount()!=8) throw std::runtime_error("truncated uint64 record");
    x=0;
    for (int i=0;i<8;i++) x |= static_cast<std::uint64_t>(b[i]) << (8*i);
    return true;
}

static std::string sha256_file(const fs::path &p) {
    std::ifstream in(p, std::ios::binary);
    if (!in) throw std::runtime_error("cannot open for SHA-256: " + p.string());
    EVP_MD_CTX *ctx=EVP_MD_CTX_new();
    if (!ctx) throw std::runtime_error("EVP_MD_CTX_new failed");
    if (EVP_DigestInit_ex(ctx,EVP_sha256(),nullptr)!=1) {EVP_MD_CTX_free(ctx);throw std::runtime_error("EVP_DigestInit_ex failed");}
    std::array<char,1<<20> buf{};
    while (in) {
        in.read(buf.data(), static_cast<std::streamsize>(buf.size()));
        auto n=in.gcount();
        if (n>0 && EVP_DigestUpdate(ctx,buf.data(),static_cast<std::size_t>(n))!=1) {EVP_MD_CTX_free(ctx);throw std::runtime_error("EVP_DigestUpdate failed");}
    }
    std::array<unsigned char,EVP_MAX_MD_SIZE> digest{}; unsigned int len=0;
    if (EVP_DigestFinal_ex(ctx,digest.data(),&len)!=1) {EVP_MD_CTX_free(ctx);throw std::runtime_error("EVP_DigestFinal_ex failed");}
    EVP_MD_CTX_free(ctx);
    std::ostringstream out; out<<std::hex<<std::setfill('0');
    for (unsigned int i=0;i<len;i++) out<<std::setw(2)<<static_cast<int>(digest[i]);
    return out.str();
}

static std::optional<std::pair<std::uint32_t,std::uint32_t>> T(std::uint32_t a, std::uint32_t b) {
    const std::uint64_t r=(10ULL*a)%b;
    if (r==0) return std::pair<std::uint32_t,std::uint32_t>{0,1};
    const std::uint64_t g=std::gcd(r,static_cast<std::uint64_t>(b));
    return std::pair<std::uint32_t,std::uint32_t>{static_cast<std::uint32_t>(r/g),static_cast<std::uint32_t>(b/g)};
}
static std::optional<std::pair<std::uint32_t,std::uint32_t>> S(std::uint32_t a, std::uint32_t b) {
    if (a==0 || 2ULL*a < b) return std::nullopt;
    const std::uint64_t r=(10ULL*(static_cast<std::uint64_t>(b)-a))%a;
    const std::uint64_t d=static_cast<std::uint64_t>(a)+r;
    const std::uint64_t g=std::gcd(static_cast<std::uint64_t>(a),d);
    return std::pair<std::uint32_t,std::uint32_t>{static_cast<std::uint32_t>(a/g),static_cast<std::uint32_t>(d/g)};
}
static bool is_hit(std::uint32_t a, std::uint32_t b) {
    return a<b && static_cast<unsigned __int128>(b) >
        static_cast<unsigned __int128>(Q_TARGET)*(static_cast<std::uint64_t>(b)-a);
}
static bool viable(std::uint32_t b, int remaining) {
    if (remaining<0) return false;
    const int s=(remaining+1)/2;
    if (s>=64) return true;
    return (static_cast<unsigned __int128>(b) << s) > Q_TARGET;
}

static const std::unordered_set<std::uint64_t>& terminal_set() {
    static const std::unordered_set<std::uint64_t> v = {
        pack(2,11),pack(9,11),pack(0,1),pack(1,1),pack(1,2),pack(1,3),
        pack(2,3),pack(3,4),pack(4,5),pack(5,6),pack(7,8),pack(7,9),
        pack(7,10),pack(4,11),pack(7,11),pack(7,12),pack(2,13),pack(5,13),
        pack(6,13),pack(7,13),pack(8,13),pack(11,13),pack(11,20)
    };
    return v;
}

static std::unordered_set<std::uint64_t> load_optional_set(const fs::path &p) {
    std::unordered_set<std::uint64_t> out;
    if (p.empty()) return out;
    std::ifstream in(p,std::ios::binary);
    if (!in) throw std::runtime_error("cannot open safe-state binary: "+p.string());
    std::uint64_t k;
    while (read_le64(in,k)) out.insert(k);
    return out;
}

static Args parse_args(int argc,char**argv) {
    if (argc<2) throw std::runtime_error("usage: engine worker|merge [options]");
    Args a; a.mode=argv[1];
    for (int i=2;i<argc;i++) {
        std::string k=argv[i];
        auto value=[&]() -> std::string {
            if (++i>=argc) throw std::runtime_error("missing value for "+k);
            return argv[i];
        };
        if (k=="--src") a.src=value();
        else if (k=="--run-root") a.run_root=value();
        else if (k=="--run-dir") a.run_dir=value();
        else if (k=="--out") a.out=value();
        else if (k=="--safe-bin") a.safe_bin=value();
        else if (k=="--src-bucket") a.src_bucket=std::stoi(value());
        else if (k=="--dst-bucket") a.dst_bucket=std::stoi(value());
        else if (k=="--source-time") a.source_time=std::stoi(value());
        else if (k=="--fanin") a.fanin=std::stoi(value());
        else if (k=="--buffer-keys") a.buffer_keys=static_cast<std::size_t>(std::stoull(value()));
        else if (k=="--delete-inputs") a.delete_inputs=true;
        else throw std::runtime_error("unknown option: "+k);
    }
    return a;
}

struct WorkerMetrics {
    std::uint64_t source_states=0, raw_children=0, inadmissible=0, hits=0;
    std::uint64_t terminal_pruned=0, safe_pruned=0, viability_pruned=0, emitted=0, runs=0;
    std::uint32_t max_den=0, max_q_num=0, max_q_den=1;
};
static void update_max(WorkerMetrics &m,std::uint32_t a,std::uint32_t b) {
    m.max_den=std::max(m.max_den,b);
    const std::uint32_t d=b-a;
    if (static_cast<unsigned __int128>(b)*m.max_q_den >
        static_cast<unsigned __int128>(m.max_q_num)*d) {
        m.max_q_num=b; m.max_q_den=d;
    }
}

static int run_worker(const Args &a) {
    if (a.src.empty() || a.run_root.empty() || a.src_bucket<0 || a.source_time<0)
        throw std::runtime_error("worker requires --src --run-root --src-bucket --source-time");
    if (a.src_bucket>=static_cast<int>(BUCKETS)) throw std::runtime_error("source bucket out of range");
    const int child_time=a.source_time+1;
    const int remaining=211-child_time;
    fs::create_directories(a.run_root/"workers");
    for (std::size_t d=0;d<BUCKETS;d++) {
        std::ostringstream n; n<<'d'<<std::setw(4)<<std::setfill('0')<<d;
        fs::create_directories(a.run_root/n.str());
    }
    const auto safe=load_optional_set(a.safe_bin);
    std::vector<std::vector<std::uint64_t>> buffers(BUCKETS);
    std::array<std::uint64_t,BUCKETS> seq{};
    for (auto &v:buffers) v.reserve(a.buffer_keys);
    WorkerMetrics m;
    std::ostringstream worker_tag; worker_tag<<'s'<<std::setw(4)<<std::setfill('0')<<a.src_bucket;
    const std::string stag=worker_tag.str();

    auto flush=[&](std::size_t d) {
        auto &v=buffers[d];
        if (v.empty()) return;
        std::sort(v.begin(),v.end());
        v.erase(std::unique(v.begin(),v.end()),v.end());
        std::ostringstream dn; dn<<'d'<<std::setw(4)<<std::setfill('0')<<d;
        std::ostringstream rn; rn<<stag<<"_r"<<std::setw(6)<<std::setfill('0')<<seq[d]++<<".bin";
        fs::path final=a.run_root/dn.str()/rn.str();
        fs::path tmp=final; tmp += ".tmp";
        std::ofstream out(tmp,std::ios::binary|std::ios::trunc);
        if (!out) throw std::runtime_error("cannot create run "+tmp.string());
        for (auto k:v) write_le64(out,k);
        out.close();
        fs::rename(tmp,final);
        m.runs++;
        v.clear();
    };
    auto emit=[&](std::uint64_t k) {
        const std::size_t d=splitmix64(k)&(BUCKETS-1);
        auto &v=buffers[d]; v.push_back(k); m.emitted++;
        if (v.size()>=a.buffer_keys) flush(d);
    };

    fs::path hits_path=a.run_root/"workers"/(stag+"_hits.csv");
    std::ofstream hits(hits_path,std::ios::trunc);
    hits << "child_time,parent_a,parent_b,action,child_a,child_b\n";
    std::ifstream in(a.src,std::ios::binary);
    if (!in) throw std::runtime_error("cannot open source bucket "+a.src.string());
    std::uint64_t key;
    while (read_le64(in,key)) {
        m.source_states++;
        auto [pa,pb]=unpack(key);
        auto process=[&](char action,const std::optional<std::pair<std::uint32_t,std::uint32_t>>& y) {
            if (!y) {m.inadmissible++; return;}
            m.raw_children++;
            auto [ca,cb]=*y;
            update_max(m,ca,cb);
            if (is_hit(ca,cb)) {
                m.hits++;
                hits<<child_time<<','<<pa<<','<<pb<<','<<action<<','<<ca<<','<<cb<<'\n';
                return;
            }
            const auto ck=pack(ca,cb);
            if (terminal_set().count(ck)) {m.terminal_pruned++; return;}
            if (!safe.empty() && safe.count(ck)) {m.safe_pruned++; return;}
            if (!viable(cb,remaining)) {m.viability_pruned++; return;}
            emit(ck);
        };
        process('T',T(pa,pb));
        process('S',S(pa,pb));
    }
    for (std::size_t d=0;d<BUCKETS;d++) flush(d);
    hits.close();
    fs::path metrics_path=a.run_root/"workers"/(stag+".json");
    std::ofstream js(metrics_path,std::ios::trunc);
    js<<"{\n"
      <<"  \"source_time\": "<<a.source_time<<",\n"
      <<"  \"child_time\": "<<child_time<<",\n"
      <<"  \"source_bucket\": "<<a.src_bucket<<",\n"
      <<"  \"source_states\": "<<m.source_states<<",\n"
      <<"  \"raw_children\": "<<m.raw_children<<",\n"
      <<"  \"inadmissible\": "<<m.inadmissible<<",\n"
      <<"  \"hits\": "<<m.hits<<",\n"
      <<"  \"terminal_pruned\": "<<m.terminal_pruned<<",\n"
      <<"  \"safe_pruned\": "<<m.safe_pruned<<",\n"
      <<"  \"viability_pruned\": "<<m.viability_pruned<<",\n"
      <<"  \"emitted_before_run_dedup\": "<<m.emitted<<",\n"
      <<"  \"runs\": "<<m.runs<<",\n"
      <<"  \"max_denominator\": "<<m.max_den<<",\n"
      <<"  \"max_q_num\": "<<m.max_q_num<<",\n"
      <<"  \"max_q_den\": "<<m.max_q_den<<"\n"
      <<"}\n";
    return 0;
}

struct RunReader {
    std::ifstream in;
    std::uint64_t value=0;
    bool valid=false;
    explicit RunReader(const fs::path &p):in(p,std::ios::binary) {
        if (!in) throw std::runtime_error("cannot open run: "+p.string());
        valid=read_le64(in,value);
    }
    bool advance() {valid=read_le64(in,value); return valid;}
};
struct HeapItem {std::uint64_t value; std::size_t reader;};
struct HeapGreater {bool operator()(const HeapItem&a,const HeapItem&b)const{return a.value>b.value;}};

static std::uint64_t merge_group(const std::vector<fs::path>& inputs,const fs::path& output) {
    std::vector<RunReader> readers; readers.reserve(inputs.size());
    for (const auto&p:inputs) readers.emplace_back(p);
    std::priority_queue<HeapItem,std::vector<HeapItem>,HeapGreater> heap;
    for (std::size_t i=0;i<readers.size();i++) if (readers[i].valid) heap.push({readers[i].value,i});
    fs::path tmp=output; tmp += ".tmp";
    std::ofstream out(tmp,std::ios::binary|std::ios::trunc);
    if (!out) throw std::runtime_error("cannot create merged run: "+tmp.string());
    bool have=false; std::uint64_t last=0,count=0;
    while (!heap.empty()) {
        auto x=heap.top(); heap.pop();
        if (!have || x.value!=last) {write_le64(out,x.value);last=x.value;have=true;count++;}
        auto &r=readers[x.reader];
        if (r.advance()) heap.push({r.value,x.reader});
    }
    out.close(); fs::rename(tmp,output); return count;
}

static int run_merge(const Args &a) {
    if (a.run_dir.empty() || a.out.empty() || a.dst_bucket<0)
        throw std::runtime_error("merge requires --run-dir --out --dst-bucket");
    if (a.fanin<2) throw std::runtime_error("fanin must be >=2");
    fs::create_directories(a.out.parent_path());
    std::vector<fs::path> current;
    if (fs::exists(a.run_dir)) {
        for (auto &e:fs::directory_iterator(a.run_dir))
            if (e.is_regular_file() && e.path().extension()==".bin") current.push_back(e.path());
    }
    std::sort(current.begin(),current.end());
    std::uint64_t final_count=0;
    int pass=0;
    if (current.empty()) {
        std::ofstream(a.out,std::ios::binary|std::ios::trunc).close();
    } else {
        while (current.size()>1) {
            std::vector<fs::path> next;
            for (std::size_t i=0;i<current.size();i+=static_cast<std::size_t>(a.fanin)) {
                const std::size_t j=std::min(current.size(),i+static_cast<std::size_t>(a.fanin));
                std::vector<fs::path> group(current.begin()+static_cast<std::ptrdiff_t>(i),current.begin()+static_cast<std::ptrdiff_t>(j));
                std::ostringstream n; n<<"merge_p"<<std::setw(2)<<std::setfill('0')<<pass<<"_g"<<std::setw(6)<<std::setfill('0')<<(i/a.fanin)<<".bin";
                fs::path merged=a.run_dir/n.str();
                merge_group(group,merged);
                next.push_back(merged);
                if (a.delete_inputs) for (const auto&p:group) fs::remove(p);
            }
            current.swap(next); pass++;
        }
        fs::path tmp=a.out; tmp += ".tmp";
        fs::copy_file(current[0],tmp,fs::copy_options::overwrite_existing);
        fs::rename(tmp,a.out);
        if (a.delete_inputs && current[0]!=a.out) fs::remove(current[0]);
    }
    const auto bytes=fs::file_size(a.out);
    if (bytes%8) throw std::runtime_error("merged bucket size is not multiple of 8");
    final_count=bytes/8;
    const auto sha=sha256_file(a.out);
    fs::path meta=a.out; meta += ".json";
    std::ofstream js(meta,std::ios::trunc);
    js<<"{\n"
      <<"  \"bucket\": "<<a.dst_bucket<<",\n"
      <<"  \"count\": "<<final_count<<",\n"
      <<"  \"bytes\": "<<bytes<<",\n"
      <<"  \"sha256\": \""<<sha<<"\"\n"
      <<"}\n";
    return 0;
}

int main(int argc,char**argv) {
    try {
        Args a=parse_args(argc,argv);
        if (a.mode=="worker") return run_worker(a);
        if (a.mode=="merge") return run_merge(a);
        throw std::runtime_error("mode must be worker or merge");
    } catch (const std::exception &e) {
        std::cerr<<"ERROR: "<<e.what()<<"\n";
        return 1;
    }
}
