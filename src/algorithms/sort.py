def bubble_sort(array):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        n = 1

        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i+1], array[i]
                is_sorted = False
                n += 1


def merge_sort(array):
    temp_array = [None] * len(array)
    do_merge_sort(array, temp_array, 0, len(array) - 1)


def do_merge_sort(array, temp_array, start, end):
    if start == end:
        return

    mid_point = (start + end) // 2

    do_merge_sort(array, temp_array, start, mid_point)
    do_merge_sort(array, temp_array, mid_point + 1, end)

    left_idx = start
    right_idx = mid_point + 1
    temp_array_idx = left_idx

    while (left_idx <= mid_point) and (right_idx <= end):
        if array[left_idx] < array[right_idx]:
            temp_array[temp_array_idx] = array[left_idx]
            left_idx += 1
        else:
            temp_array[temp_array_idx] = array[right_idx]
            right_idx += 1
        temp_array_idx += 1

    for i in range(left_idx, mid_point + 1):
        temp_array[temp_array_idx] = array[i]
        temp_array_idx += 1

    for i in range(right_idx, end + 1):
        temp_array[temp_array_idx] = array[i]
        temp_array_idx += 1

    for i in range(start, end + 1):
        array[i] = temp_array[i]


def counting_sort(array):
    negative_values = [i for i in array if i < 0]
    if len(negative_values) == 0:
        min_value = 0
    else:
        min_value = min(array)

    max_value = max(array)
    counts = [0] * (max_value - min_value + 1)

    for value in array:
        counts[value] += 1

    index = 0
    for i in range(min_value, max_value + 1):
        for j in range(0, counts[i]):
            array[index] = i
            index += 1
