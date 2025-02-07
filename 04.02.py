'''Given a string s consisting of words and spaces, return the length of the last word in the 
string.A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''
def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
# Test the function
s=input("Enter the String:")
print(length_of_last_word(s))  

'''Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101'''
a=input("Enter the number:")
b=input("Enter the number:")
print(bin(int(a,2)+int(b,2))[2:])
#or
a=input("Enter the numebr:")
b=input("Enetr te number:")
sum_ab=int(a,2)+int(b,2)
print(sum_ab)
