'''1.	You are building a program to track user login attempts. Write a function that:
•	Records a new login attempt.
•	Limits login attempts to 5.
•	Locks the account after 5 failed attempts.'''

Id=True
LOGIN_CHECK="RICK123"
for i in range(5):
    login=input("Enter the Login ID:")
    if login==LOGIN_CHECK:
        Id=True
        print("Login Id is valid")
        exit()
    else:
        Id=False
        print("Your login id was wrong")
        print(f"You Have {5-(i+1)} More attempts TRY AGAIN")
if not Id:
    print("Login In Id failed your account is locked")
    print("Try again After Some time")

'''3.	Write a program that takes a number as input and returns the sum of its digits'''
num=int(input("Enter the numebr:"))

sum_of_digits=0
for digit in str(num):
    sum_of_digits+=int(digit)
print(sum_of_digits)

'''4.4.	Identify common elements between two lists.'''
l1=[1,2,3]
l2=[2,3,4]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

'''5.	Write a program that counts the number of words in a given string.'''
sen=input()
word_count=len(sen.split())
print(word_count)
'''6.	Sort a list of integers without using Python's sorted() function.'''
n=int(input("Enter the number of elements in the array"))
elements=list(map(int,input().split())) 
for i in range(n):
 for j in range(0,n-i-1):
     if elements[j]>elements[j+1]:
         elements[j],elements[j+1]=elements[j+1],elements[j]
print(elements)
'''7)Create a BankAccount class to simulate a bank account with features:
Deposit money.
Withdraw money (ensure sufficient balance).
Check balance.'''
print("1.Deposit 2.Withdraw 3.View balance 4.Exit")
balance=10000
while True:
    choice=int(input("Enter the choice you wanted"))
    match choice:
     case 1:
         print("Deposit")
         deposit=int(input("Enter the deposit amount"))
         balance+=deposit
         print(f"You have successfully deposited {deposit}")
     case 2:
         print("Withdraw")
         withdraw=int(input("Enter the withdraw amount"))
         if balance>=withdraw:
             print(f"You have successfully withdrawn {withdraw}")
             balance-=withdraw
         else:
             print("You have insyfficient balance")
     case 3:
        print("Check balance")
        print(balance)
     case 4:
        exit()

     case _:
         print("Invalid Choice")

'''8)Check if a given string is a valid email address'''
import re
email=input("Enter the email id:")
ex=r'^[a-z0-9._%+-]+@gmail\.com$'
if re.match(ex,email):
 print("Valid")
else:
 print("invalid")

'''9.Extract all phone numbers from a given text.'''
text=input("Enter the text")
phone=[]
for i in text:
 if i.isdigit()==True:
     phone.append(i)
for i in phone:
 print(i,end="")
'''10. Extract all hashtags from a given text'''
import re
text=input("Enter the text:")
ex=r'#\w+'
result=re.findall(ex,text)
print(result)

