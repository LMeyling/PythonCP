# Status: checked
# returns Intersection of two lines (s1->e1) and (s2->e2)
# if one Intersection 1, Point; if no Intersection 0, (0,0); if infinite -1, (0,0)

from point import *

def lineInter(s1,e1,s2,e2):
    d = (e1-s1).cross(e2-s2)
    if d == 0:
        return -(s1.crossp(e1,s2) == 0), Point(0,0)
    p = s2.crossp(e1,e2); q = s2.crossp(e2,s1)
    return 1, (s1 * p + e1 * q) / d