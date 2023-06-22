from geometry import Point
from geometryspe import WeightedColoredPoint

def scenario1():
    p1 = Point(name="A", x=3, y=4)
    p2 = Point()
    p3 = Point(x=3, y=4)
    for p in p1, p2, p3:
        print("str:", p)
        print("repr:", repr(p))

def scenario2_weightedColoredPoint():
    wcpD = WeightedColoredPoint(name="D", x=2.5, y=3.25, weight=5.5, color="red")
    print(WeightedColoredPoint.__mro__)
    # res:  
            # (geometryspe.WeightedColoredPoint,
            # geometryspe.WeightedPoint,
            # geometryspe.ColoredPoint,
            # geometry.Point,
            # object)
    wcpD.dummy()
    return wcpD

if __name__ == '__main__':
    scenario1()
    wcpD = scenario2_weightedColoredPoint()