import itertools
class ConvexHull():
    def __init__(self):
        self.points = []
    def add_point(self,x,y):
        self.points.append([x,y])
        
    def ccw(self, A, B, C):
        return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    
    def get_hull_points(self,points_on_edges=False):
        
        if len(self.points) <= 1:
            return self.points

        hull = []
        self.points.sort()
        points = self.points
        for i in itertools.chain(range(len(points)), reversed(range(len(points)-1))):
            if points_on_edges:
                while len(hull) >= 2 and self.ccw(hull[-2], hull[-1], points[i]) < 0:
                    hull.pop()
            else:
                while len(hull) >= 2 and self.ccw(hull[-2], hull[-1], points[i]) <= 0:
                    hull.pop()
            hull.append(points[i])
        hull.pop()

        for i in range(1, (len(hull)+1)//2):
            if hull[i] != hull[-1]:
                break
            hull.pop()
        return hull
