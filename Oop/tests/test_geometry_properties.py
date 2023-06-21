import pytest
import geometry as geo

@pytest.fixture
def pointA():
    return geo.Point(name="A", x=3.5, y=4.75)

def test_getterName(pointA):
    assert "A" == pointA.name

# @pytest.mark.xfail(raises=AttributeError)
def test_setterName(pointA):
    # AttributeError: property 'name' of 'Point' object has no setter
    pointA.name = "B"
    assert "B" == pointA.name

# for deletter choose between the 3 following strategies

# 1 - accept del
@pytest.mark.xfail
def test_deleteName_ok(pointA):
    del pointA.name # ok
    # now point has no attribute name anymore
    with pytest.raises(AttributeError, match=r"object has no attribute 'name'"):
        pointA.name

# 2 - forbid del attribute
# # NB: forbid del can be obtain with frozen=True
# # or need override of __delattr__ | deleter method
@pytest.mark.xfail
def test_deleteName_forbidden(pointA):
    # AttributeError: property 'name' of 'Point' object has no deleter
    with pytest.raises(AttributeError, match=r"object has no deleter$"):
        del pointA.name

# 3 - override del to restore default value
# # deleter set name to default None
@pytest.mark.xfail
def test_deleteName_setDefault(pointA):
    del pointA.name
    assert pointA.name is None