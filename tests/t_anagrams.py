import unittest
from src.scripts.anagrams import anagrams_string_count


class TestStringFunc(unittest.TestCase):
    def test_anagram_of_0(self):
        string_value = "abcd"
        result = anagrams_string_count(string_value)

        self.assertTrue(result == 0)

    def test_anagram_of_3(self):
        string_value = "ifailuhkqq"
        result = anagrams_string_count(string_value)

        self.assertTrue(result == 3)

    def test_anagram_of_4(self):
        string_value = "abba"
        result = anagrams_string_count(string_value)

        self.assertTrue(result == 4)

    def test_anagram_of_5(self):
        string_value = "cdcd"
        result = anagrams_string_count(string_value)

        self.assertTrue(result == 5)

    def test_anagram_of_10(self):
        string_value = "kkkk"
        result = anagrams_string_count(string_value)

        self.assertTrue(result == 10)
