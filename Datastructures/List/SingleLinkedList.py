class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, data):  # O(1)
        node = Node(data)

        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

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
            current = self.head
            currentpos = 0
            while (currentpos < pos-1):
                current = current.next
                currentpos += 1

            node.next = current.next
            current.next = node

            self.size += 1

    def addLast(self, data):  # O(n)
        node = Node(data)

        if self.isEmpty():
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

        self.size += 1

    def removeFirst(self):  # O(1)

        if self.isEmpty():
            return

        current = self.head
        self.head = current.next
        current = None

        self.size -= 1

    def removeLast(self):  # O(n)

        if self.isEmpty():
            return

        current = self.head
        prev = None

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        current = None

        self.size -= 1

    def removeAtPos(self, pos):  # O(n)
        if pos < 0 or pos > self.size:
            return

        if pos == 0:
            self.removeFirst()
        elif pos == self.size - 1:
            self.removeLast()
        else:
            currentpos = 0
            current = self.head

            while(currentpos < pos-1):
                current = current.next
                currentpos += 1

            current.next = current.next.next

            self.size -= 1

    def search(self, data):  # O(n)
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

    def displayList(self):  # O(n)
        if self.isEmpty():
            return

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def isEmpty(self):  # O(1)
        return self.size == 0

    def sizeOf(self):  # O(1)
        return self.size


list = SingleLinkedList()
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
list.displayList()
list.removeAtPos(5)
list.displayList()
