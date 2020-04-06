def linear_search(array, value):
    result = []
    for idx in range(array.__len__()):
        if array[idx] == value:
            result.append(idx)
    if result.__len__() == 0:
        return -1
    else:
        return result


def binary_search(arr, value, min_idx=None, max_idx=None):
    if min_idx is None:
        min_idx = 0

    if max_idx is None:
        max_idx = len(arr) - 1

    if min_idx > max_idx:
        return -1

    middle_idx = (min_idx + max_idx) // 2

    if value == arr[middle_idx]:
        return first_in_array(arr, middle_idx)

    if value > arr[middle_idx]:
        min_idx = middle_idx + 1
    else:
        max_idx = middle_idx - 1

    return binary_search(arr, value, min_idx, max_idx)


def first_in_array(arr, idx):
    if arr[idx] != arr[idx - 1]:
        return idx
    return first_in_array(arr, idx - 1)
