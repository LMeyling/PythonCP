M={};Z={}
N=frozenset(range(1,len(dist_m)))
def dist(ni,N):
    if not N:
        Z[(ni,N)]=dist_m[ni][0]
        return
    for nj in N:
        if (nj,N.difference({nj})) not in Z:
            dist(nj,N.difference({nj}))
    c=[(nj,dist_m[ni][nj]+Z[(nj,N.difference({nj}))]) for nj in N]
    nmin,min_cost=min(c,key=lambda x:x[1])
    M[(ni,N)] = nmin
    Z[(ni,N)] = min_cost
min_dist = dist(0,N)
ni = 0
solution = [0]

while N:
    ni = M[(ni, N)]
    solution.append(ni)
    N = N.difference({ni})
print(solution)
