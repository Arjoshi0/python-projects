"""
Problem 2: Employee Class with Inheritance
Description:
Create a base class Employee with the following attributes:

name: The name of the employee.
employee_id: The ID of the employee.
The class should have the following methods:

get_details(): Returns a string with the employee's name and ID.
Then, create three derived classes:

Manager:

    Additional attribute: department (the department the manager is responsible for).
Additional methods:
get_details(): Returns a string with the manager's name, ID, and department.

Developer:

Additional attribute: programming_language (the programming language the developer specializes in).
Additional methods:
get_details(): Returns a string with the developer's name, ID, and programming language.

Intern:

Additional attributes: school (the school the intern is attending), graduation_year (the expected year of graduation).
Additional methods:
get_details(): Returns a string with the intern's name, ID, school, and graduation year.
"""

class Employee:
  def __init__(self, name, employee_id):
    self.name = name
    self.employee_id = employee_id

  def get_details(self):
    return f"Name: {self.name} ID: {self.employee_id}"

class Manager(Employee):
  def __init__(self, name, employee_id, department):
    super().__init__(name, employee_id)
    self.department = department
  def get_details(self):
     return f"Name: {self.name} ID: {self.id} Department: {self.department}"

class Developer(Employee):
  def __init__(self, name, employee_id, programming_language):
    super().__init__(name, employee_id)
    self.programming_language = programming_language

  def get_details(self):
    return f"Name: {self.name} ID: {self.employee_id} PL: {self.programming_language}"

class Intern(Employee):
  def __init__(self, name, employee_id, school, graduation_year):
    super().__init__(name, employee_id)
    self.school = school
    self.graduation_year = graduation_year

  def get_details(self):
    return f"Name: {self.name} ID: {self.employee_id} School: {self.school} Graduation: {self.graduation_year}"

emp1 = Intern("Aarush", 361, "Ideal Model School", 2011)
print(emp1.get_details())