class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def tampilkan_maju(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def tampilkan_mundur(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data)
            temp = temp.prev

# SOAL 2
    def hapus_kendaraan(self, plat):
        temp = self.head

        while temp:
            if temp.data == plat:
                # jika head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                # jika tengah / tail
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next