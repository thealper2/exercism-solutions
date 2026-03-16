def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    counter = 1
    n = 2
    while True:
        prime = is_prime(n)
        if prime and counter == number:
            return n

        if prime:
            counter += 1

        n += 1

    return -1
    
