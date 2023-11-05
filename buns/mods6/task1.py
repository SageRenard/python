class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        i = 0
        while current and i < index:
            current = current.next_node
            i += 1
        if current:
            return current.data
        else:
            return None

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next_node
            return
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next_node
            i += 1
        if current and current.next_node:
            current.next_node = current.next_node.next_node

    def insert(self, n, val):
        if n <= 0:
            new_node = Node(val)
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            i = 0
            while current and i < n - 1:
                current = current.next_node
                i += 1
            if current:
                new_node = Node(val)
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node


linkedList = LinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)

print(linkedList.get(0))
print(linkedList.get(1))
print(linkedList.get(2))

linkedList.remove(2)
print(linkedList.get(2))

linkedList.push(4)
print(linkedList.get(2))

linkedList.insert(2, 30)
print(linkedList.get(2))
print(linkedList.get(3))

for item in linkedList:
    print(item, end=' ')
