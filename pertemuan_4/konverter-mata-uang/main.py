# main.py
from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

# Menampilkan tabel kurs
data = []
for kode, nilai in kurs.items():
    data.append([kode, f"{nilai:,}".replace(",", ".")])

print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

# Input user
dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

# Proses konversi
hasil = konversi(dari, ke, jumlah)

print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {ke}")