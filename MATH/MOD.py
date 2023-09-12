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
