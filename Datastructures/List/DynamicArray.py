import ctypes


class DynamicArray:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def get(self, i):
        if(i < 0 or i > self.size-1):
            return

        return self.array[i]

    def add(self, data):
        if(self.size == self.capacity):
            self._resize()

        self.array[self.size] = data
        self.size += 1

    def _resize(self):
        tArray = self._make_array(2*self.capacity)
        for i in range(self.size):
            tArray[i] = self.array[i]

        self.array = tArray
        self.capacity = 2*self.capacity

    def display(self):
        for i in range(self.size):
            print(array[i])

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()


arrayList = DynamicArray()
arrayList.add(1)
arrayList.add(2)
print(arrayList.get(1))
