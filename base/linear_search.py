def linear_search(array, value):
    result = []
    for idx in range(array.__len__()):
        if array[idx] == value:
            result.append(idx)
    if result.__len__() == 0:
        return -1
    else:
        return result

print(linear_search([1,2,3,4,5,6,3,3], 3))
print(linear_search([6,1,2,3,4,6,5,6], 6))
print(linear_search([1,2,3,4,5,6], 11))

print(linear_search([1,6,15,41,20,14,2], 41))
print(linear_search([1,6,15,41,20,14,2], 14))
print(linear_search([1,6,15,41,20,14,2], 44))