from  functools import total_ordering
from dataclasses import dataclass

# See also: pydantic (external dependency better than @dataclass)

# default settings: init=True, match_args=True, eq=True, order=False, repr=True
@dataclass(slots=True, order=True, kw_only=True, unsafe_hash=True)
class Point:

    x: int|float = 0
    y: int|float = 0
    name: str|None = None

    def __delattr__(self,name):
        raise AttributeError(f"property '{name}' of 'Point' object has no deleter")
    
    # str different from repr (default)
    def __str__(self):
        return "{}({},{})".format(
            "?" if self.name is None else self.name,
            self.x,
            self.y
        )
    
    
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
    
    def dummy(self):
        print("Dummy as a point")