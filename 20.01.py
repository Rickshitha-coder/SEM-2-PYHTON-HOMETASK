'''Topic : Encapsulation
Create a BankAccount class with private attributes:
• __account_number
• __balance
Implement public methods to:
1. Set the account number and initialize the balance.
2. Deposit and withdraw money.
3. Implement a method add_interest(rate) to calculate and add interest to the balance.'''
class BankAccount:
    def __init__(self):
        self.__account_number=int(input("Enter the Your Account Number:"))
        self.__initial_balance=int(input("Enter the inital balance:"))
    def get_account_number(self):
        return self.__account_number
    def get_initial_balance(self):
        return self.__initial_balance
    def deposit(self,amount):
        if amount>0:
            self.__initial_balance+=amount
            print(f"Deposited ${amount:.2f}. Current balance: ${self.__initial_balance:.2f}")
        else:
            print("Invaild Amount")
    def withdraw(self,amount):
        if 0<amount<=self.__initial_balance:
            self.__initial_balance-=amount
            print(f"withdraw ${amount:.2f}. Current balance: ${self.__initial_balance:.2f}")
        else:
            print("Invaild Amount")
    def add_interest(self,rate):
        interest=self.__initial_balance*rate
        self.__initial_balance+=interest
        print(f"Added ${interest:.2f} interest. Current  balance: ${self.__initial_balance:.2f}")
account = BankAccount()
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: ${account.get_initial_balance():.2f}")
des=int(input("Enter the despoist amount:"))
account.deposit(des)
withdraw_amount=int(input("Enter the withdraw amount:"))
account.withdraw(withdraw_amount)
rate_per=int(input("Enter the interest rate:"))
account.add_interest(rate_per)


    
