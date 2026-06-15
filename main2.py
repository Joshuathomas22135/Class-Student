# Write a program to create a class with name Student and perform the following tasks - 
# Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name 
# Create an object of class Student Call the two functions to execute them

class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section

    def output(self):
        print(f"The student named {self.name} is in grade {self.grade} and in the section {self.section}.")


s = Student("Josh", 11, "B")
s.output()