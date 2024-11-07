# Status: checked
from point import *

# Returns the shortest distance between point p and the line segment from point s to e.
def segDist(s,e,p):
    if s==e: return (p-s).dist()
    d = (e-s).dist2(); t = min(d,max(0,(p-s).dot(e-s)))
    return ((p-s)*d-(e-s)*t).dist()/d