# Status: checked
# conv from https://judge.yosupo.jp/submission/41422
mod = 998244353 # Only works for this MOD
g = 3
ginv = pow(g,-1,mod)
W = [pow(g, (mod - 1) >> i, mod) for i in range(24)]
Winv = [pow(ginv, (mod - 1) >> i, mod) for i in range(24)]

def fft(k, f):
    for l in range(k, 0, -1):
        d = 1 << l - 1
        U = [1]
        for i in range(d):
            U.append(U[-1] * W[l] % mod)
        for i in range(1 << k - l):
            for j in range(d):
                s = i * 2 * d + j
                f[s], f[s + d] = (f[s] + f[s + d]) % mod, U[j] * (f[s] - f[s + d]) % mod


def fftinv(k, f):
    for l in range(1, k + 1):
        d = 1 << l - 1
        for i in range(1 << k - l):
            u = 1
            for j in range(i * 2 * d, (i * 2 + 1) * d):
                f[j + d] *= u
                f[j], f[j + d] = (f[j] + f[j + d]) % mod, (f[j] - f[j + d]) % mod
                u *= Winv[l]
                u %= mod


def convolution(a, b):
    le = len(a) + len(b) - 1
    k = le.bit_length()
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    fft(k, a)
    fft(k, b)
    for i in range(n):
        a[i] *= b[i]
        a[i] %= mod
    fftinv(k, a)

    ninv = pow(n, mod - 2, mod)
    for i in range(le):
        a[i] *= ninv
        a[i] %= mod

    return a[:le]

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*convolution(A, B))