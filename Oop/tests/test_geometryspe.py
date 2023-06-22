import geometryspe as geos
import pytest

@pytest.fixture
def weightedPointB():
    return geos.WeightedPoint(name="B", x=2.5, y=3.25, weight=5.5)

@pytest.fixture
def coloredPointC():
    return geos.ColoredPoint(name="C", x=2.5, y=3.25, color="red")

@pytest.fixture
def weigtedColoredPointD():
    return geos.WeightedColoredPoint(name="D", x=2.5, y=3.25, weight=5.5, color="red")

def test_init_weightedPoint(weightedPointB):
    assert "B" == weightedPointB.name
    assert 2.5 == weightedPointB.x
    assert 3.25 == weightedPointB.y
    assert 5.5 == weightedPointB.weight

def test_init_coloredPoint(coloredPointC):
    assert "C" == coloredPointC.name
    assert 2.5 == coloredPointC.x
    assert 3.25 == coloredPointC.y
    assert "red" == coloredPointC.color

def test_init_weightColoredPoint(weigtedColoredPointD):
    assert "D" == weigtedColoredPointD.name
    assert 2.5 == weigtedColoredPointD.x
    assert 3.25 == weigtedColoredPointD.y
    assert 5.5 == weigtedColoredPointD.weight
    assert "red" == weigtedColoredPointD.color
