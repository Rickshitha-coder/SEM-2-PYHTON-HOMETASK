'''Date: 25-2-25
1. Print the following pattern using python
Sample Output:
1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9'''
def generate_spiral_pattern(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, left = 0, 0
    bottom, right = n - 1, n - 1

    while num <= n * n:
        # Fill top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    for row in matrix:
        print(" ".join(map(str, row)))

# Set n=5 for the given pattern
n=int(input("Enter the number"))
generate_spiral_pattern(n)



'''2. The Collatz Conjecture
For any positive integer n:
1. If n is even, divide it by 2 → n = n / 2.
2. If n is odd, multiply it by 3 and add 1 → n = 3n + 1.
3. Repeat until n becomes 1.
Input: 12
Output: 12 steps to reach 1

*Example 1: n = 10*
1. n is even (10), so divide by 2: n = 5
2. n is odd (5), so multiply by 3 and add 1: n = 16
3. n is even (16), so divide by 2: n = 8
4. n is even (8), so divide by 2: n = 4
5. n is even (4), so divide by 2: n = 2
6. n is even (2), so divide by 2: n = 1

total steps 6

'''
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Example input
n = int(input())
print(f"{collatz_steps(n)} steps to reach 1.")


















