'''Create a class called Account to store your total_amount
Create a function called deposit() to add money to the total_amount
Create a function called withdraw() to subtract money from the total
Create a function to display the remaining amount'''


class Account:
  def __init__(self, total_amount):
    # sanitize total_amount
    self.total_amount = total_amount

  def deposit(self, amount):
    # sanitize amount
    # self.total_amount = self.total_amount + amount 
    self.total_amount += amount

  def withdraw(self, amount):
    # sanitize amount
    if self.total_amount < amount:
      print(f"Your account is deficient. Total amount: {self.total_amount}")
    else:
      self.total_amount -= amount

  def remaining_balance(self):
    return self.total_amount

aarush = Account(50000)
aarush.withdraw(12000)
print(aarush.remaining_balance())

pukar = Account(50000)
pukar.deposit(2000)
pukar.withdraw(17000)
pukar.withdraw(60000)
print(pukar.remaining_balance())