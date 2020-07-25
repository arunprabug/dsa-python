class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def addRear(self, data):
        node = Node(data)

        if(self.isEmpty()):
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.size += 1

    def addFront(self, data):
        node = Node(data)

        if self.isEmpty():
            self.rear = node
        else:
            node.next = self.front

        self.front = node
        self.size += 1

    def removeFront(self):
        if(self.isEmpty()):
            return

        data = self.front.data
        self.front = self.front.next
        if(self.front == None):
            self.rear = None

        self.size -= 1
        return data

    def removeRear(self):
        if(self.isEmpty()):
            return

        data = self.rear.data
        if(self.front == self.rear):
            self.rear = None
            self.front = None
        else:
            current = self.front
            while(current.next is not self.rear):
                current = current.next
            current.next = None
            self.rear = current

        self.size -= 1
        return data

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


deque = Deque()
deque.addFront(1)
deque.addRear(2)
print(deque.removeFront())
print(deque.removeRear())
