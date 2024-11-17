# Status: checked
MOD = 998244353
 
fac_arr = [1]
finv_arr = [1]
 
def enlarge_fac():
    old_size = len(fac_arr)
    new_size = old_size * 2
    for i in range(old_size, new_size + 1):
        fac_arr.append((fac_arr[-1] * i) % MOD)
        finv_arr.append(pow(fac_arr[-1], -1, MOD))
 
def fac(n):
    while n >= len(fac_arr): enlarge_fac()
    return fac_arr[n]
 
def finv(n):
    while n >= len(finv_arr): enlarge_fac()
    return finv_arr[n]
 
def binom(n, k):
    if k < 0 or k > n: return 0
    return ((fac(n) * finv(k)) % MOD * finv(n - k)) % MOD

import math
def solve_first_occurrence(a, b, c, d,m):
    a_prime = a - c
    k = b - d

    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return (g, x, y)

    g, x, y = extended_gcd(a_prime % m, m)

    if k % g != 0:
        return None  # No solution exists

    # Simplify the equation
    a_double_prime = a_prime // g
    k_double_prime = k // g
    m_double_prime = m // g

    inv_a = pow(a_double_prime % m_double_prime, -1, m_double_prime)
    if inv_a is None:
        return None  # No solution exists
    i0 = (inv_a * (-k_double_prime)) % m_double_prime
    if i0 < 0:
        i0 += m_double_prime

    return i0
def calc_col(a,b,c,d,t):
    if a < c:
        a,c = c,a
        b,d = d,b
    first_oc = solve_first_occurrence(a,b,c,d,H)
    if first_oc is None:
        return - 1
    else:
        freq =  H // math.gcd(a-c,H)
        x = (t // freq) * freq
        x += first_oc
        if x < t:
            x+= freq
        return x
