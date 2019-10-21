class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    def __init__(self, size):
        self.array = Array(size)
        self.top = -1
        self.size = size

    def pop(self):
        if self.top == -1:
            return None
        value_to_pop = self.array.data[self.top]
        self.top -= 1
        return value_to_pop

    def peek(self):
        if self.top == -1:
            return None
        return self.array.data[self.top]

    def push(self, value):
        if self.top == self.size - 1:
            raise OverflowError()
        self.top += 1
        self.array.data[self.top] = value

    def count(self):
        return self.top + 1

    def clear(self):
        self.top = -1
