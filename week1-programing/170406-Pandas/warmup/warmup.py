class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y

    def distance(self, other):
        return (abs(self.x - other.x)**2 + abs(self.y - other.y)**2)**0.5

class Triangle(Point):

    def __init__(self,p1,p2,p3):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def perimeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)

    def _sine(self, a, b):
        return (abs(a.y - b.y)) / a.distance(b)

    def is_line(self):
        return (self._sine(self.p1,self.p2) == self._sine(self.p2,self.p3))


if __name__ == '__main__':
    p1, p2, p3 = Point(9, 2), Point(5, 5), Point(2, 1)
    print ("distance:", p1.distance(p2))
    triangle = Triangle(p1, p2, p3)
    print ("perimeter of triangle:", triangle.perimeter())
    print (triangle.is_line())

# testing for is_line to be true
    x1, x2, x3 = Point(1,2),Point(5,10),Point(10,20)
    xtriangle = Triangle(x1,x2,x3)
    print (xtriangle.perimeter())
    print (xtriangle.is_line())
