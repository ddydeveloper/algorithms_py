# The function below should replace "AAAAAAABBCCCDDDFFFRRRTONNXX" with the "A7B2C3D3F3R3TON2X2"
def wrap_string(value):
    if value is None:
        return None

    if value.isspace():
        return value

    str_length = len(value)
    cur_char = None
    cur_count = 1
    result = []

    for i in range(str_length):
        char = value[i]

        if cur_char is None:
            cur_char = char
            continue

        if char == cur_char:
            cur_count += 1
            continue

        result.append(cur_char)

        if cur_count > 1:
            result.append(str(cur_count))

        cur_char = char
        cur_count = 1

    result.append(cur_char)

    if cur_count > 1:
        result.append(str(cur_count))

    return "".join(result)


# The function below should swap vowels only order
def swap_vowels(value):
    if value is None:
        return None

    if value.isspace() or len(value) == 1:
        return value

    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    vowels_stack = []
    result = []
    str_length = len(value)

    for i in range(str_length):
        char = value[i]
        if char.lower() in vowels:
            vowels_stack.append(value[i])
            result.append(None)
        else:
            result.append(char)

    for i in range(str_length):
        if result[i] is None:
            result[i] = vowels_stack.pop()

    return "".join(result)
