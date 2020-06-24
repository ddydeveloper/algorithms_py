import unittest

from src.data_structures.trees.dijkstra import main


class TestArray(unittest.TestCase):
    def test_hash_resize(self):
        result = main()
        expected = {0: 0, 1: 5, 4: 5, 2: 15, 3: 9, 6: 11, 7: 10, 8: 13, 5: 14, 9: 20, 10: 14}
        self.assertTrue(result == expected)


if __name__ == '__main__':
    unittest.main()
