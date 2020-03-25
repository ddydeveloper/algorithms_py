import unittest
from src.data_structures.array import Array, merge


class TestArray(unittest.TestCase):
    def test_remove_single(self):
        array = Array(4)
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.remove(2)

        self.assertTrue(len(array) == 3)
        self.assertTrue(str(array) == '[1, 3, 4]')

    def test_remove(self):
        array = Array(4)
        array.append(1)
        array.append(2)
        array.append(2)
        array.append(4)
        array.remove(2)

        self.assertTrue(len(array) == 2)
        self.assertTrue(str(array) == '[1, 4]')

    def test_merge(self):
        array1 = [1, 4, 8, 15]
        array2 = [2, 3, 5, 9, 12]

        array = merge(array1, array2)
        self.assertTrue(len(array) == 9)
        self.assertTrue(str(array) == '[1, 2, 3, 4, 5, 8, 9, 12, 15]')

        array = merge(array2, array1)
        self.assertTrue(len(array) == 9)
        self.assertTrue(str(array) == '[1, 2, 3, 4, 5, 8, 9, 12, 15]')


if __name__ == '__main__':
    unittest.main()
