import unittest
from src.data_structures.c_array import CustomArray, merge


class TestArray(unittest.TestCase):
    def test_remove_single(self):
        custom_array = CustomArray(4)
        custom_array.append(1)
        custom_array.append(2)
        custom_array.append(3)
        custom_array.append(4)
        custom_array.remove(2)

        self.assertTrue(len(custom_array) == 3)
        self.assertTrue(str(custom_array) == '[1, 3, 4]')

    def test_remove(self):
        custom_array = CustomArray(4)
        custom_array.append(1)
        custom_array.append(2)
        custom_array.append(2)
        custom_array.append(4)
        custom_array.remove(2)

        self.assertTrue(len(custom_array) == 2)
        self.assertTrue(str(custom_array) == '[1, 4]')

    def test_merge(self):
        array1 = [1, 4, 8, 15]
        array2 = [2, 3, 5, 9, 12]

        custom_array = merge(array1, array2)
        self.assertTrue(len(custom_array) == 9)
        self.assertTrue(str(custom_array) == '[1, 2, 3, 4, 5, 8, 9, 12, 15]')

        custom_array = merge(array2, array1)
        self.assertTrue(len(custom_array) == 9)
        self.assertTrue(str(custom_array) == '[1, 2, 3, 4, 5, 8, 9, 12, 15]')


if __name__ == '__main__':
    unittest.main()
