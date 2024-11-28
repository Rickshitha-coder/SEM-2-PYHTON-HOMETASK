#1.Create a BankAccount class that handles common operations like depositing money, withdrawing money, and checking the balance.
class Bank:
 #constructor to initialize the objects
 def __init__(self,holder_name,acc_num,initial_bal=0):
     self.holder_name=holder_name
     self.acc_num=acc_num
     self.balance=initial_bal
     print(self.holder_name,self.acc_num)
 def deposit(self,amount):
     if amount>0:
         print(f"you have DEPOSITED {amount} successfully")
         self.balance+=amount
     else:
         print("your DEPOSIT AMOUNT is invalid")
 def withdraw(self,amount):
     if amount<self.balance:
         print(f"you have WITHDRAWN {amount} successfully")
         self.balance-=amount
     else:
        print("you DON'T have sufficient fund")
 def check_balance(self):
     print(f" your CURRENT balance is {self.balance}")
user=Bank("Rickshi",8072688557,10000)

user.deposit(1000)
user.check_balance()

user.withdraw(5000)
user.check_balance()

#2. Scenario: Cosmetic Product Information  (Default constructor)
class Cosmetics:
 def __init__(self,product_name="COMPACT POWDER",price=190,brand="Maybeline",category="MAKEUP"):
     self.product_name=product_name
     self.price=price
     self.brand=brand
     self.category=category
 def show(self):
     print(f"The product name is {self.product_name}")
     print(f"Price is ${self.price}")
     print(f"Brand is {self.brand}")
     print(f"Category is {self.category}")
choice=Cosmetics("eyemake")

choice.show()
