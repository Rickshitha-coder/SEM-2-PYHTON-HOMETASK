'''1. Keerthana wants to print the UserName and Department and Mobile
number and also print the same in the required format.
Conditions of Input:
Print your name Concatenate with First Name and Last Name
Print Concatenate with College name and Stream
Print the ASCII value of Your Name
Print the ASCII value of your Mobile Number
Print the ASCII value Addition Result of Your Name and Mobile
number with Alternate method'''
class Details:
        def __init__(self):
            self.first_name=input("Enter the first name:")
            self.second_name=input("Enter the last name:")
            self.phone=int(input("enter the phone number:"))
            self.college_name=input("Enter the college name:")
            self.stream=input("Enter the stream:")
            self.name=self.first_name+self.second_name
        def display(self):
            print("Name of the Student:",self.name)
            print("Name of College is :",self.college_name,"Department of",self.stream)
        def ASCII_value(self):
            print("ASCII values of Name:")
            for i in self.name:
                print(i,"-",ord(i),end=" ")
            print()
            print("ASCII values of Phone:")
            for m in str(self.phone):
                print(m,"-",ord(m),end=" ")
            print()
        def ASCII_addition(self):
            print("Result of Addition:")
            self.ascii_addition=[]
            for i, m in zip(self.name, str(self.phone)):
                addition = ord(i) + ord(m)
                self.ascii_addition.append(f"{i}+{m} = {addition}")
            print("-".join(self.ascii_addition))
det=Details()
det.display()
det.ASCII_value()
det.ASCII_addition()
'''Nithya wants to print the Operational Result with two user input
values.
1. Do the all Arithmetic operation and Print the result.
2. Swapping Three values using bitwise operator without third
variable .'''

def arithmetic_operations():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    print("Arithmetic Operations Are:")
    print("Addition:", n1 + n2)
    print("Subtraction:", n1 - n2)
    print("Multiplication:", n1 * n2)
    print("Division:", n1 / n2)
    print("Modulus:", n1 % n2)
    print("Exponentiation:", n1 ** n2)

def swap_three_values():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))

    print("Before Swapping:")
    print("Number 1:", n1)
    print("Number 2:", n2)
    print("Number 3:", n3)

    # Swap num1, num2, and num3 using bitwise XOR operator
    n1 = n1 ^ n2
    n2 = n1^ n2
    n1 = n1 ^ n2
    
    n2 = n2 ^ n3
    n3 = n2 ^ n3
    n2 = n2 ^ n3

    print("After Swapping:")
    print("Number 1:", n1)
    print("Number 2:", n2)
    print("Number 3:", n3)


arithmetic_operations()
swap_three_values()

'''Kathir has to design a method that will accept the UserName Input:
Print Username with Conditions
Requirements: Name with Special Characters
a. Print the string with special characters.
Input:
Enter First Name : face123@#$%^
Output:
Hi ! Your Entered Input is “face@#$%^”
b. Split Characters and Special Characters from the given string.
Enter Name : faceprep12345!@#$%^&
Your entered Characters are –faceprep
Your entered Special Characters are -!@#$%^&'''
n=input("Enter the name:")
#Print the string with special characters.
for char in n:
    if char.isdigit()==False:
        print(char,end="")
print()
#Split Characters and Special Characters from the given string.
for char in n:
    if char.isalpha():
        print(char,end="")
print()
for char in n:
    if not char.isalnum():
        print(char,end="")


































