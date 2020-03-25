import unittest

from src.algorithms.sort import bubble_sort


class TestArray(unittest.TestCase):
    def bubble_sort(self):
        array = [13, 7, 8, 2, 11, 5]
        bubble_sort(array)
        self.assertTrue(array[0] == 13)
        self.assertTrue(array[1] == 11)
        self.assertTrue(array[2] == 8)
        self.assertTrue(array[3] == 7)
        self.assertTrue(array[4] == 5)
        self.assertTrue(array[5] == 2)


if __name__ == '__main__':
    unittest.main()
