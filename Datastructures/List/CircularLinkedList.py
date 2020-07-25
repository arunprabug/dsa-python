class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0

    def search(self, data):  # o(n)
        if self.isEmpty():
            return -1

        if(self.tail.data == data):
            return self.size() - 1

        first = self.last.next

        while first is not last:
            if first.data == data:
                return pos

            pos += 1
            first = first.next

        return -1

    def addFirst(self, data):  # O(1)
        node = Node(data)
        if self.isEmpty():
            self.last = node

        first = self.last.next
        node.next = first
        self.last.next = node

        self.size += 1

    def addLast(self, data):  # O(1)
        node = Node(data)
        if self.isEmpty():
            self.last = node

        last = self.last
        node.next = last.next
        last.next = node
        self.last = node

        self.size += 1

    def addAtPos(self, pos, data):  # O(n)
        if(pos < 0 or pos > self.size):
            return

        node = Node(data)

        if pos == 0:
            self.addFirst(data)
        elif pos == self.size:
            self.addLast(data)
        else:
            first = self.last.next
            currentpos = 0

            while (currentpos < pos-1):
                first = first.next
                currentpos += 1

            node.next = first.next
            first.next = node

            self.size += 1

    def removeAtPos(self, pos):  # O(n)
        if(pos < 0 or pos > self.size):
            return

        if pos == 0:
            self.removeFirst()
        elif pos == self.size:
            self.removeLast()
        else:
            first = self.last.next
            currentpos = 0

            while (currentpos < pos-1):
                first = first.next
                currentpos += 1

            first.next = first.next.next

            self.size -= 1

    def removeFirst(self):  # O(1)
        if self.isEmpty():
            return

        first = self.last.next
        self.last.next = first.next

        self.size -= 1

    def removeLast(self):  # O(n)
        if self.isEmpty():
            return

        first = self.last.next

        while first.next is not self.last:
            first = first.next

        first.next = self.last.next
        self.last = first.next

        self.size -= 1

    def displayList(self):
        if self.isEmpty():
            return

        first = self.last.next
        while first is not self.last:
            print(first.data)
            first = first.next
        print(first.data)

    def isEmpty(self):
        return self.size == 0

    def sizeOf(self):
        return self.size


list = CircularLinkedList()
list.addFirst(1)
list.addLast(2)
list.addAtPos(1, 3)
list.removeAtPos(1)
list.displayList()
