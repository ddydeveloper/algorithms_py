import unittest
from src.algorithms.search import binary_search


class TestArray(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 20, 30, 30, 30, 30, 30, 40, 50, 60]

        idx = binary_search(array, 3)
        self.assertTrue(idx == 2)

        idx = binary_search(array, 8)
        self.assertTrue(idx == 11)

        idx = binary_search(array, 30)
        self.assertTrue(idx == 16)


if __name__ == '__main__':
    unittest.main()
