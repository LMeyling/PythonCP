class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def cross(self,P):
        # pos = left, 0 = straight, neg = right
        return self.x*P.y - P.x * self.y

    def subtract(self, P):

        return Point(self.x-P.x, self.y - P.y)

    def same(self, P):
        return self.x == P.x and self.y == P.y

    def abst(self):
        return (self.x**2+self.y**2)**0.5

class Line:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2

    def location(self, P):
        # 0 = on line, > 0 = left, < 0 = right
        return P.subtract(self.P1).cross(P.subtract(self.P2))

    def closes_point(self, P):

        u = self.P2.subtract(self.P1).abst()

        return abs(self.P1.subtract(P).cross(self.P2.subtract(P)) / u)

class Segment:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2

    def intersect(self, S):
        V = self.P2.subtract(self.P1)
        C1 = V.cross(S.P1)
        C2 = V.cross(S.P2)

        if self.P1.same(S.P1) or self.P2.same(S.P1) or self.P1.same(S.P2) or self.P2.same(S.P2):
            return True

        if C1 == C2 == 0:
            LIST = [(self.P1.x,self.P1.y,0),(self.P2.x,self.P2.y,1),(S.P1.x,S.P1.y,2),(S.P2.x,S.P2.y,3)]
            LIST.sort()
            if (LIST[0][2] + LIST[1][2] == 1) or  (LIST[2][2] + LIST[3][2] == 1):
                return False
            return True
        V1 = S.P2.subtract(S.P1)
        C3 = V1.cross(self.P1)
        C4 = V1.cross(self.P2)

        if C1 * C2 <= 0 and C3 * C4 <= 0:
            return True

        return False


import itertools
class ConvexHull():
    def __init__(self):
        self.points = []
    def add_point(self,x,y):
        self.points.append([x,y])
        
    def ccw(self, A, B, C):
        return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    
    def get_hull_points(self):
        
        if len(self.points) <= 1:
            return self.points

        hull = []
        self.points.sort()
        points = self.points
        for i in itertools.chain(range(len(points)), reversed(range(len(points)-1))):
            while len(hull) >= 2 and self.ccw(hull[-2], hull[-1], points[i]) < 0:
                hull.pop()
            hull.append(points[i])
        hull.pop()

        for i in range(1, (len(hull)+1)//2):
            if hull[i] != hull[-1]:
                break
            hull.pop()
        return hull
