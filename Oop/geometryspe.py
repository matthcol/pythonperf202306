from geometry import Point
from dataclasses import dataclass

@dataclass(slots=True, order=True, kw_only=True, unsafe_hash=True)
class WeightedPoint(Point):

    weight: float = 1.0

@dataclass(slots=True, order=True, kw_only=True, unsafe_hash=True)
class ColoredPoint(Point):

    color: str = "#000000"
