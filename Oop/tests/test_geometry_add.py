import pytest
import geometry as geo

@pytest.fixture
def pointA():
    return geo.Point("A", 2.5, 3.25)

@pytest.fixture
def pointB():
    return geo.Point("B", 1.5, 1.75)

@pytest.fixture
def tupleXY():
    return (1.5, 1.75)

@pytest.fixture
def tupleNXY():
    return ("A",1.5, 1.75)

@pytest.fixture
def listXY():
    return [1.5, 1.75]

@pytest.fixture
def listNXY():
    return ["A",1.5, 1.75]

@pytest.fixture
def dictX():
    return {"x":1.5}

@pytest.fixture
def dictY():
    return {"y":1.75}

@pytest.fixture
def dictXY():
    return {"x":1.5, "y":1.75}

@pytest.fixture
def dictNXY():
    return {"name": "A","x":1.5, "y":1.75}

def test_add_point(pointA, pointB):
    res = pointA + pointB 
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_tupleXY(pointA, tupleXY):
    res = pointA + tupleXY
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_tupleNXY(pointA, tupleNXY):
    res = pointA + tupleNXY
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_listXY(pointA, listXY):
    res = pointA + listXY
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_listNXY(pointA, listNXY):
    res = pointA + listNXY
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_dictX(pointA, dictX):
    res = pointA + dictX
    assert res.x == 4.0
    assert res.y == 3.25 # pointA.y

def test_add_dictY(pointA, dictY):
    res = pointA + dictY
    assert res.x == 2.5 # pointA.x
    assert res.y == 5

def test_add_dictXY(pointA, dictXY):
    res = pointA + dictXY
    assert res.x == 4.0
    assert res.y == 5.0

def test_add_dictNXY(pointA, dictNXY):
    res = pointA + dictNXY
    assert res.x == 4.0
    assert res.y == 5.0


@pytest.mark.parametrize(
        "scalar,expX,expY",
        [
            (2, 4.5, 5.25),
            (2.25, 4.75, 5.5),
            (True, 3.5, 4.25), 
            (False, 2.5, 3.25),
        ],
        ids=["int","float",
             "bool true","bool false",
        ]
)
def test_add_scalar(pointA, scalar, expX, expY):
    res = pointA + scalar
    assert res.x == expX
    assert res.y == expY


@pytest.mark.xfail(raises=TypeError)
def test_radd_tuple(pointA, tupleXY):
    res = tupleXY + pointA
    assert res.x == 4.0
    assert res.y == 5.0

def test_iadd_point(pointA, pointB):
    pointA += pointB
    assert pointA.x == 4.0
    assert pointA.y == 5.0
    
def test_iadd_tupleXY(pointA, tupleXY):
    pointA += tupleXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0

def test_iadd_tupleNXY(pointA, tupleNXY):
    pointA += tupleNXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0

def test_iadd_listXY(pointA, listXY):
    pointA += listXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0

def test_iadd_listNXY(pointA, listNXY):
    pointA += listNXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0

def test_iadd_dictX(pointA, dictX):
    pointA += dictX
    assert pointA.x == 4.0
    assert pointA.y == 3.25 # unchanged

def test_iadd_dictY(pointA, dictY):
    pointA += dictY
    assert pointA.x == 2.5 # unchanged
    assert pointA.y == 5

def test_iadd_dictXY(pointA, dictXY):
    pointA += dictXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0

def test_add_dictNXY(pointA, dictNXY):
    pointA += dictNXY
    assert pointA.x == 4.0
    assert pointA.y == 5.0


@pytest.mark.parametrize(
        "scalar,expX,expY",
        [
            (2, 4.5, 5.25),
            (2.25, 4.75, 5.5),
            (True, 3.5, 4.25), 
            (False, 2.5, 3.25),
        ],
        ids=["int","float",
             "bool true","bool false",
        ]
)
def test_iadd_scalar(pointA, scalar, expX, expY):
    pointA += scalar
    assert pointA.x == expX
    assert pointA.y == expY

notAddableDataList = [
    "A", # cannot add str (for now)
    (3,4,5,6), # cannot add list with too uch element
    [3,4,5,6], # cannot add list with too uch element
    {"key":1} # cannot add dict without x or y key
] 

@pytest.mark.parametrize(
    "other", 
    notAddableDataList
)
def test_add_ko_notAddable(pointA, other):
    with pytest.raises(TypeError):
        pointA + other

@pytest.mark.parametrize(
    "other", 
    notAddableDataList
)
def test_iadd_ko_notAddable(pointA, other):
    with pytest.raises(TypeError):
        pointA += other
