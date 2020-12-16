import sys
import math

def prime(n):                       # Returns whether n is prime
    for i in range(2, n):           # Starts at 2 because that is first prime
        if n % i == 0:
            return False            # If n is divisible by i, n is not prime
    
    return True                     # Otherwise, n is prime

def get_relative_primes(n):         # Returns a list of relative primes less than n
    rel_primes = []

    for i in range(1, n):
        if math.gcd(i, n) == 1 and prime(i):
            rel_primes.append(i)

    return rel_primes

def get_prime_factors(n):           # Returns a list of the prime factors of n
    if prime(n):
        return {}

    factor_set = set()              # Set, so there are no repeat elements
    o = n                           # o is a copy of n

    for i in range(n):
        if i > 1:                   # Skip integers >= 1
            while o % i == 0:      # while o is even
                factor_set.add(i)   # Add i to the set
                o = o / i           # o /= i

    return factor_set

def phi(n):
    result = n
    primes = get_prime_factors(n)

    if len(primes) == 0:
        return n

    for p in primes:
        result = result * (1 - (1 / p))

    return int(result)

if __name__ == "__main__":
    vals = []
    for i in range(2, 26):
        vals.append(i)

    print("--------------------------------Problem (a)--------------------------------")
    for v in vals:
        v_primes = get_relative_primes(v)
        print(f"Relative primes less than {v}: {v_primes}\t\tϕ({v}) = {len(v_primes)} (based on list size)")
    print("\nThe pattern is whenever n is greater than the last prime number, that last prime number is ")
    print("one of the next n's relative primes. And as n increases, the list of relative primes ")
    print("iterates through various combinations of the previous relatives primes.")
    print("---------------------------------------------------------------------------\n")

    print("--------------------------------Problem (b)--------------------------------")
    for v in vals:
        print(f"Prime factors of {v}: {get_prime_factors(v)}\t\tϕ({v}) = {phi(v)} (based on formula)")
    print("\nϕ(n) usually differs between the list size and the formula. It only matches with some ")
    print("values of n when n is a composite number.")
    print("---------------------------------------------------------------------------")