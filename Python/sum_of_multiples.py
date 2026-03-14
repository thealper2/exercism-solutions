def sum_of_multiples(limit, multiples):
    multiples = [n for n in multiples if n > 0]
    result = set()
    for multiple in multiples:
        i = 1
        while multiple * i < limit:
            result.add(multiple * i)
            i += 1

    return sum(result)
