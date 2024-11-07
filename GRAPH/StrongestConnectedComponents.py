# Status: needs revisit
#Takes numbers as nodes, scc stores components as array, store node in connections array

V = len(nodes)
g, gt = [[] for _ in range(V)], [[] for _ in range(V)]
for a in connections:
    for b in connections[a]:
        g[a].append(b)
        gt[b].append(a)

top, vis, scc = [], set(), []


def DFS(s, add):
    vis.add(s)
    a = gt if add else g
    for v in a[s]:
        if v not in vis: DFS(v, add)
    if add:
        top.append(s)
    else:
        scc[-1].append(stores[s])


for i in range(V):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: scc.append([]), DFS(i, False)
