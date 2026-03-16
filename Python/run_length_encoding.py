def decode(string):
    result = []
    num = ""

    for char in string:
        if char.isdigit():
            num += char
        else:
            count = int(num) if num else 1
            result.append(char * count)
            num = ""

    return "".join(result)


def encode(string):
    if not string:
        return ""

    result = []
    count = 1
    prev_char = string[0]
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))

            result.append(prev_char)
            prev_char = char
            count = 1

    if count > 1:
        result.append(str(count))

    result.append(prev_char)
    return "".join(result)
