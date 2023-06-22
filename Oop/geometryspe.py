from geometry import Point
from dataclasses import dataclass

class WeightedPoint(Point):

    def __init__(self, name=None, x=0.0, y=0.0, weight=1.0):
        super().__init__(name=name, x=x, y=y)
        self.weight = weight

    def dummy(self):
        print("Dummy as a weighted point")


class ColoredPoint(Point):

    def __init__(self, name=None, x=0.0, y=0.0, color= "#000000"):
        super().__init__(name=name, x=x, y=y)
        self.color = color

    def dummy(self):
        print("Dummy as a colored point")

# @dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
# class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    
#     # override to call the parent version 
#     # of our choice (ColoredPoint)
#     # not the MRO one (from WeightedColored)
#     def dummy(self):
#         ColoredPoint.dummy(self)