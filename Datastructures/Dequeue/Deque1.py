class Deque:
    def __init__(self):
        self.items = []

    def addRear(self, data):
        self.items.append[data]

    def addFront(self, data):
        self.items.insert(0, data)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


deque = Deque()
deque.addFront(1)
deque.addRear(2)
print(deque.removeFront())
print(deque.removeRear())
