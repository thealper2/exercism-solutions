def primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(2 * i, limit + 1, i):
                is_prime[j] = False

    result = [i for i in range(limit + 1) if is_prime[i]]
    return result
