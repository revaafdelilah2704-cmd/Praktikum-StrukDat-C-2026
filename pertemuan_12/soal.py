class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.right = Node("F")

    def preorder(self, node):
        if node:
            print(node.data, end=" _ ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" _ ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" _ ")

    def get_leaf_nodes(self, node, leaf=[]):
        if node:
            if node.left is None and node.right is None:
                leaf.append(node.data)
            self.get_leaf_nodes(node.left, leaf)
            self.get_leaf_nodes(node.right, leaf)
        return leaf


# Main Program
tree = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")

print("[INFO] Membangun Struktur Gudang...")
tree.insert_manual()
print("[INFO] Struktur berhasil dibuat.\n")

print("HASIL AUDIT:")

print("1. Pre-Order  : ", end="")
tree.preorder(tree.root)


print("\n2. In-Order   : ", end="")
tree.inorder(tree.root)


print("\n3. Post-Order : ", end="")
tree.postorder(tree.root)


leaf_nodes = tree.get_leaf_nodes(tree.root, [])
print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf_nodes))

print("======================================")
print("Audit Selesai!")