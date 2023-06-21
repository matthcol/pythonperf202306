from  functools import total_ordering

# NB: engagement du concepteur de la classe
# à avoir un == et < compatible
@total_ordering
class Point:

    # freeze attribute list (dynamic add impossible)
    __slots__ = ["_name","x","y"]
    
    # for pattern matching by position
    __match_args__ = ("name","x","y")
    
    def __init__(self, name=None, x=0.0, y=0.0):
        self._name = name
        self.x = x
        self.y = y

    @property
    def name(self):
        """name of the point (optional)"""
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    # NB: deleter forbidden

    # NB: __repr__ overrides both __str__ and __repr__ 
    # if __str__ is not overriden
    def __repr__(self):
        return "Point<name={},x={},y={}>".format(
            self.name,
            self.x,
            self.y
        )
    
    def __str__(self):
        return "{}({},{})".format(
            "?" if self.name is None else self.name,
            self.x,
            self.y
        )
    
    # override ==, !=, hash
    def __eq__(self, other):
        if self is other:
            return True 
        if isinstance(other, Point):
            return (self.name, self.x, self.y) == \
                (other.name, other.x, other.y)
        return NotImplemented
    
    # NB: p1 == p2 => hash(p1) == hash(p2)
    def __hash__(self):
        return hash((self.name, self.x, self.y))

    # total_ordering: <, <=, >, >=
    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y, self.name) < \
                (other.x, other.y, other.name)
        return NotImplemented
    
    # override + (__add__/__radd__)
    def __add__(self, other):
        match other:
            case int(v) | float(v):
                return Point(x=self.x + v, y=self.y + v)
            case Point(x=x, y=y):
                return Point(x=self.x + x, y=self.y + y)
            case (x, y):
                return Point(x=self.x + x, y=self.y + y)
            case (str,x, y):
                return Point(x=self.x + x, y=self.y + y)
            case {"x":x, "y":y}:
                return Point(x=self.x + x, y=self.y + y)
            case {"x":x}:
                return Point(x=self.x + x, y=self.y)
            case {"y":y}:
                return Point(x=self.x, y=self.y + y)
            case _:
                return NotImplemented

    # override += (__iadd__)
    def __iadd__(self, other):
        match other:
            case int(v) | float(v):
                self.x += v
                self.y += v
            case Point(x=x, y=y):
                self.x += x
                self.y += y
            case (x, y):
                self.x += x
                self.y += y
            case (str,x, y):
                self.x += x
                self.y += y
            case {"x":x, "y":y}:
                self.x += x
                self.y += y
            case {"x":x}:
                self.x += x            
            case {"y":y}:
                self.y += y
            case _:
                return NotImplemented
        return self