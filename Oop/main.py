from geometry import Point

def scenario1():
    p1 = Point("A", 3, 4)
    p2 = Point()
    p3 = Point(x=3, y=4)
    for p in p1, p2, p3:
        print("str:", p)
        print("repr:", repr(p))

if __name__ == '__main__':
    scenario1()