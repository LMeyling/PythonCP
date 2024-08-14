# Lowest Common Ancestor Query; init O(nlogn), query O(1)

class LCA:
    def __init__(self, n, graph, root=0):
        # assert n >= 2
        self.n = n
        path = [-1] * (n - 1)
        nodein = [-1] * n
        par = [-1] * n
        curtime = -1
        todo = [root]
        while todo:
            v = todo.pop()
            path[curtime] = par[v]
            curtime += 1
            nodein[v] = curtime
            for u in graph[v]:
                if nodein[u] == -1:
                    par[u] = v
                    todo.append(u)

        a = [nodein[v] for v in path]
        m = len(a)
        log = m.bit_length() - 1
        self.data = [a] + [[] for i in range(log)]
        for i in range(log):
            pre = self.data[i]
            l = 1 << i
            self.data[i + 1] = [pre[j] if pre[j] < pre[j + l] else pre[j + l] for j in range(len(pre) - l)]

        self.path = path
        self.nodein = nodein

    def lca(self, u, v):
        if u == v:
            return u
        l, r = self.nodein[u], self.nodein[v]
        if l > r:
            l, r = r, l
        u = (r - l).bit_length() - 1
        return self.path[
            self.data[u][l] if self.data[u][l] < self.data[u][r - (1 << u)] else self.data[u][r - (1 << u)]]