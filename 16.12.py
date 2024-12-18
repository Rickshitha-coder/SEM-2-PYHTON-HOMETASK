'''1)1. User Login System: Write a User class with:
o Private attributes _username and _password.
o A setter method set_password to ensure the password:
▪ Is at least 8 characters long.
▪ Contains at least one number and one special character.
o A method check_password(input_password) to verify the password.'''

class User:
 def __init__(self,username,password):
     self.__username=username
     self.__password=password
 def get_username(self):
     return self.__username
 def get_password(self):
     return self.__password
 def set_username(self):
     self.__username=username
 def set_password(Self):
     self.__password=password
 def checkpassword(self):
     digit=False
     char=False
     if len(self.__password)<8:
         return False
     if any (i.isdigit() for i in self.__password): #acgshdn17w
         digit=True
     if any (not i.isalnum() for i in self.__password):
         char=True

     if digit and char:
         print("password is valid")
         return True
     else:
       
          return False
username=input("Enter the username")
password=input("Enter the password:")
u=User(username,password)
if u.checkpassword():
 print(f"Username:{u.get_username()}\nPassword:{u.get_password()}")
else:
 print("Invalid credentials")

'''2)2. Encapsulation with Validation: Create a Product class with:
o Private attributes _name, _price, and _stock.
o set_price method to ensure price is greater than 0.
o set_stock method to ensure stock is an integer and non-negative.
o A getter method get_stock to retrieve the current stock.'''
class Product:
 def __init__(self,name,price,stock):
     self.__name=name
     self.__price=price
     self.__stock=stock
 def get_name(self):
     return self.__name
 def get_price(self):
     return self.__price
 def get_stock(self):
     return self.__stock
 def set_details(self):
     self.__name=name
     self.__price=price
     self.__stock=stock
 def check_price_and_stock(self):
     price=False
     stock=False
     if self.__price>0:
         price=True
     if type(self.__stock)==int and self.__stock>0:
         stock=True
     if price and stock:
         print("Valid details")
         return True
     else:
         return False
name=input("Enter the name")
price=int(input("Enter the price"))
stock=int(input("Enter the stock available"))
p=Product(name,price,stock)
if p.check_price_and_stock():
 print(f"Name:{p.get_name()}\nPrice:{p.get_price()}\nStock:{p.get_stock()}")
else:
 print("No valid details")


'''3)Basic Getter and Setter: Create a Student class with the following private attributes:
o _name
o _age
o _marks
Implement getter and setter methods to:
o Set and retrieve the name.
o Ensure age is between 5 and 100; otherwise, raise a ValueError.
Ensure marks are between 0 and 100; otherwise, raise a ValueError.'''
class Student:
 def __init__(self,name,age,marks):
     self.__name=name
     self.__age=age
     self.__marks=marks
 def get_name(self):
     return self.__name
 def get_age(self):
     return self.__age
 def get_marks(self):
     return self.__marks
 def check_details(self):
     if not self.__age>5 and self.__age<100:
         raise ValueError("Age is invalid")
     if not self.__marks>0 and self.__marks<=100:
         raise ValueError("Marks are invalid")
try:
 name=input("Enter the name:")
 age=int(input("Enter the age"))
 marks=int(input("Enter the marks"))
 s=Student(name,age,marks)
 s.check_details()
 print(f"Name:{s.get_name()}")
 print(f"Age:{s.get_age()}")
 print(f"Marks:{s.get_marks()}")
except ValueError as e:
 print(e)
