class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]

    # fungsi hash
    def hash_function(self, kode):
        total = 0
        for huruf in kode:
            total += ord(huruf)

        return total % self.size

    # insert data
    def insert(self, kode, judul):
        index = self.hash_function(kode)

        for data in self.table[index]:
            if data[0] == kode:
                data[1] = judul
                print(f"Data {kode} berhasil diupdate")
                return

        self.table[index].append([kode, judul])
        print(f"Data {kode} berhasil ditambahkan")

    # search data
    def search(self, kode):
        index = self.hash_function(kode)

        for data in self.table[index]:
            if data[0] == kode:
                print(f"{kode} : {data[1]}")
                return

        print("Buku tidak ditemukan")

    # delete data
    def delete(self, kode):
        index = self.hash_function(kode)

        for data in self.table[index]:
            if data[0] == kode:
                self.table[index].remove(data)
                print(f"Data {kode} berhasil dihapus")
                return

        print("Data tidak ditemukan")

    # display hash table
    def display(self):
        print("\nIsi Hash Table")
        for i in range(self.size):
            print(f"Bucket {i} :", end=" ")

            if len(self.table[i]) == 0:
                print("Kosong")
            else:
                for data in self.table[i]:
                    print(f"[{data[0]} : {data[1]}]", end=" ")
                print()


# hash table
buku = HashTable()

# insert data awal
buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")
buku.insert("BK555", "Algoritma Pemrograman")

# display awal
buku.display()

# insert data baru
print("\nTambah dan Update Data")
buku.insert("BK045", "Mein Kampf")
buku.insert("BK111", "Bumi Manusia")

# display lagi
buku.display()

# search data
print("\nSearch Buku")
buku.search("BK222")
buku.search("BK999")

# delete data
print("\nDelete Buku")
buku.delete("BK333")

# display terakhir
buku.display()