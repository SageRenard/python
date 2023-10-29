class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:

    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        else:
            val = self.start.data
            self.start = self.start.next
            if self.start is None:
                self.end = None
            return val

    def push(self, val):

        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node

    def insert(self, n, val):
        if n <= 0:
            self.push(val)
            return

        new_node = Node(val)
        current = self.start
        count = 1
        while current is not None and count < n:
            current = current.next
            count += 1

        if current is None:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node
        else:
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

    def print(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)


queue.print()

queue.insert(3, 5)

queue.insert(4, 4)

queue.print()

print(queue.pop())
print(queue.pop())

queue.print()
