# Status: checked
from onSegment import onSegment
from point import *

#If a unique intersection point between the line segments going from s1 to e1 and from s2 to e2 exists then it is returned.
#If no intersection point exists an empty set is returned.
#If infinitely many exist a set with 2 elements is returned, containing the endpoints of the common line segment.

def segInter(a,b,c,d):
    oa = c.crossp(d,a); ob = c.crossp(d,b)
    oc = a.crossp(b,c); od = a.crossp(b,d)
    if sgn(oa)*sgn(ob) < 0 and sgn(oc) * sgn(od) < 0:
        return {(a * ob - b * oa) / (ob - oa)}
    s = set()
    if onSegment(c,d,a): s.add(a)
    if onSegment(c,d,b): s.add(b)
    if onSegment(a,b,c): s.add(c)
    if onSegment(a,b,d): s.add(d)
    return s

