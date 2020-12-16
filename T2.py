import sys

def prime(n):                       # Returns whether n is prime
    for i in range(2, n):           # FIXME? Starts at 2 because that is first prime
        if not (n % i):
            return False            # If n is divisible by i, n is not prime
    
    return True                     # Otherwise, n is prime

def get_primes(n):                  # Gets primes less than n
    primes_list = []

    for i in range(2, n + 1):       # Starts at 2 because that is first prime
        if prime(i):
            primes_list.append(i)
            
    return primes_list  

def get_relative_primes(n):         # Gets relative primes less than n
    primes = get_primes(n)          # 

    for i in range(2, n + 1):
        print(i) # TODO

    return primes

def get_prime_factors(n):
    factor_set = set()              # Set, so there no repeat elements
    o = n                           # o is a copy of n

    for i in range(n):
        if i > 1:                   # Skip integers >= 1
            while not (o % i):      # while o is even
                factor_set.add(i)   # Add i to the set
                o = o / i           # o /= i

    return factor_set

def phi(n):
    res = n
    primes = get_prime_factors(n)

    for p in primes:
        res = res * (1 - (1 / p))

    return int(res)

if __name__ == "__main__":
    vals = []

    for i in range(2, 26):
        vals.append(i)

    print(vals)

    n = 12
    factor_set = get_prime_factors(n)
    print(f"Prime factors of {n}: {factor_set}")
    print(f"ϕ({n}): {phi(n)}")