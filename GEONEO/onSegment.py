# Returns true if p lies on the line segment from s to e.
def onSegment(s,e,p):
    return p.crossp(s,e) == 0 and (s-p).dot(e-p) <= 0
