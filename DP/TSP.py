# Status: needs revisit
def tsp(dist_m, circle=False):
    n = len(dist_m)
    N = sum([1 << i for i in range(n)])
    M = [[-1] * (N + 1) for _ in range(n)];
    Z = [[-1] * (N + 1) for _ in range(n)]
    def dist(ni, N):
        if N == 0:
            if circle:
                Z[ni][N] = dist_m[ni][Start]
            else:
                Z[ni][N] = 0
            return
        for nj in range(n):
            if 1 & (N >> nj):
                if Z[nj][N - (1 << nj)] == -1:
                    dist(nj, N - (1 << nj))
        c = [(nj, dist_m[ni][nj] + Z[nj][N - (1 << nj)]) for nj in range(n) if 1 & (N >> nj)]
        nmin, min_cost = min(c, key=lambda x: x[1])
        M[ni][N] = nmin
        Z[ni][N] = min_cost
    ni = 0
    mdist = int(1e20)
    for bit in range(n):
        Start = bit
        dist(bit, N - (1 << bit))
        d = Z[bit][N - (1 << bit)]
        if d < mdist:
            ni = bit
            mdist = d
    # path reconstruction make sure to adjust the path for the problems requirements
    path = [ni]
    N -= (1<<ni)
    while N:
        ni = M[ni][N]
        path.append(ni)
        N -= (1<<ni)
    return mdist, path