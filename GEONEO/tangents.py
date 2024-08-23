# finds external (or internal for negative r) tangets of two circles (c1,r1), (c2,r2)
# 0 tangents: one circle contains the other
# 1 if circles are tangent to each other (first point = second point)
# 2 each gives both tangent points (can be seen as line)
# for point circle set r2 to 0

def tangents(c1,r1,c2,r2):
    d = c2 - c1
    dr = r1 - r2; d2 = d.dist2(); h2 = d2 - dr * dr
    if d2 == 0 or h2 < 0: return []
    out = []
    for sign in [-1,1]:
        v = (d * dr + d.perp() * (h2**0.5) * sign) / d2
        out.append((c1 + v*r1, c2 + v*r2))
    if h2 == 0: out.pop()
    return out