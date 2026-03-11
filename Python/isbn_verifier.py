def is_valid(isbn):
    isbn = isbn.replace('-', '')
    n = len(isbn)
    if n != 10 or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
        return False

    total = 0
    for i in range(n):
        c = isbn[i]
        if i < 9 and not c.isdigit():
            return False

        if c == 'X':
            total += 10 * (10 - i)
        else:
            total += int(c) * (10 - i)

    return total % 11 == 0
