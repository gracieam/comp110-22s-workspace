""""""

from __future__ import annotations

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special method to represent object as a string."""
        return f"{self.x}, {self. y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float"""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    # def scale(self, factor: float) -> Point:
    #     """Scale a Point's attributes by factor."""
    #     # x: float = self.x * factor
    #     # y: float = self.y * factor
    #     # p: Point = Point(x, y)
    #     # return p
    #     return Point(self.x * factor, self.y * factor)

a: Point = Point(1.0, 2.0)
b: Point = a * (2.0)
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")