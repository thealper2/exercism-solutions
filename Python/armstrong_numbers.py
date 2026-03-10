def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    p = len(digits)
    return True if sum([digit ** p for digit in digits]) == number else False
