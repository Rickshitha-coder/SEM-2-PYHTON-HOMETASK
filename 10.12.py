'''Vehicle – example hybrid inheritance
1. Vehicle (Base Class): Represents a general vehicle with basic attributes like 
make, model, and year.
2. Car (Derived from Vehicle): Represents cars, which have additional 
features like the number of doors and trunk capacity.
3. Truck (Derived from Vehicle): Represents trucks, which have attributes 
like cargo capacity and number of axles.
4. PickupTruck (Derived from both Car and Truck): A specific type of vehicle 
that combines features of both cars (passenger-friendly) and trucks (cargofriendly). Method – display all the feature'''
class Vehicle:
 def __init__(self,make,model,year):
     self.make=make
     self.model=model
     self.year=year
 def displayVehicle(self):
     print(f"Make:{self.make}\nModel:{self.model}\nYear:{self.year}")
class Car(Vehicle):
 def __init__(self,make,model,year,n_doors,trunk_cap):
    Vehicle.__init__(self,make,model,year)
    self.n_doors=n_doors
    self.trunk_cap=trunk_cap
 def displayCar(self):
    print(f"Number of doors in car:{self.n_doors}\nTrunk Capacity:{self.trunk_cap}")
class Truck(Vehicle):
 def __init__(self,make,model,year,cargo_cap,n_axles):
    super().__init__(make,model,year)
    self.cargo_cap=cargo_cap
    self.n_axles=n_axles
 def displayTruck(self):
    print(f"Cargo Capacity:{self.cargo_cap}\nNumber of Axles:{self.n_axles}")
class PickupTruck(Car,Truck):
 def __init__(self,make,model,year,n_doors,truck_cap,cargo_cap,n_axles):
    Car.__init__(self,make,model,year,n_doors,truck_cap)
    Truck.__init__(self,make,model,year,cargo_cap,n_axles)
 def displayfeatures(self):
    self.displayVehicle()
    self.displayCar()
    self.displayTruck()
vec=PickupTruck("Ford","F",2000,6,2000,9000,2)
vec.displayfeatures()
'''Inventory Management System [Hierarchical inheritance]
1. Product (Base Class): Defines common attributes like product ID, name, 
and price. Method to display all the info.
2. Electronics (Derived Class): Inherits from Product and adds attributes 
like warranty period and brand. Method to display all the info.
3. Clothing (Derived Class): Inherits from Product and adds attributes like 
size and material. Method to display all the info'''

class Product:
 def __init__(self,Id,name,price):
     self.Id=Id
     self.name=name
     self.price=price
 def displayProduct(self):
     print("Product ID:",self.Id)
     print("Product name:",self.name)
     print("Product price:",self.price)
class Electronics(Product):
 def __init__(self,Id,name,price,warranty,brand):
     Product.__init__(self,Id,name,price)
     self.warranty=warranty
     self.brand=brand
 def displayElectronics(self):
     print("Warranty:",self.warranty)
     print("Brand:",self.brand)
class Clothing(Product):
 def __init__(self,Id,name,price,size,material):
     Product.__init__(self,Id,name,price)
     self.size=size
     self.material=material
 def displayClothing(self):
     print("Material:",self.material)
     print("Size:",self.size)
phone=Electronics(123456,"Moto","25,000.","1-year","motorola")
shirt=Clothing(98765,"Chudithar","600rs.","L","Cotton")
phone.displayProduct()
phone.displayElectronics()
shirt.displayProduct()
shirt.displayClothing()




