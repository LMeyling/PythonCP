# Gives Convex Hull, if strict = False, points on edges are allowed
# Warning strict = False is not 100% tested
# TLE Warning n = 2e5 runs in ~1s

from point import *

def convexHull(p,strict=True):
    eps = 1e-10
    if strict:
        eps = 0
    if len(p) < 2: return p
    p.sort()
    h = [Point(0,0) for _ in range(len(p)+2)]
    s = 0
    t = 0
    for it in range(2):
        for P in p:
            while t >= s + 2 and h[t-2].crossp(h[t-1],P)+eps<=0:t-=1
            h[t] = P
            t+=1
        t-=1
        s=t
        p.reverse()
    return h[0:t-(t==2 and h[0] == h[1])]