class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"

    def __len__(self):
        return self.length

    def append(self, value):
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def insert(self, index, value):
        if index >= self.length or index < 0 or index is None:
            raise IndexError()
        if self.size == self.length:
            raise OverflowError()

        shifted = [None] * self.size
        shifted[index] = value

        for idx, item in enumerate(self.data[:self.length]):
            if idx < index:
                shifted[idx] = item
            if idx >= index:
                shifted[idx + 1] = item

        self.data = shifted
        self.length += 1

    def min(self):
        if self.length == 0 or self.size == 0:
            return None

        min_value = None
        for value in self.data:
            if value is None:
                continue
            if min_value is None:
                min_value = value
                continue
            if value >= min_value:
                continue
            min_value = value

        return min_value

    def max(self):
        if self.length == 0 or self.size == 0:
            return None

        max_value = None
        for value in self.data:
            if value is None:
                continue
            if max_value is None:
                max_value = value
                continue
            if value <= max_value:
                continue
            max_value = value

        return max_value

    def avg(self):
        if self.length == 0 or self.size == 0:
            return None

        array_sum = 0
        array_count = 0

        for value in self.data:
            if value is None:
                continue
            array_sum += value
            array_count += 1

        return array_sum / array_count

    def reverse(self):
        if self.size <= 1 or self.length <= 1:
            return self.data

        middle_idx = None
        is_even = False
        reverse_array = [None] * self.length

        if self.length % 2 == 0:
            middle_idx = self.length // 2
            is_even = True
        else:
            middle_idx = (self.length - 1) // 2

        i = 0
        while i < middle_idx:
            reverse_idx = self.length - 1 - i
            reverse_array[i] = self.data[reverse_idx]
            reverse_array[reverse_idx] = self.data[i]
            i += 1

        if not is_even:
            reverse_array[middle_idx] = self.data[middle_idx]

        self.data = reverse_array

    def remove_single(self, value):
        if self.length == 0 or self.size == 0:
            return

        if self.length == 1 and self.data[0] != value:
            return

        shifted = [None] * self.size
        is_found = False
        for idx, current in enumerate(self.data[:self.length]):
            if current == value:
                if self.is_last_item(idx):
                    shifted[idx] = None
                else:
                    shifted[idx] = self.data[idx + 1]
                is_found = True
            else:
                if is_found:
                    if self.is_last_item(idx):
                        shifted[idx] = None
                    else:
                        shifted[idx] = self.data[idx + 1]
                else:
                    shifted[idx] = current

        if is_found:
            self.data = shifted
            self.length -= 1

    def remove(self, value):
        if self.length == 0 or self.size == 0:
            return

        if self.length == 1 and self.data[0] != value:
            return

        shifted_idx = 0
        removed_count = 0
        shifted = [None] * self.size

        for current in self.data[:self.length]:
            if current != value:
                shifted[shifted_idx] = current
                shifted_idx += 1
            else:
                removed_count += 1

        if removed_count > 0:
            self.data = shifted
            self.length -= removed_count

    def is_last_item(self, idx):
        return idx == self.length - 1


def merge(array1, array2):
    result = []
    array1_idx = 0

    array2_to_reduce = array2[:]

    for value in array1:
        if len(array2) == 0:
            break

        array2_part = list(filter(lambda item: item <= value, array2_to_reduce))
        array2_to_reduce = array2_to_reduce[len(array2_part):]

        result += array2_part
        result.append(value)
        array1_idx += 1

    if len(array1) - 1 > array1_idx:
        result += array1[array1_idx:]

    if len(array2_to_reduce) > 0:
        result += array2_to_reduce

    return result
