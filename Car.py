'''Description:Create a Car class that models a car. The class should have the following attributes:
make: The make of the car (e.g., Toyota, Ford)
model: The model of the car (e.g., Camry, Mustang)
year: The year the car was manufactured
fuel_level: The current fuel level of the car (initially set to 100)
The class should have the following methods:
drive(distance): Decreases the fuel level based on the distance driven (assume 1 unit of distance decreases fuel by 1 unit). If there is not enough fuel to cover the distance, print a message indicating insufficient fuel and do not decrease the fuel level.
refuel(amount): Increases the fuel level by the given amount, but the maximum fuel level cannot exceed 100.
get_fuel_level(): Returns the current fuel level.'''  

class Car:
  def __init__(self, make, model, year, fuel_level):
    self.__make = make
    self.__model = model
    self.__year = year
    self.__fuel_level = fuel_level

  def drive(self, distance):
    if self.__fuel_level < distance:
      print("The fuel is insufficient to cover the distance")
    else:
      self.__fuel_level -= distance

  def refuel(self, amount):
    if self.__fuel_level + amount > 100:
      print(f"Here is your return money: {amount - (100 - self.__fuel_level)}")
      self.__fuel_level = 100
    else:
      self.__fuel_level += amount

  def get_fuel_level(self):
    return self.__fuel_level

car1 = Car("Honda", "civic", 2020, 80)
car1.drive(20)
car1.refuel(500)
car1.drive(20)
print(f"Your current fuel level is {car1.get_fuel_level()}")