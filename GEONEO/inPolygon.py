# Returns 1 if p lies within the polygon. Returns 2 if p lies on an edge
# care with floats

from point import *
from onSegment import *
from segDist import *

def inPolygon(p, a):
    cnt = 0; n = len(p)
    for i in range(n):
        q = p[(i+1)%n]
        if onSegment(p[i], q , a): return 2
        # or if segDist(p[i], q, a) <= eps: return 2
        cnt ^= ((a.y<p[i].y) - (a.y<q.y)) * a.crossp(p[i], q) > 0
    return cnt