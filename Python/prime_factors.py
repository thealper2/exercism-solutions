def factors(value):
    if value < 2:
        return []

    result = []
    divisor = 2
    while value > 1:
        if value % divisor == 0:
            value //= divisor
            result.append(divisor)
        else:
            divisor += 1

    return result
