class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, n):
        if self.head is None:
            return

        current = self.head

        for i in range(1, n + 1):
            print(f"Giliran {i}: {current.data}")
            current = current.next