import pytest
import geometry as geo

@pytest.fixture
def pointA():
    return geo.Point("A", 2.5, 3.25)

@pytest.fixture
def pointB():
    return geo.Point("B", 1.5, 1.75)

@pytest.fixture
def tupleB():
    return (1.5, 1.75)

def test_add_point(pointA, pointB):
    res = pointA + pointB 
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_tuple(pointA, tupleB):
    res = pointA + tupleB
    assert res.x == 4.0
    assert res.y == 5.0

def test_radd_tuple(pointA, tupleB):
    res = tupleB + pointA
    assert res.x == 4.0
    assert res.y == 5.0

def test_iadd_point(pointA, pointB):
    pointA += pointB
    assert pointA.x == 4.0
    assert pointA.y == 5.0
    
def test_iadd_tuple(pointA, tupleB):
    pointA += tupleB
    assert pointA.x == 4.0
    assert pointA.y == 5.0
