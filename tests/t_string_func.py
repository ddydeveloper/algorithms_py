import unittest
from src.scripts.string_func import wrap_string, swap_vowels


class TestStringFunc(unittest.TestCase):
    def test_wrap_none(self):
        self.assertTrue(wrap_string(None) is None)

    def test_wrap_empty(self):
        str_value = "   "
        self.assertTrue(wrap_string(str_value) == str_value)

    def test_wrap_single_char(self):
        str_value = "F"
        self.assertTrue(wrap_string(str_value) == str_value)

    def test_wrap_single_letters(self):
        str_value = "BCDFGAEI"
        self.assertTrue(wrap_string(str_value) == str_value)

    def test_wrap_multi_end(self):
        str_value = "AAAAAAABBCCCDDDFFFRRRTONNXX"
        str_wrapped = wrap_string(str_value)
        self.assertTrue(str_wrapped == "A7B2C3D3F3R3TON2X2")

    def test_wrap_single_end(self):
        str_value = "AAAAAAABBCCCDDDFFFRRRTONNXXY"
        self.assertTrue(wrap_string(str_value) == "A7B2C3D3F3R3TON2X2Y")

    def test_swap_vowels_none(self):
        self.assertTrue(swap_vowels(None) is None)

    def test_swap_vowels_empty(self):
        str_value = "   "
        self.assertTrue(swap_vowels(str_value) == str_value)

    def test_swap_vowels_single_char(self):
        str_value = "A"
        self.assertTrue(swap_vowels(str_value) == str_value)

    def test_swap_vowels_single_vowel(self):
        str_value = "What?"
        self.assertTrue(swap_vowels(str_value) == str_value)

    def test_swap_vowels_two_same_vowels(self):
        str_value = "What's app?"
        str_swapped = swap_vowels(str_value)
        self.assertTrue(str_swapped == "What's app?")

    def test_swap_vowels_two_different_vowels(self):
        str_value = "What's up?"
        str_swapped = swap_vowels(str_value)
        self.assertTrue(str_swapped == "Whut's ap?")

    def test_swap_vowels(self):
        str_value = "I am a doctor here, OK?"
        str_swapped = swap_vowels(str_value)
        self.assertTrue(str_swapped == "O em e doctor hara, IK?")
