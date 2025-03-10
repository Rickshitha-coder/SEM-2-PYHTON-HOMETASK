'''Write a Python program that takes an integer input N and prints N rows of a pattern where: 
1. Each row starts with an increasing character from 'a' onward. 
2. The row consists of two alternating characters repeated twice (e.g., "abab", "bcbc"). 
3. The number of rows printed should be equal to the given input N. 
Sample Input: 
Enter a number: 3 
Sample Output: 
abab   
bcbc   
cdcd  '''
def print_pattern(N):
    for i in range(N):
        first_char = chr(ord('a') + i)  # First character in the row
        second_char = chr(ord('a') + i + 1)  # Second character in the row
        row_pattern = (first_char + second_char) * 2  # Repeat "xy" twice
        print(row_pattern)

# Take input from the user
N = int(input("Enter a number: "))
print_pattern(N)

'''Write a Python program that takes an integer input N and prints N rows of a pattern where: 
1. Each row starts with an increasing character from 'a' onward. 
2. The row consists of the first character repeated twice, followed by the next character 
repeated twice (e.g., "aabb", "bbcc"). 
3. The number of rows printed should be equal to the given input N. 
Sample Input: 
Enter a number: 3 
Sample Output: 
aabb   
bbcc   
ccdd  '''
def print_pattern(N):
    for i in range(N):
        first_char = chr(ord('a') + i)  # First character in the row
        second_char = chr(ord('a') + i + 1)  # Second character in the row
        row_pattern = first_char * 2 + second_char * 2  # "aabb", "bbcc", etc.
        print(row_pattern)

# Take input from the user
N = int(input("Enter a number: "))
print_pattern(N)
