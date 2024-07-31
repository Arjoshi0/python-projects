class Animal:
  def __init__(self, name, sound):
    self.name = name
    self.sound = sound

  def make_sound(self):
    print(f"{self.sound}!")
    
class Dog(Animal):
  def __init__(self, name):
    super().__init__(name, "Woof")

  # def make_sound(self):
  #   print("Dog makes no sound")

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow")


dog1 = Dog("Labrador")
dog1.make_sound()

cat1 = Cat("Siamese")
cat1.make_sound()