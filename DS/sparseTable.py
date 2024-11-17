class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        k = self.log[n] + 1
        self.st = [arr]
        for j in range(1, k):
            prev = self.st[-1]
            curr = [min(prev[i], prev[i + (1 << (j - 1))]) for i in range(n - (1 << j) + 1)]
            self.st.append(curr)

    def query(self, l, r):
        k = self.log[r - l]
        return min(self.st[k][l], self.st[k][r - (1 << k)])