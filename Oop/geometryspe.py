from geometry import Point
from dataclasses import dataclass

class WeightedPoint(Point):

    def __init__(self, name=None, x=0.0, y=0.0, weight=1.0, **kwargs):
        super().__init__(name=name, x=x, y=y, **kwargs)
        self.weight = weight

    def dummy(self):
        print("Dummy as a weighted point")


class ColoredPoint(Point):

    def __init__(self, name=None, x=0.0, y=0.0, color= "#000000", **kwargs):
        super().__init__(name=name, x=x, y=y, **kwargs)
        self.color = color

    def dummy(self):
        print("Dummy as a colored point")


class WeightedColoredPoint(WeightedPoint, ColoredPoint):

    def __init__(self, name=None, x=0.0, y=0.0, weight=1.0, color= "#000000", **kwargs):
        # call all __init__ from super classes in MRO order 
        super().__init__(name=name, x=x, y=y, weight=weight, color=color, **kwargs)


    # override to call the parent version 
    # of our choice (ColoredPoint)
    # not the MRO one (from WeightedColored)
    def dummy(self):
        ColoredPoint.dummy(self)