class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)

        if(self.isEmpty()):
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.size += 1

    def dequeue(self):
        if(self.isEmpty()):
            return

        data = self.front.data
        self.front = self.front.next
        if(self.front == None):
            self.rear = None

        self.size -= 1
        return data

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


queue = Queue()
queue.enqueue(1)
print(queue.dequeue())
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
