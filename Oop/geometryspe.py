from geometry import Point
from dataclasses import dataclass

@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class WeightedPoint(Point):

    weight: float = 1.0

@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class ColoredPoint(Point):

    color: str = "#000000"

@dataclass(slots=False, order=True, kw_only=True, unsafe_hash=True)
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    
    pass