from geometry import Point
from dataclasses import dataclass

@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class WeightedPoint(Point):

    weight: float = 1.0

    def dummy(self):
        print("Dummy as a weighted point")


@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class ColoredPoint(Point):

    color: str = "#000000"

    def dummy(self):
        print("Dummy as a colored point")

@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    
    # override to call the parent version 
    # of our choice (ColoredPoint)
    # not the MRO one (from WeightedColored)
    def dummy(self):
        ColoredPoint.dummy(self)