#1. a Python program that demonstrates single inheritance. Create a parent class called Person with an attribute name and a method show_name to display the name. Create a child class called Student that inherits from the Person class and adds a new attribute student_id with a method 
#show_student_id to display the student ID. Create an object of the Student class, and use it to display both the name and student ID.

class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"The Person Nmae:{self.name}")
class Student(Person):
    def __init__(self,name,stu_id):
        super().__init__(name)
        self.stu_id=stu_id
    def show(self):
        print(f"The Student ID is:{self.stu_id}")
stu=Student("Rickshi",37)
stu.display()
stu.show()



#2.Write a Python program to demonstrate single inheritance. Create a parent class Employee with attributes name and salary, and a method display_details to show the employee's details. Create a 
#child class Manager that inherits from Employee and adds an attribute department, along with a method display_department to show the department name. Create an object of the Manager class to 
#display all details
class Employee:  #parent class
    def getEmployeeInfo(self):
        self.name=input("Enter the name")
        self.salary=input("Enter the salary:")
    def displayEmployeeInfo(self):
        print("Name=",self.name,"\n Salary=",self.salary)
class Manager(Employee):   #child class
    def getDetails(self):
        self.getEmployeeInfo()
        self.dep=input("Enter the department")
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary",self.dep)
emp=Manager()
emp.getDetails()
emp.displayInfo()

            
