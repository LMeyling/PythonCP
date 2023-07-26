def LIS(A, strict=True):
    # 最長増加部分列(strict=Falseで広義単調増加になる)
    from bisect import bisect_left
    T = []
    position = []

    for a in A:
        if len(T) == 0 or (strict and T[-1] < a) or (not strict and T[-1] <= a):
            position.append(len(T))
            T.append(a)
        else:
            if strict:
                k = bisect_left(T, a)
            else:
                k = bisect_left(T, a + 1)
            position.append(k)
            T[k] = a

    res = []
    t = len(T) - 1
    for i, p in enumerate(reversed(position)):
        if t == p:
            res.append(len(A) - 1 - i)
            t -= 1
    res.reverse()
    return res
