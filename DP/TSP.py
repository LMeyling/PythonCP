M={}
N=frozenset(range(1,len(dist_m)))
def dist(ni,N):
    if not N:
        return dist_m[ni][0]
    c=[(nj,dist_m[ni][nj]+dist(nj,N.difference({nj}))) for nj in N]
    nmin,min_cost=min(c,key=lambda x:x[1])
    M[(ni,N)] = nmin
    return min_cost
min_dist = dist(0,N)
ni = 0
solution = [0]

while N:
    ni = memo[(ni, N)]
    solution.append(ni)
    N = N.difference({ni})
