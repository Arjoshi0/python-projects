"""
Problem 1: Shape Class with Inheritance
Description:
Create a base class Shape with the following attributes:

color: The color of the shape.
The class should have the following method:

describe(): Returns a string describing the shape's color.
Then, create two derived classes:

Circle:

Additional attribute: radius (the radius of the circle).
Additional methods: area() (returns the area of the circle), perimeter() (returns the circumference of the circle).

Rectangle:

Additional attributes: length (the length of the rectangle), width (the width of the rectangle).
Additional methods:
area(): Returns the area of the rectangle.
perimeter(): Returns the perimeter of the rectangle.
is_square(): Returns True if the rectangle is a square, False otherwise.

Triangle:

Additional attributes: base (the base of the triangle), height (the height of the triangle).
Additional methods:
area(): Returns the area of the triangle.
perimeter(side1, side2, side3): Returns the perimeter of the triangle given the lengths of its three sides.
"""
PI = 3.14 
class Shape:
  def __init__(self, name, color):
    self.color = color

  def describe(self):
    return f"The color of {self.name} is {self.color}"

class Circle(Shape):
  def __init__(self, color, radius):
    super().__init__("circle", color)
    self.radius = radius

  def area(self):
    return PI * (self.radius ** 2)

  def perimeter(self):
    return 2 * PI * self.radius

class Rectangle(Shape):
  def __init__(self, color, length, width):
    super().__init__("rectangle", color)
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * (self.length + self.width)

  def is_square(self):
    return self.length == self.width

class Triangle(Shape):
  def __init__(self, color, base, height):
    super().__init__("triangle", color)
    self.base = base
    self.height = height

  def area(self):
    return (self.base * self.height) / 2

  def perimeter(self, side1, side2, side3):
    return side1 + side2 + side3
    
tri1 = Triangle("red", 4, 5)
print(tri1.area())
print(tri1.perimeter(1, 2, 3))