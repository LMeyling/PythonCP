# Status: checked
# returns signed distance between p and line from a to b

from point import *

def lineDist(a,b,p):
    return (b-a).cross(p-a)/(b-a).dist()
