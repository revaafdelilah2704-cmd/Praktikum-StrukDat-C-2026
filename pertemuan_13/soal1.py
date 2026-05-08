class Graph:
    def __init__(self):
        self.graph = {}

    # menambahkan kota
    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    # menambahkan jalan        
    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f'[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)')

    # menampilkan graph
    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            tetangga = []

            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")

            print(f"- {kota} terhubung ke: {', '.join(tetangga)}")

     # algoritma dijkstra
    def dijkstra(self, kota_asal):
        jarak = {}
        sudah_dikunjungi = []
        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        while len(sudah_dikunjungi) < len(self.graph):
            kota_sekarang = None
            jarak_minimum = float('inf')

            for kota in self.graph:
                if kota not in sudah_dikunjungi and jarak[kota] < jarak_minimum:
                    jarak_minimum = jarak[kota]
                    kota_sekarang = kota
            if kota_sekarang is None:
                break

            sudah_dikunjungi.append(kota_sekarang)
            for tetangga, bobot in self.graph[kota_sekarang]:
                if tetangga not in sudah_dikunjungi:

                    jarak_baru = jarak[kota_sekarang] + bobot

                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru

        return jarak


# ==========================
# PROGRAM UTAMA
# ==========================

print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=========================================")

g = Graph()

# input jalan
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)
g.tampilkan_graph()

print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...")

hasil = g.dijkstra("Jakarta")

print("\n[HASIL] Jarak Terpendek dari Jakarta:")

nomor = 1
for kota, jarak in hasil.items():
    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {jarak} km")
        nomor += 1

print("=========================================")
print("Simulasi Navigasi Selesai!")