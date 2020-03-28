from src.data_structures.custom_array import CustomArray
from src.data_structures.custom_node import CustomNode


class StackArrayBased(CustomArray):
    def __init__(self, size):
        self.array = CustomArray(size)
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


class StackNodeBased:
    def __init__(self):
        self.top = CustomNode(None)
        self._count = 0

    def pop(self):
        if self.top.next_node is None:
            return None
        node_to_pop = self.top.next_node
        self.top.next_node = node_to_pop.next_node
        self._count -= 1
        return node_to_pop.value

    def peek(self):
        if self.top.next_node is None:
            return None
        return self.top.next_node.value

    def count(self):
        return self._count

    def clear(self):
        self._count = 0
        self.top.next_node = None

    def push(self, value):
        new_node = CustomNode(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        self._count += 1


class Stack2Side(CustomArray):
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