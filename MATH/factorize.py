# Status: checked
import math
from functools import reduce


# Helper function for modular multiplication
def mod_mul(a, b, M):
    res = a * b - M * int(1 / M * a * b)
    return res + M * (res < 0) - M * (res >= M)


# Helper function for modular exponentiation
def mod_pow(b, e, mod):
    res = 1
    while e:
        if e & 1:
            res = mod_mul(res, b, mod)
        b = mod_mul(b, b, mod)
        e >>= 1
    return res


# Function to count trailing zeros in binary representation
def count_trailing_zeros(n):
    if n == 0:
        return 0
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


# Miller-Rabin primality test
def is_prime(n):
    if n < 2 or n % 6 % 4 != 1:
        return (n | 1) == 3
    if n == 13:
        return True

    s = count_trailing_zeros(n - 1)
    d = (n - 1) >> s

    # Witnesses for Miller-Rabin test (deterministic for n < 2^64)
    witnesses = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    for a in witnesses:
        p = mod_pow(a, d, n)
        i = s
        while p != 1 and p != n - 1 and a % n != 0 and i > 0:
            p = mod_mul(p, p, n)
            i -= 1
        if p != n - 1 and i != s:
            return False

    return True


# Pollard's Rho algorithm to find a factor of n
def get_factor(n):
    def f(x):
        return mod_mul(x, x, n) + 1

    x = y = prd = 2
    i = 1
    t = 30

    while t % 40 != 0 or math.gcd(prd, n) == 1:
        if x == y:
            i += 1
            x = i
            y = f(x)
        q = mod_mul(prd, abs(x - y), n)
        if q != 0:
            prd = q
        x = f(x)
        y = f(f(y))
        t += 1

    return math.gcd(prd, n)


# Factorize the number n into prime factors
def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    x = get_factor(n)
    left_factors = factorize(x)
    right_factors = factorize(n // x)
    # Remove duplicates
    return left_factors + right_factors