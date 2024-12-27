'''Date : 26-12-24 Task :Exceptional handling
You are building a Python program that interacts with a simple calculator class. The program takes 
two numbers and an operation (e.g., addition, subtraction) as input from the user. It should handle 
the following exceptions:
1. ZeroDivisionError: If the user attempts to divide by zero, inform the user and allow them to 
retry.
2. ValueError: If the user provides non-numeric input for the numbers, inform them and allow 
them to retry.
3. KeyError: If the user provides an invalid operation (e.g., not +, -, *, or /), inform them and 
allow them to retry.
4. TypeError: If any unexpected data type issue occurs, catch it and raise the error'''
class Calculator:
 def __init__(self,operator1,operator2):
     self.operator1=operator1
     self.operator2=operator2
 def choices(self):
     if not isinstance(operator1,int) or not isinstance(operator2,int):
         raise ValueError("DATA TYPE IS WRONG TRY AGAIN")
     else:
         if choice>=3:
             raise KeyError("CHOICES ARE INVALID")
             
         else:
             match choice:
                 case 1:
                     result=self.operator1+self.operator2
                     return result
                 case 2:
                     result=self.operator1-self.operator2
                     return result
                 case 3:
                     if self.operator2==0:
                         raise ZeroDivisionError ("OPERATOR SHOULD NOT BE ZERO, IT SHOULD STARTS FROM 1")
                     else:
                         result=self.operator1/self.operator2
                         return result
                 case _:
                    exit()
 
 
try:
 
 while True:
     print("1)addition \n2)subtraction \n3)division")
     choice=int(input("Enter your choice : "))
     operator1=int(input("Enter the operator number 1:"))
     operator2=int(input("Enter the operator number 2:"))
     cal=Calculator(operator1,operator2)
     result=cal.choices()
     print(result)
except ValueError as e:
 print(e)
except KeyError as e:
 print(e)
except ZeroDivisionError as e:
 print(e)
