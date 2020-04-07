import unittest

from src.algorithms.hash_table import HashTable


class TestArray(unittest.TestCase):
    def test_hash_resize(self):
        ht = HashTable(2)
        ht.insert(617, "a")
        ht.insert(313, "b")
        ht.insert(254, "c")
        ht.insert(123, "d")
        ht.insert(637, "e")
        self.assertTrue(ht.__str__() == "0->[254:c] 1->[637:e;123:d;313:b;617:a]")

        ht.change_size(5)
        self.assertTrue(ht.__str__() == "0->[] 1->[] 2->[617:a;637:e] 3->[313:b;123:d] 4->[254:c]")


if __name__ == '__main__':
    unittest.main()
