import unittest
from scr import stack_array_based


class TestStack(unittest.TestCase):
    def test_pop(self):
        stack = stack_array_based.Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.pop() == 3)
        self.assertTrue(stack.pop() == 2)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_pop_overflow(self):
        stack = stack_array_based.Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.push(4)

    def test_push(self):
        stack = stack_array_based.Stack(3)
        stack.push(1)
        self.assertTrue(stack.pop() == 1)
        self.assertTrue(stack.pop() is None)

    def test_count(self):
        stack = stack_array_based.Stack(3)
        stack.push(1)
        self.assertTrue(stack.count() == 1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)

    def test_clear(self):
        stack = stack_array_based.Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.count() == 3)
        stack.clear()
        self.assertTrue(stack.count() == 0)

if __name__ == '__main__':
    unittest.main()
