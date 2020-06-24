import unittest
from src.data_structures.c_stack import StackNodeBased, Stack2Side, StackArrayBased


class TestStack(unittest.TestCase):
    # node_based
    def test_node_based_pop(self):
        stack = StackNodeBased()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.pop() == 3)
        self.assertTrue(stack.pop() == 2)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_node_based_push(self):
        stack = StackNodeBased()
        stack.push(1)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_node_based_peek(self):
        stack = StackNodeBased()
        self.assertTrue(stack.peek() is None)
        stack.push(1)
        stack.push(2)
        self.assertTrue(stack.peek() == 2)
        stack.pop()
        self.assertTrue(stack.peek() == 1)
        stack.pop()
        self.assertTrue(stack.peek() is None)

    def test_node_based_count(self):
        stack = StackNodeBased()
        self.assertTrue(stack.count() == 0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)

    def test_node_based_clear(self):
        stack = StackNodeBased()
        self.assertTrue(stack.peek() is None)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.peek() == 3)
        stack.clear()
        self.assertTrue(stack.peek() is None)

    # array  based
    def test_array_based_pop(self):
        stack = StackArrayBased(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.pop() == 3)
        self.assertTrue(stack.pop() == 2)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_array_based_pop_overflow(self):
        stack = StackArrayBased(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.push(4)

    def test_array_based_push(self):
        stack = StackArrayBased(3)
        stack.push(1)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_array_based_count(self):
        stack = StackArrayBased(3)
        stack.push(1)
        self.assertTrue(stack.count() == 1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)

    def test_array_based_clear(self):
        stack = StackArrayBased(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)
        stack.clear()
        self.assertTrue(stack.count() == 0)

    # 2 side
    def test_two_side_push_left(self):
        stack = Stack2Side(3)
        stack.push_left(1)
        stack.push_left(2)
        stack.push_left(3)
        self.assertTrue(stack.pop_left() == 3)
        self.assertTrue(stack.pop_left() == 2)
        self.assertTrue(stack.pop_left() == 1)
        self.assertTrue(stack.pop_left() is None)
        self.assertTrue(stack.pop_right() is None)

    def test_two_side_push_right(self):
        stack = Stack2Side(3)
        stack.push_right(1)
        stack.push_right(2)
        stack.push_right(3)
        self.assertTrue(stack.pop_right() == 3)
        self.assertTrue(stack.pop_right() == 2)
        self.assertTrue(stack.pop_right() == 1)
        self.assertTrue(stack.pop_right() is None)
        self.assertTrue(stack.pop_left() is None)

    def test_two_side_push(self):
        stack = Stack2Side(3)
        stack.push_left(1)
        stack.push_right(2)
        stack.push_right(3)
        self.assertTrue(stack.pop_right() == 3)
        self.assertTrue(stack.pop_right() == 2)
        self.assertTrue(stack.pop_right() is None)
        self.assertTrue(stack.pop_left() == 1)
        self.assertTrue(stack.pop_left() is None)


if __name__ == '__main__':
    unittest.main()
