from bisect import bisect_left
from collections import defaultdict

class RangeCountQuery:
    def __init__(self, arr):
        self.depth = defaultdict(list)
        for i, e in enumerate(arr):
            self.depth[e].append(i)

    def count(self, l, r, x):
        """l <= k < r におけるa[k]=xの個数"""
        a = self.depth[x]
        s = bisect_left(a, l)
        t = bisect_left(a, r, s)
        return t - s
