class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        self.items.append[data]

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
