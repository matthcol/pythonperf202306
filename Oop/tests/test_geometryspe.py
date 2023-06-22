import geometryspe as geos
import pytest

@pytest.fixture
def weightedPointB():
    return geos.WeightedPoint(name="B", x=2.5, y=3.25, weight=5.5)

@pytest.fixture
def coloredPointC():
    return geos.ColoredPoint(name="C", x=2.5, y=3.25, color="red")

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
