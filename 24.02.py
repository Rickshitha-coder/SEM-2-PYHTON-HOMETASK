'''Checks for twin primes (pairs of prime numbers that differ by 2) within a given range.
Sample input”
1
50
Sample Output:
Twin Primes: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)'''
def is_prime(n):# Check if a number is prime.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):#FInd twin primes within a given range.
    
    twin_primes = []
    for i in range(start, end - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

# Sample input
start = int(input("Enter the start Range:"))
end = int(input("Enter the end  Range:"))

# Find and print twin primes
twin_primes = find_twin_primes(start, end)
print("Twin Primes:", twin_primes)


'''2. Write a program that:
Takes an input range (start and end).
Finds all prime numbers within the range.
Checks if they are palindromes.
Outputs all palindromic prime numbers in the given range.
Sample Input:
Enter start: 10 
Enter end: 200'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def prime_palindromes(start, end):
    result = []
    for num in range(start, end + 1):
        if is_prime(num) and is_palindrome(num):
            result.append(num)
    return result
start = int(input("Enter the start Range:"))
end = int(input("Enter the end  Range:"))
palindrome_primes = prime_palindromes(start, end)
print("Prime Palindromes in the given range:", palindrome_primes)
