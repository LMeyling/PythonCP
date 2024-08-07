from math import atan2, cos, sin
from functools import total_ordering
def sgn(x):
    return (x > 0) - (x < 0)
@total_ordering
class Point:
    def __init__(self, x=0, y=0):
        self.x = x;self.y = y
    def __lt__(self, other):return (self.x, self.y) < (other.x, other.y)
    def __eq__(self, other):return (self.x, self.y) == (other.x, other.y)
    def __add__(self, other):return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, d):return Point(self.x * d, self.y * d)
    def __truediv__(self, d):return Point(self.x / d, self.y / d)
    def dot(self, other):return self.x * other.x + self.y * other.y
    def cross(self, other):return self.x * other.y - self.y * other.x
    def crossp(self, a, b):return (a - self).cross(b - self)
    def dist2(self):return self.x * self.x + self.y * self.y
    def dist(self):return self.dist2()**0.5
    def angle(self):return atan2(self.y, self.x)
    def unit(self):
        d = self.dist()
        return Point(self.x / d, self.y / d) if d != 0 else Point(0, 0)
    def perp(self):return Point(-self.y, self.x)
    def normal(self):return self.perp().unit()
    def rotate(self, a):
        return Point(self.x * cos(a) - self.y * sin(a),
                     self.x * sin(a) + self.y * cos(a))
    def __repr__(self):return f"({self.x}, {self.y})"
