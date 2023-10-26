class FenwickTree():
    def __init__(self, n):
        self.n = n
        self.data = [0] * n
 
    def build(self, arr):
        #assert len(arr) <= n
        for i, a in enumerate(arr):
            self.data[i] = a
        for i in range(1, self.n + 1):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i) - 1] += self.data[i - 1]
 
    def add(self, p, x):
        #assert 0 <= p < self.n
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p
 
    def sum(self, r):
        #assert 0 <= r <= self.n
        s = 0
        while r:
            s += self.data[r - 1]
            r -= r & -r
        return s
 
    def range_sum(self, l, r):
        #assert 0 <= l <= r <= self.n
        return self.sum(r) - self.sum(l)
