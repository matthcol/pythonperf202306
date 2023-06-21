from  functools import total_ordering

# NB: engagement du concepteur de la classe
# à avoir un == et < compatible
@total_ordering
class Point:
    
    def __init__(self, name=None, x=0.0, y=0.0):
        self.name = name
        self.x = x
        self.y = y

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

    # TODO: <, <=, >, >=
    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y, self.name) < \
                (other.x, other.y, other.name)
        return NotImplemented
    
    # TODO: + , +=