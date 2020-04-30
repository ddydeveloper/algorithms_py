import os


class AnagramsContainer:
    def __init__(self, s):
        self.d = {}
        for char in s:
            self.increment(char)

    def _create_if_not_exists(self, char):
        if char not in self.d:
            self.d[char] = 0

    def _del_if_zero(self, char):
        if self.d[char] == 0:
            del self.d[char]

    def is_empty(self):
        return not self.d

    def decrement(self, char):
        self._create_if_not_exists(char)
        self.d[char] -= 1
        self._del_if_zero(char)

    def increment(self, char):
        self._create_if_not_exists(char)
        self.d[char] += 1
        self._del_if_zero(char)


def anagrams_count(pattern, s):
    result = 0

    freq = AnagramsContainer(pattern)

    for char in s[:len(pattern)]:
        freq.decrement(char)

    if freq.is_empty():
        result += 1

    for i in range(len(pattern), len(s)):
        start_char, end_char = s[i - len(pattern)], s[i]
        freq.increment(start_char)
        freq.decrement(end_char)
        if freq.is_empty():
            result += 1

    return result


def anagrams_string_count(s):
    anagrams = 0
    str_length = len(s)

    # length of pattern
    size = 1

    # pattern starts from
    step = 0

    cur_pattern = ""

    while len(cur_pattern) < str_length:
        if step == str_length - 1:
            size += 1
            step = 0
            continue

        cur_pattern = s[step:step + size]
        cur_str = s[step + 1:]

        if len(cur_pattern) <= len(cur_str):
            anagrams += anagrams_count(cur_pattern, cur_str)

        step += 1

    return anagrams


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagrams_string_count(s)

        fptr.write(str(result) + '\n')

    fptr.close()