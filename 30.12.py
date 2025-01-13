'''1. Write a program to count how many alphabetic characters, numbers, and special
characters are in a string.
Input: Enter a string: Prep123!@#
Output:
Alphabetic Characters: 4
Numeric Characters: 3
Special Characters: 3
'''
string=input("Enter the string to count:") 
alphabet=0
number=0
special=0
for i in string:
 if i.isalpha():
     alphabet+=1
 elif i.isdigit():
     number+=1
 else:
     if not i.isalnum():
         special+=1
print("Alphabetic Characters Count:",alphabet)
print("Numeric Characters count",number)
print("Special Characters Count",special)
'''2. Write a program to validate whether the string contains at least one alphabet and one
special character.
Input: Enter a string: Prep!@123
Output: The string contains both alphabets and special character'''
import re
string=input("Enter the string you want to check:")
ex=r'^(?=.*[a-zA-z].{1,})(?=.*[!@#$%^&*()]).{1,}$'
if re.match(ex,string):
 print("Valid ")
else:
 print("Not valid")
