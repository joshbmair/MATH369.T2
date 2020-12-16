import sys
import math

def get_prime_factors(n):
    factor_set = set()
    o = n

    for index in range(n):
        if index > 1:
            while o % index == 0:
                factor_set.add(index)
                o = o / index

    return factor_set

def phi(n):
    res = n
    primes = get_prime_factors(n)

    for p in primes:
        res = res * (1 - (1 / p))

    return math.ceil(res)

if __name__ == "__main__":
    n = 12
    factor_set = get_prime_factors(n)
    print(f"Prime factors of {n}: {factor_set}")
    print(f"ϕ({n}): {phi(n)}")