# Status: checked
# find max independnet_set; literal magic, works up to n = 100

def maximum_independnet_set(
    n: int, edges: list[tuple[int, int]]
) -> tuple[int, list[int]]:
    adj = [0] * n
    for u, v in edges:
        if u > v:
            u, v = v, u
        adj[u] |= 1 << v
    dp = {0: 0}
    for i in range(n):
        nex = dict()
        for S, val in dp.items():
            if S >> i & 1 == 0:
                S1 = S | adj[i]
                nv = (val + (1 << n)) | (1 << i)
                if S1 in nex:
                    if nex[S1] < nv:
                        nex[S1] = nv
                else:
                    nex[S1] = nv
            S2 = S & ~(1 << i)
            if S2 in nex:
                if nex[S2] < val:
                    nex[S2] = val
            else:
                nex[S2] = val
        dp = nex

    size, bitset = divmod(dp[0], 1 << n)
    res = []
    for i in range(n):
        if bitset >> i & 1:
            res.append(i)
    return size, res