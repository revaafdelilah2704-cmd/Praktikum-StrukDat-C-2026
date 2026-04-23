class StackList:
    def __init__(self):
        self.items = [] 
        
    def is_empty(self):
        return len(self.items) == 0
  
    def push(self, url):
        self.items.append(url)  

    def pop(self):
        if self.is_empty():
            return "riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return none
        return self. items[-1]

    def size(self):
        return len(self.items)

print ("=== Stack list ===")
Stack1 = StackList()
Stack1.push("google.com")
Stack1.push("instagram.com")
print(Stack1.peek())
print(Stack1.pop())
print(Stack1.size())











