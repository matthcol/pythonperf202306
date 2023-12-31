import pytest
import geometry as geo


@pytest.mark.parametrize(
    ["p1","p2"], 
    [
        (geo.Point(), geo.Point()),
        (geo.Point(x=3.5), geo.Point(x=3.5)),
        (geo.Point(y=5.25), geo.Point(y=5.25)),
        (geo.Point(x=3.5, y=5.25), geo.Point(x=3.5, y=5.25)),
        (geo.Point("A",3.5,5.25), geo.Point("A",3.5,5.25)),
    ],
    ids=[
        "default point",
        "x explicit",
        "y explicit",
        "x,y explicit",
        "name,x,y explicit",
        ]
)
def test_eq_ok(p1,p2):
    assert p1 == p2
    assert not (p1 != p2)

@pytest.mark.parametrize(
    ["p1","p2"], 
    [
        (geo.Point(), geo.Point("A")),
        (geo.Point("A"), geo.Point()),
        (geo.Point("A",3.5,5.25), geo.Point("B",3.5,5.25)),
        (geo.Point("A",3.5,5.25), geo.Point("A",4.5,5.25)),
        (geo.Point("A",3.5,5.25), geo.Point("A",3.5,6.25)),
        (geo.Point("A",3.5,5.25), geo.Point("B",4.5,6.25)),
        (geo.Point("A",3.5,5.25), 12),
        (12, geo.Point("A",3.5,5.25)),
        (geo.Point("A",3.5,5.25), "B"),
        ("B", geo.Point("A",3.5,5.25)),
    ],
    ids=[
        "name None vs str",
        "name str vs None",
        "name different",
        "x different",
        "y different",
        "name,x,y different",
        "Point vs int",
        "int vs Point",
        "Point vs str",
        "str vs Point",


    ])
def test_eq_ko(p1,p2):
    assert not(p1 == p2)
    assert p1 != p2

def test_eq_same():
    p = geo.Point("A", 1.25, 3.5)
    assert p == p
    assert not(p != p)

def test_eq_inContainerList():
    p = geo.Point("A", 1.25, 3.5)
    container = [
        geo.Point("C", 1.25, 3.5),
        geo.Point("A", 1.25, 3.5),
        geo.Point("B", 1.25, 3.5)
    ]
    assert p in container

def test_eq_inContainerSet():
    p = geo.Point("A", 1.25, 3.5)
    container = {
        geo.Point("C", 1.25, 3.5),
        geo.Point("A", 1.25, 3.5),
        geo.Point("B", 1.25, 3.5)
    }
    assert p in container

def test_eq_inContainerDict():
    p = geo.Point("A", 1.25, 3.5)
    container = {
        geo.Point("C", 1.25, 3.5): "Good",
        geo.Point("A", 1.25, 3.5): "Average",
        geo.Point("B", 1.25, 3.5): "Bad"
    }
    assert p in container

