def linear_search(array, value):
    result = []
    for idx in range(array.__len__()):
        if array[idx] == value:
            result.append(idx)
    if result.__len__() == 0:
        return -1
    else:
        return result
