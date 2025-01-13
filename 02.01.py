from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @absractmethod
    def calculate_pay(self):
        pass
class SalariedEmployee:
    def __init__(self,name,annual_sal):
        self.name=name
        self.annual_sal=annual_sal
    def calculate_pay(self):
         return self.annual_sal/12
class HourlyEmployee:
    def __init__(self,name,hoursworked,hourlyrate):
        self.name=name
        self.hoursworked=hoursworked
        self.hourlyrate=hourlyrate
    def calculate_pay(self):
        return self.hoursworked*self.hourlyrate
n=input("Enter the name: ")
a=float(input("Enter the annual amount: "))
s=SalariedEmployee(n,a)
print(f"Salaried Employee ({n}) Pay: ${s.calculate_pay():.2f}")
n=input("Enter the name: ")
h_worked=float(input("Enter how many hours worked: "))
h_rate=float(input("Enter the hourly rate: "))
hour=HourlyEmployee(n,h_worked,h_rate)
print(f"Hourly Employee ({n}) Pay: ${hour.calculate_pay():.2f}")
