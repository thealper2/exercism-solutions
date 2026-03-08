def is_triangle(sides):
    a, b, c = sides
    if a == 0 and b == 0 and c == 0:
        return False

    if a + b < c or b + c < a or a + c < b:
        return False

    return True


def equilateral(sides):
    return 2 < equal_sides(sides)


def isosceles(sides):
    return 2 <= equal_sides(sides)


def scalene(sides):
    return 0 == equal_sides(sides)

def equal_sides(sides):
    if not is_triangle(sides):
        return -1

    equals = 0
    for i in range(3):
        for j in range(3):
            if sides[i] == sides[j]:
                equals += 1

    return equals - 3
