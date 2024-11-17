def build_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))
    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev = sa[i - 1]
            curr = sa[i]
            tmp[curr] = tmp[prev] + (rank[prev] != rank[curr] or
                                     (rank[prev + k] if prev + k < n else -1) !=
                                     (rank[curr + k] if curr + k < n else -1))
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

def substring_search(s, sa, p):
    n, m = len(s), len(p)
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if s[sa[mid]:sa[mid] + m] < p:
            l = mid + 1
        else:
            r = mid
    if s[sa[l]:sa[l] + m] == p:
        return True
    return False
