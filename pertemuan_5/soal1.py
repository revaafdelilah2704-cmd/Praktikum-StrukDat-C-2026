stok_barang = [15, 40, 30, 10, 25]

stok_barang[3] = 50
print(stok_barang)

stok_barang.append(5)
stok_barang.sort(reverse=True)
jumlah = sum(stok_barang)

rata = jumlah/len(stok_barang)
print(jumlah)
status = 'Stok Aman' if rata > 20 else 'waspada'
print(status)
