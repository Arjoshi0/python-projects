'''Description:Create a Book class that models a book in a library. The class should have the following attributes:
title: The title of the book
author: The author of the book
year: The year the book was published
The class should have the following methods:
get_description(): Returns a string in the format "Title by Author, published in Year".
is_older_than(year): Returns True if the book was published before the given year, False otherwise.'''

class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def get_description(self):
    return f"{self.title} by {self.author}, published in {self.year}"

  def is_older_than(self, current_year = 2024):
    return self.year < current_year

book1 = Book("Atomic Habits", "James Clear", 2018)
print(book1.get_description())
print("The book is older" if book1.is_older_than(2014) else "The book is not older")