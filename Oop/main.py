from geometry import Point
from geometryspe import WeightedPoint

def scenario1():
    p1 = Point("A", 3, 4)
    p2 = Point()
    p3 = Point(x=3, y=4)
    for p in p1, p2, p3:
        print("str:", p)
        print("repr:", repr(p))

def scenario3_classmethods():
    p1 = Point.of(3,4)
    p2 = Point.of(6,7, "B")
    wp3 = WeightedPoint.of(3, 6, "C")
    wp4 = WeightedPoint.fromCoords(3, 6, "D")
    p5 = Point.fromCoords(6,7, "E")
    for p in p1,p2,wp3, wp4, p5:
        print(p, type(p))

if __name__ == '__main__':
    scenario1()
    scenario3_classmethods()