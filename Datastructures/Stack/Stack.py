class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data)

        if not self.isEmpty():
            node.next = self.top

        self.top = node
        self.size += 1

    def pop(self):

        if self.isEmpty():
            return

        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.isEmpty():
            return
        return self.top.data


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
