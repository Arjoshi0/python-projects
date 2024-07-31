class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * (self.length + self.width)

  def is_square(self):
    return self.length == self.width

rect1 = Rectangle(7, 7)
print(f"The area of the rectangle is {rect1.area()}")
print(f"The perimeter of the rectangle is {rect1.perimeter()}")


print("The rectangle is a square." if rect1.is_square() else "The rectangle is not a square.")