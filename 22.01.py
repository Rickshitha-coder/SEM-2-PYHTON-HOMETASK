'''Scenario: Employee Management System
A company has different types of employees: Full-Time Employees and Part-Time Employees. Each 
employee has common details like name, employee ID, and department. However, the salary 
calculation differs for each type:
• Full-Time Employee: Salary is calculated as a fixed monthly salary.
• Part-Time Employee: Salary is calculated based on hourly wages and hours worked.
You are tasked with designing an object-oriented solution using an abstract class to represent the 
common behavior and structure of all employees while allowing specific implementations for each 
type.
Hint:-
1. Create an abstract class Employee with the following:
o Fields: name, employee_id, department.
o An abstract method calculate_salary().
o A concrete method display_details() to display employee details.
2. Create two subclasses:
o FullTimeEmployee: Implements calculate_salary() for a fixed monthly salary.
o PartTimeEmployee: Implements calculate_salary() based on hourly wage and hours 
worked.
3. Write a program to create objects of both types, calculate their salaries, and display their 
details.'''

from abc import ABC, abstractmethod

class Employee(ABC):   #create a abstractmethod
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, monthly_salary):
        super().__init__(name, employee_id, department)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, hourly_wage, hours_worked):
        super().__init__(name, employee_id, department)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

# Create objects of both types
full_time_employee = FullTimeEmployee("Rickshi", "AI001", "Marketing", 9000)
part_time_employee = PartTimeEmployee("Kannama", "CS001", "Sales", 60, 100)

# Calculate salaries and display details
print("Full-time Employee:")
full_time_employee.display_details()
print(f"Salary: ${full_time_employee.calculate_salary():.2f}")
print()
print("Part-time Employee:")
part_time_employee.display_details()
print(f"Salary: ${part_time_employee.calculate_salary():.2f}")


