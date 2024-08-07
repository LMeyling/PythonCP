# Calculates latice points for Polygon of INTEGER POINTS a, b (inside Polygon, on Polygon)
# Picks Theorem: Area = a + b/2 - 1

from math import gcd
from polygonArea import *

def latticePoints(p):
    ar = polygonArea2(p)
    n = len(p)
    on = 0
    for i in range(n):
        q = p[i]-p[i-1]
        on += gcd(abs(q.x),abs(q.y))
    return (abs(ar) + 2 - on) // 2, on