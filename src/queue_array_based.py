class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Queue(Array):
    def __init__(self, size):
        super().__init__(size)
        self.first = None
        self.last = None

    def enqueue(self, value):
        if self.length == self.size:
            raise OverflowError()

        if self.first is None:
            self.first = 0
            self.last = 0
            self.data[0] = value
            self.length += 1
            return

        if self.last == self.size - 1:
            self.last = 0
            self.data[0] = value
        else:
            self.last += 1
            self.data[self.last] = value

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        if self.length == 1:
            value = self.data[self.first]
            self.length = 0
            self.first = None
            self.last = None
            return value

        value = self.data[self.first]

        if self.first == self.size - 1:
            self.first = 0
        else:
            self.first += 1

        self.length -= 1
        return value
