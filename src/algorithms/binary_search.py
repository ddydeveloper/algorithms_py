import sys


def binary_search(arr, value, min_idx=None, max_idx=None, first_idx=True):
    if min_idx is None:
        min_idx = 0

    if max_idx is None:
        max_idx = len(arr) - 1

    if min_idx > max_idx:
        return -1

    middle_idx = (min_idx + max_idx) // 2

    if value == arr[middle_idx]:
        if first_idx:
            return first_in_array(arr, middle_idx)
        else:
            return last_in_array(arr, middle_idx, len(arr) - 1)

    if value > arr[middle_idx]:
        min_idx = middle_idx + 1
    else:
        max_idx = middle_idx - 1

    return binary_search(arr, value, min_idx, max_idx)


def first_in_array(arr, idx):
    if idx == 0 or arr[idx] != arr[idx - 1]:
        return idx
    return first_in_array(arr, idx - 1)


def last_in_array(arr, idx, max_idx):
    if idx == max_idx or arr[idx] != arr[idx + 1]:
        return idx
    return last_in_array(arr, idx + 1, max_idx)


def main():
    arr = sys.argv[1:]
    value = arr.pop(0)
    print(binary_search(arr, value))


if __name__ == '__main__':
    main()
