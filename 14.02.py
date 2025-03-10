'''Date:14.02.2025
.Imagine you are building an Employee Management System where you need to store employee 
details and calculate their yearly salary.
• The __init__ method initializes attributes: name, emp_id, and salary.
• display_info() prints employee details.
• calculate_yearly_salary() computes the yearly salary'''
class Employee:
    def __init__(self,name,emp_id,month_salary):
        self.name=name
        self.emp_id=emp_id
        self.month_salary=month_salary
    def display(self):
        print("Employee Name:",self.name)
        print(f"Employee ID:{self.emp_id}")
        print("Month Salary:",self.month_salary)
        
    def calculate_yearly(self):
        self_yearly_salary=self.month_salary*12
        print("Yearly Salary:",self_yearly_salary)
        
e=Employee("Rickshi",108,1000)
e.display()
e.calculate_yearly()

'''2. You are developing an Employee Management System for a company where there are two types of 
employees:
• Full-Time Employees who receive a fixed monthly salary.
• Part-Time Employees who are paid based on the hours they work.
Since all employees share common attributes (name, employee ID, and department), you decide to 
use inheritance to create specialized classes for different types of employees.
Parent Class (Employee)
• Common attributes: name, emp_id, department.
• display_info() method prints basic employee details.
Child Class (FullTimeEmployee)
• Inherits from Employee and adds a salary attribute.
• calculate_annual_salary() calculates the yearly salary.
• display_full_time_info() shows all details for a full-time employee.
Child Class (PartTimeEmployee)
• Inherits from Employee and adds hourly_rate and hours_worked.
• calculate_salary() computes the total earnings.
• display_part_time_info() shows all details for a part-time employee'''
class Employee:
    def __init__(self):
        self.name=input("Enter the name:")
        self.emp_id=int(input("Enter the employee id:"))
        self.department=input("Enter the department:")
    def display(self):
        print("Name of Employee:",self.name)
        print("Employess ID:",self.emp_id)
        print("Department:",self.department)
class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.month_salary=int(input("Enter the Monthly salary:"))
    def calculate_salary(self):
        self.yearly_salary=self.month_salary*12
    def display_full(self):
        self.display()
        self.calculate_salary()
        print("Annuval salary:",self.yearly_salary)
        print("Monthly salary:",self.month_salary)
class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_rated=int(input("Enter the per hour rate:"))
        self.hour_worked=int(input("Enter the Hours worked:"))
    def calculate(self):
        self.salary=self.hourly_rated*self.hour_worked
    def display_part(self):
        self.display()
        self.calculate()
        print("Per Hour amount:",self.hourly_rated)
        print("Hours Worked:",self.hour_worked)
        print("Salary for part time:",self.salary)
print("FULL TIME EMPLOYEE")
f=FullTimeEmployee()
f.display_full()
print("PART TIME EMPLOYEE")
p=PartTimeEmployee()
p.display_part()






















