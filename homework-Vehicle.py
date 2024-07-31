
# Problem 3: Vehicle Class with Inheritance
# Description:
# Create a base class Vehicle with the following attributes:

# make: The make of the vehicle (e.g., Toyota, Ford).
# model: The model of the vehicle (e.g., Camry, Mustang).
# year: The year the vehicle was manufactured.
# The class should have the following methods:

# get_info(): Returns a string with the vehicle's make, model, and year.
# Then, create three derived classes:

# Car:

# Additional attribute: fuel_level (initially set to 100).
# Additional methods:
# drive(distance): Decreases the fuel level based on the distance driven (assume 1 unit of distance decreases fuel by 1 unit). If there is not enough fuel to cover the distance, print a message indicating insufficient fuel and do not decrease the fuel level.
# refuel(amount): Increases the fuel level by the given amount, but the maximum fuel level cannot exceed 100.
# get_fuel_level(): Returns the current fuel level.


# ElectricCar:

# Additional attribute: battery_level (initially set to 100).
# Additional methods:
# drive(distance): Decreases the battery level based on the distance driven (assume 1 unit of distance decreases battery by 1 unit). If there is not enough battery to cover the distance, print a message indicating insufficient battery and do not decrease the battery level.
# recharge(amount): Increases the battery level by the given amount, but the maximum battery level cannot exceed 100.
# get_battery_level(): Returns the current battery level.

# Motorcycle:

# Additional attributes: fuel_level (initially set to 50).
# Additional methods:
# drive(distance): Decreases the fuel level based on the distance driven (assume 1 unit of distance decreases fuel by 0.5 units). If there is not enough fuel to cover the distance, print a message indicating insufficient fuel and do not decrease the fuel level.
# refuel(amount): Increases the fuel level by the given amount, but the maximum fuel level cannot exceed 50.
# get_fuel_level(): Returns the current fuel level.

class Vehicle:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def get_info(self):
    return f"Make: {self.make} Model: {self.model} Year: {self.year}"

class Car(Vehicle):
  def __init__(self, make, model, year)
  super().__init__(make, model, year)
  self.fuel_level = 100

  def drive(self):
    if self.fuel_level < distance:
      print("The fuel is insufficient to cover the distance")
    else:
      self.fuel_level -= distance

  def refuel(self, amount):
    if self.fuel_level + amount > 100:
      print(f"Here is your return money: {amount - (100 - self.fuel_level)}")
      self.fuel_level = 100
    else:
      self.fuel_level += amount

  def get_fuel_level(self):
    return self.fuel_level

class ElectricCar(Vehicle):
  
  def __init__(self, make, model, year,):
    super().__init__(make, model, year)
    self.battery_level = 100

  def drive(self):
    if self.battery_level < distance:
      print("The fuel is insufficient to cover the distance")
    else:
      self.battery_level -= distance

  def recharge(self, amount):
    if self.battery_level + amount > 100:
      print(f"Here is your return money: {amount - (100 - self.battery_level)}")
      self.battery_level = 100
    else:
      self.battery_level += amount

  def get_battery_level(self):
    return self.battery_level

class Motorcycle(Vehicle):
  def __init__(self, make, model, year)
  super().__init__(make, model, year)
  self.fuel_level = 50

  def drive(self):
    if self.fuel_level < distance:
      print("The fuel is insufficient to cover the distance")
    else:
      self.fuel_level -= distance

  def refuel(self, amount):
    if self.fuel_level + amount > 50:
      print(f"Here is your return money: {amount - (50 - self.fuel_level)}")
      self.fuel_level = 50
    else:
      self.fuel_level += amount

  def get_fuel_level(self):
    return self.fuel_level








