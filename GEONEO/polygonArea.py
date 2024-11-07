# Status: checked
# Returns twice the signed area of a polygon.
# Clockwise enumeration gives negative area

def polygonArea2(v):
    a = v[-1].cross(v[0])
    for i in range(0,len(v)-1): a+= v[i].cross(v[i+1])
    return a