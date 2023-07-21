import sys

sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
tmp = 2 ** n
t = [0 for _ in range(tmp * 4)]


def build(arr, v, tl, tr):
    if tl == tr:
        t[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(arr, v * 2, tl, tm)
        build(arr, v * 2 + 1, tm + 1, tr)
        # If Abfrage abändern je nachdem welche levels im Baum man betrachten möchte
        if tl == tm:
            t[v] = t[v * 2] | t[v * 2 + 1]
        else:
            t[v] = t[v * 2] ^ t[v * 2 + 1]


def update(v, tl, tr, pos, new_val):
    if tl == tr == pos:
        t[v] = new_val
    elif tl <= pos <= tr:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(v * 2, tl, tm, pos, new_val)
        else:
            update((v * 2) + 1, tm + 1, tr, pos, new_val)
        # If Abfrage abändern je nachdem welche levels im Baum man betrachten möchte
        if tl == tm:
            t[v] = t[v * 2] | t[v * 2 + 1]
        else:
            t[v] = t[v * 2] ^ t[v * 2 + 1]


