import pytest
import geometry as geo

@pytest.fixture
def pointA():
    return geo.Point("A", 3.5, 4.75)

def test_getterName(pointA):
    assert "A" == pointA.name

# @pytest.mark.xfail(raises=AttributeError)
def test_setterName(pointA):
    # AttributeError: property 'name' of 'Point' object has no setter
    pointA.name = "B"
    assert "B" == pointA.name

def test_deleteName(pointA):
    # AttributeError: property 'name' of 'Point' object has no deleter
    with pytest.raises(AttributeError, match=r"object has no deleter$"):
        del pointA.name

# #Alt. deleter set name to None
# def test_deleteName(pointA):
#     del pointA.name
#     assert pointA.name is None