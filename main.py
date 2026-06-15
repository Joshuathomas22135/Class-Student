# Write a program to create a class with name Student and perform the following tasks - 
# Declare a variable grade Print a sentence inside the class 
# Create an object of class student and see the output

class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"The student {self.name} is in {self.grade} class")

student = Student("Josh", 11)
student.display()
