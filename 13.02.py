'''Date : 13-2-25
1. Print the following pattern and use method to call the pattern logic.
 1 
 1 2 
 1 2 3 
1 2 3 4 
1 2 3 4 5'''
def print_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

n=int(input("Enter the numbers:"))
print_pattern(n) #function call
'''2. A bank's IT department is working on a security feature that involves prime number 
verification. They need a program that can check whether a given number is prime using a 
method (function)'''
def is_prime(n):
    if n < 2:
        return "Enter a positive number greater than 1"
    elif n == 2:
        return "Prime"
    else:
        for i in range(2,n):
            if n % i == 0:
                return "Not Prime"
        return "Prime"

n = int(input("Enter a number: "))
print(is_prime(n))
