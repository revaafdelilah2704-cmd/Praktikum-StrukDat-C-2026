# Class Node
class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


# Class BST
class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        
        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        current = self.root
        while True:
            if id_buku < current.id:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
        
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    # SEARCH
    def search(self, id_buku):
        current = self.root
        
        while current:
            if id_buku == current.id:
                return current
            elif id_buku < current.id:
                current = current.left
            else:
                current = current.right
        
        return None

    # INORDER TRAVERSAL
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    # GET MIN
    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    # GET MAX
    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    # HEIGHT
    def height(self, node):
        if node is None:
            return -1
        
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        
        return max(left_h, right_h) + 1


# ===========================
# MAIN PROGRAM
# ===========================

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst = BST()

# Input data
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# Inorder traversal
print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root)

# Search
print("\n[SEARCH] Mencari ID 60...")
result = bst.search(60)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")

print("\n[SEARCH] Mencari ID 100...")
result = bst.search(100)
if result:
    print(f"Ditemukan! Judul: {result.judul}")
else:
    print("Data tidak ditemukan.")

# Statistik
min_buku = bst.get_min()
max_buku = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

# Height
print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")

print("=========================================")
print("Simulasi Selesai!")