# Status: checked
def kosaraju_scc(V, adj):
    gt = [[] for _ in range(V)]
    for u in range(V):
        for v in adj[u]:
            gt[v].append(u)
    vis, order = set(), []
    def dfs(u):
        vis.add(u)
        for v in adj[u]:
            if v not in vis:
                dfs(v)
        order.append(u)
    for u in range(V):
        if u not in vis:
            dfs(u)
    vis.clear()
    scc = []
    def dfs_rev(u):
        vis.add(u)
        scc[-1].append(u)
        for v in gt[u]:
            if v not in vis:
                dfs_rev(v)
    for u in reversed(order):
        if u not in vis:
            scc.append([])
            dfs_rev(u)
    return scc