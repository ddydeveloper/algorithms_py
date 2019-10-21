import unittest
from scr import stack_2_side


class TestStack(unittest.TestCase):
    def test_push_left(self):
        stack = stack_2_side.Stack(3)
        stack.push_left(1)
        stack.push_left(2)
        stack.push_left(3)
        self.assertTrue(stack.pop_left() == 3)
        self.assertTrue(stack.pop_left() == 2)
        self.assertTrue(stack.pop_left() == 1)
        self.assertTrue(stack.pop_left() is None)
        self.assertTrue(stack.pop_right() is None)

    def test_push_right(self):
        stack = stack_2_side.Stack(3)
        stack.push_right(1)
        stack.push_right(2)
        stack.push_right(3)
        self.assertTrue(stack.pop_right() == 3)
        self.assertTrue(stack.pop_right() == 2)
        self.assertTrue(stack.pop_right() == 1)
        self.assertTrue(stack.pop_right() is None)
        self.assertTrue(stack.pop_left() is None)

    def test_push(self):
        stack = stack_2_side.Stack(3)
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
