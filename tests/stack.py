import unittest
from scr import stack_node_based


class TestStack(unittest.TestCase):
    def test_pop(self):
        stack = stack_node_based.Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.pop() == 3)
        self.assertTrue(stack.pop() == 2)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_push(self):
        stack = stack_node_based.Stack()
        stack.push(1)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_peek(self):
        stack = stack_node_based.Stack()
        self.assertTrue(stack.peek() is None)
        stack.push(1)
        stack.push(2)
        self.assertTrue(stack.peek() == 2)
        stack.pop()
        self.assertTrue(stack.peek() == 1)
        stack.pop()
        self.assertTrue(stack.peek() is None)

    def test_count(self):
        stack = stack_node_based.Stack()
        self.assertTrue(stack.count() == 0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)

    def test_clear(self):
        stack = stack_node_based.Stack()
        self.assertTrue(stack.peek() is None)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.peek() == 3)
        stack.clear()
        self.assertTrue(stack.peek() is None)


if __name__ == '__main__':
    unittest.main()
