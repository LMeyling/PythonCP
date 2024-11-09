#if i->j dist[i][j] = value
#if not i ->j dist[i][j] = INF
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
