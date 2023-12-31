import pytest
import geometry as geo

@pytest.mark.parametrize(
    ["p1","p2"],
    [
        (geo.Point("A",2.5,3.5), geo.Point("B",3.5,3.5)), 
        (geo.Point("A",2.5,3.5), geo.Point("B",2.5,4.5)),
        (geo.Point("A",2.5,3.5), geo.Point("B",2.5,3.5)),
    ],
    ids=[
        "x1 < x2",
        "x1 = x2, y1 < y2",
        "x1 = x2, y1 = y2, name1 < name2",
    ]
)
def test_lt_ok(p1: geo.Point, p2: geo.Point):
    assert p1 < p2
    assert not (p1 > p2)
    # total ordering
    assert p1 <= p2
    assert not (p1 >= p2)
    
@pytest.mark.parametrize(
    ["p1","p2"],
    [
        (geo.Point("A",2.5,3.5), geo.Point("B",1.5,3.5)), 
        (geo.Point("A",2.5,3.5), geo.Point("B",2.5,2.5)),
        (geo.Point("A",2.5,3.5), geo.Point("A",2.5,3.5)),
        (geo.Point("Z",2.5,3.5), geo.Point("A",2.5,3.5)),
    ],
    ids=[
        "x1 > x2",
        "x1 = x2, y1 > y2",
        "x1 = x2, y1 = y2, name1 = name2",
        "x1 = x2, y1 = y2, name1 > name2",
    ]
)
def test_lt_ko(p1: geo.Point, p2: geo.Point):
    assert not(p1 < p2)
    
