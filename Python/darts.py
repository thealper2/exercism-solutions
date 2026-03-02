def score(x, y):
    v = (x ** 2 + y ** 2) ** 0.5
    if v <= 1:
        return 10
    if v <= 5:
        return 5
    if v <= 10:
        return 1

    return 0
