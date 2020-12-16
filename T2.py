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

if __name__ == "__main__":
    factor_set = get_prime_factors(213)
    print(factor_set)