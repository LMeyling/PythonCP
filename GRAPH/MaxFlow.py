# Status: checked
from collections import deque

class MaxFlow():
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, fr, to, cap):
        m = len(self.pos)
        self.pos.append((fr, len(self.graph[fr])))
        fr_id = len(self.graph[fr])
        to_id = len(self.graph[to])
        if fr == to: to_id += 1
        self.graph[fr].append([to, to_id, cap])
        self.graph[to].append([fr, fr_id, 0])
        return m

    def get_edge(self, idx):
        to, rev, cap = self.graph[self.pos[idx][0]][self.pos[idx][1]]
        rev_to, rev_rev, rev_cap = self.graph[to][rev]
        return rev_to, to, cap + rev_cap, rev_cap

    def edges(self):
        m = len(self.pos)
        for i in range(m):
            yield self.get_edge(i)

    def dfs(self, s, t, up):
        stack = [t]
        while stack:
            v = stack.pop()
            if v == s:
                flow = up
                for v in stack:
                    to, rev, cap = self.graph[v][self.iter[v]]
                    flow = min(flow, self.graph[to][rev][2])
                for v in stack:
                    self.graph[v][self.iter[v]][2] += flow
                    to, rev, cap = self.graph[v][self.iter[v]]
                    self.graph[to][rev][2] -= flow
                return flow
            lv = self.level[v]
            for i in range(self.iter[v], len(self.graph[v])):
                to, rev, cap = self.graph[v][i]
                if lv > self.level[to] and self.graph[to][rev][2]:
                    self.iter[v] = i
                    stack.append(v)
                    stack.append(to)
                    break
            else:
                self.iter[v] = len(self.graph[v])
                self.level[v] = self.n
        return 0

    def max_flow(self, s, t):
        return self.max_flow_with_limit(s, t, 2**63 - 1)

    def max_flow_with_limit(self, s, t, limit):
        flow = 0
        while flow < limit:
            self.level = [-1] * self.n
            self.level[s] = 0
            queue = deque()
            queue.append(s)
            while queue:
                v = queue.popleft()
                for to, rev, cap in self.graph[v]:
                    if cap == 0 or self.level[to] >= 0: continue
                    self.level[to] = self.level[v] + 1
                    if to == t: break
                    queue.append(to)
            if self.level[t] == -1: break
            self.iter = [0] * self.n
            while flow < limit:
                f = self.dfs(s, t, limit - flow)
                if not f: break
                flow += f
        return flow
