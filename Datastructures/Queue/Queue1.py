class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(1)
print(queue.dequeue())
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
