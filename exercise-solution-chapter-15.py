from functools import singledispatch
from dataclasses import dataclass
import math

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

@dataclass
class Square:
    side: float

@singledispatch
def area(shape):
    return f"Invalid shape for {type(shape).__name__}"

@area.register
def _(shape: Circle):
    return math.pi * shape.radius ** 2

@area.register
def _(shape: Rectangle):
    return shape.width * shape.height

circle = Circle(radius=2)
rectangle = Rectangle(width=3, height=4)
square = Square(side=5)

res_area_circle = area(circle)
res_area_rectangle = area(rectangle)
res_area_square = area(square)

print(res_area_circle) # 12.566370614359172
print(res_area_rectangle) # 12
print(res_area_square) # Invalid shape for Square
