class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, data):
        node = Node(data)

        if self.isEmpty():
            self.tail = node
        else:
            current = self.head
            current.prev = node
            node.next = current

        self.head = node

        self.size += 1

    def addLast(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = node
        else:
            current = self.tail
            current.next = node
            node.prev = current

        self.tail = node

        self.size += 1

    def addAtPos(self, pos, data):
        if(pos < 0 or pos > self.size):
            return

        node = Node(data)

        if pos == 0:
            self.addFirst(data)
        elif pos == self.size:
            self.addLast(data)
        else:
            current = self.head
            currentpos = 0

            while (currentpos < pos-1):
                current = current.next
                currentpos += 1

            node.next = current.next
            node.prev = current
            node.next.prev = node
            current.next = node

            self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return
        if self.size == 1:
            self.head = None
        else:
            current = self.head
            current = current.next
            current.prev = None
            self.head = current

        self.size -= 1

    def removeLast(self):
        if self.isEmpty():
            return
        if self.size == 1:
            self.tail = None
        else:
            current = self.tail
            current = current.prev
            current.next = None
            self.tail = current

        self.size -= 1

    def removeAtPos(self, pos):
        if pos < 0 or pos > self.size:
            return

        if self.isEmpty():
            return

        if pos == 0:
            self.removeFirst()
        elif pos == self.size - 1:
            self.removeLast()
        else:
            currentpos = 0
            current = self.head
            while(currentpos < pos):
                current = current.next
                currentpos += 1
            current.next.prev = current.prev
            current = current.next

            self.size -= 1

    def search(self, data):
        if self.isEmpty():
            return -1

        pos = 0
        current = self.head

        while current is not None:
            if current.data == data:
                return pos
            pos += 1
            current = current.next

        return -1

    def forwardDisplay(self):
        if self.head is None:
            return

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def reverseDisplay(self):
        if self.tail is None:
            return

        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


list = DoubleLinkedList()
list.addFirst(1)
list.addFirst(2)
list.addLast(3)
list.addLast(4)
list.addLast(5)
list.addLast(6)
list.removeFirst()
list.removeLast()
list.search(4)
list.addAtPos(2, 7)
list.addAtPos(0, 9)
list.addAtPos(6, 10)
list.forwardDisplay()
list.removeAtPos(5)
list.reverseDisplay()
