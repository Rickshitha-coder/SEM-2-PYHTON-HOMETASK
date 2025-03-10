'''Date:27.02.2025
You are developing a vehicle management system for a transportation company. The system 
should handle different types of vehicles, such as Cars and Bikes. Each vehicle has a method 
called fuelType() that specifies the type of fuel it uses. 
However, different vehicles use different fuels, so you need to 
implement method overriding to ensure each vehicle class 
provides its own fuel type. 
Task: 
• Create a base class Vehicle with a method fuelType() that 
returns "General Fuel". 
• Create two subclasses Car and Bike, both inheriting from 
Vehicle. 
• Override the fuelType() method in each subclass: 
• The Car class should return "Petrol or Diesel". 
• The Bike class should return "Petrol". 
• Create objects of Car and Bike and call their fuelType() 
methods to demonstrate method overriding.'''
class Vehicle:
    def fuelType(self):
        return "General Fuel"


class Car(Vehicle):
    def fuelType(self):
        return "Petrol or Diesel"


class Bike(Vehicle):
    def fuelType(self):
        return "Petrol"


car = Car()
bike = Bike()
print("Car Fuel Type:", car.fuelType())
print("Bike Fuel Type:", bike.fuelType())

