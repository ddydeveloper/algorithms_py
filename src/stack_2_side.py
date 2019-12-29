class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    def __init__(self, size):
        super().__init__(size)
        self.left = -1
        self.right = self.size

    def pop_left(self):
        if self.left == -1:
            return None
        left_pop = self.data[self.left]
        self.left -= 1
        return left_pop

    def pop_right(self):
        if self.right == self.size:
            return None
        right_pop = self.data[self.right]
        self.right += 1
        return right_pop

    def push_left(self, value):
        if self.right - self.left == 1:
            raise OverflowError()
        self.left += 1
        self.data[self.left] = value

    def push_right(self, value):
        if self.right - self.left == 1:
            raise OverflowError()
        self.right -= 1
        self.data[self.right] = value

    def clear(self):
        self.left = -1
        self.right = self.size

