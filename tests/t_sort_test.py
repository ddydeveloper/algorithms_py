import unittest
from src.algorithms.sort import bubble_sort, quick_sort, merge_sort, stack_based_quick_sort


class TestArray(unittest.TestCase):
    def test_bubble_sort(self):
        array = [13, 7, 8, 2, 11, 5]
        bubble_sort(array)
        self.assertTrue(array[0] == 13)
        self.assertTrue(array[1] == 11)
        self.assertTrue(array[2] == 8)
        self.assertTrue(array[3] == 7)
        self.assertTrue(array[4] == 5)
        self.assertTrue(array[5] == 2)

    def test_quick_sort(self):
        array = [7, 5, 0, 1, -5, 8, 0, -4]
        quick_sort(array)
        self.assertTrue(array[0] == -5)
        self.assertTrue(array[1] == -4)
        self.assertTrue(array[2] == 0)
        self.assertTrue(array[3] == 0)
        self.assertTrue(array[4] == 1)
        self.assertTrue(array[5] == 5)
        self.assertTrue(array[6] == 7)
        self.assertTrue(array[7] == 8)

    def test_stack_based_quick_sort(self):
        array = [7, 5, 0, 1, -5, 8, 0, -4]
        stack_based_quick_sort(array)
        self.assertTrue(array[0] == -5)
        self.assertTrue(array[1] == -4)
        self.assertTrue(array[2] == 0)
        self.assertTrue(array[3] == 0)
        self.assertTrue(array[4] == 1)
        self.assertTrue(array[5] == 5)
        self.assertTrue(array[6] == 7)
        self.assertTrue(array[7] == 8)

    def test_merge_sort(self):
        array = [7, 5, 0, 1, -5, 8, 0, -4]
        merge_sort(array)
        self.assertTrue(array[0] == -5)
        self.assertTrue(array[1] == -4)
        self.assertTrue(array[2] == 0)
        self.assertTrue(array[3] == 0)
        self.assertTrue(array[4] == 1)
        self.assertTrue(array[5] == 5)
        self.assertTrue(array[6] == 7)
        self.assertTrue(array[7] == 8)


if __name__ == '__main__':
    unittest.main()
