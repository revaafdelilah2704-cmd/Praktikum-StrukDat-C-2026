class bunga:

    def __init__(self, nama, warna, harga):
       self.nama = nama
       self.warna = warna
       self.harga = harga
   
    def info(self):
      print(self.nama, self.warna, self.harga)


b1 = bunga("mawar", "merah", 15000)
b2 = bunga("matahari", "oren", 10000)
b3 = bunga("anggrek", "unggu", 20000)
    
b1.info()
b2.info()
b3.info()


