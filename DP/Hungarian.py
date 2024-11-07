# Status: checked
def hungarian(A):
    inf = 1 << 40
    n = len(A) + 1
    m = len(A[0]) + 1
    P = [0] * m
    way = [0] * m
    U = [0] * n
    V = [0] * n
    for i in range(1, n):
        P[0] = i
        minV = [inf] * m
        used = [False] * m
        j0 = 0
        while P[j0] != 0:
            i0 = P[j0]
            j1 = 0
            used[j0] = True
            delta = inf
            for j in range(1, m):
                if used[j]:
                    continue
                if i0 == 0 or j == 0:
                    cur =  -U[i0] - V[j]
                else:
                    cur = A[i0 - 1][j - 1] - U[i0] - V[j]
                if cur < minV[j]:
                    minV[j] = cur
                    way[j] = j0
                if minV[j] < delta:
                    delta = minV[j]
                    j1 = j
            for j in range(m):
                if used[j]:
                    U[P[j]] += delta
                    V[j] -= delta
                else:
                    minV[j] -= delta
            j0 = j1
        P[j0] = P[way[j0]]
        j0 = way[j0]
        while j0 != 0:
            P[j0] = P[way[j0]]
            j0 = way[j0]
    
    ret = [-1] * (n - 1)
    for i in range(1, m):
        if P[i] != 0:
            ret[P[i] - 1] = i - 1
    return -V[0], ret
