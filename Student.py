# Write a program of Student class to set data and show data
class Student:
  def __init__(self, id, name, gender, total_marks, percentage):
    self.id = id
    self.name = name
    self.gender = gender
    self.total_marks = total_marks
    self.percentage = percentage

  def setData(self, total_marks, percentage):
    self.total_marks = total_marks
    self.percentage = percentage

  def showData(self):
    print(f"ID: {self.id}")
    print(f"Name: {self.name}")
    print(f"Gender: {self.gender}")
    print(f"Total Marks: {self.total_marks}")
    print(f"Percentage: {self.percentage}")


student_1 = Student(3, "Aarush Raj Joshi", "Male", 700, 70)
student_2 = Student(11, "Pukar Chhatkuli", "Male", 900, 90)
student_3 = Student(4, "Roshani Kumari", "Female", 800, 80)

student_3.showData()

student_3.setData(900, 90)

student_3.showData()
