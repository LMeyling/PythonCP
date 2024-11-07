# Status: checked
def is_prime(n):
    'O(logN) miller rabin algorithm'
    if n == 2: return 1
    if n == 1 or not n&1: return 0
    #miller_rabin
    if n < 1<<30: test_numbers = [2, 7, 61]
    else: test_numbers = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    d = n - 1
    while ~d&1: d>>=1
    for a in test_numbers:
        if n <= a: break
        t = d
        y = pow(a, t, n)
        while t != n-1 and y != 1 and y != n-1:
            y = y * y % n
            t <<= 1
        if y != n-1 and not t&1: return 0
    return 1