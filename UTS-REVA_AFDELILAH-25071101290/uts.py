SOAL 1

Pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]


def tampilkan_pengunjung():
    print(===== DATA PENGUNJUNG PERPUSTAKAAN =====)


def filter_belum_kembali():
    hasil = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    hasil.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI")


#soal 2
def info_perpustakaan():
    info = ("perpustakaan kampus terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321")

    print("Info perpustakaaan:")
    print("Nama :", info[0])
    print("Alamat :", info[1])
    print("Telp :", info[2])

def rekap_kategori(data):
    u = set(data)
    print("\nUnik:", u)

    f = {}
    for d in data:
        f[d] = f.get(d, 0) + 1

        print("Rekap:")
    for info,v in f.items():
        print(info, ":", v)
    
    m = max(f.values())
    t = [info for info,v in f.items() if v == m]
    print("Terbanyak:", ", ".join(t), f"({m})")

data = {"Fiksi", "Sains", "Hukum"}

print = info_perpustakaan()
print = rekap_kategori(data)  


soal 3
class pengunjung:
    total = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        pengunjung.total += 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_nama(self):
        return self.__kategori

        
    def tampilkan_info(self):
        print("id :", self.__id)
        print("Nama :", self.__nama)
        print("kategori :", self.__kategori)

    def hitung_pengunjung(self):
        return pengunjung.total

class PengunjungPrioritas(pengunjung):
    def __init__(self, id, nama,kategori , prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

        
    def tampilkan_info(self):
        print("id :", self.get_id())
        print("nama :", self.get_nama())
        print("kategori :", self.get_kategori())
        print("prioritas :", self.prioritas)

        if self.prioritas == "mendesak":
            print("** layani segera! **")

            
p1 = pengunjung("M001", "Rina", "fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "referensi", "mendesak")

p1.tampilkan_info()
print()
p2.tampilkan_info()
print("\nTotal pengunjung:", p1.hitung_pengunjung())


SOAL 4

antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())
Contoh Output:
===== ANTRIAN PEMINJAMAN =====
[1] M001 - Rina | Fiksi
[2] M002 - Hendra | Sains
[3] M003 - Siti | Fiksi
[4] M004 - Taufik | Hukum
Total antrian: 4
Memanggil pengunjung berikutnya...
Silakan masuk: Rina (M001) - Fiksi
===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M003 - Siti | Fiksi
[3] M004 - Taufik | Hukum
Total antrian: 3
Menghapus pengunjung dengan ID M003...
Siti (M003) berhasil dihapus dari antrian.
===== ANTRIAN PEMINJAMAN =====
[1] M002 - Hendra | Sains
[2] M004 - Taufik | Hukum
Total antrian: 2
Mencari 'Taufik'...
Ditemukan: M004 - Taufik | Hukum (posisi ke-2)
Total antrian: 2










            

































