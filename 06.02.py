'''Date : 6-02-25
1. Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"'''
def longest_palindrome(s):
    if not s:
        return ""
    longest="" 
    for i in range(len(s)): 
        for j in range(i, len(s)): 
            substring=s[i:j+1] 
            if substring==substring[::-1] and len(substring)>len(longest):  
                longest=substring
    return longest
s=input("Enter a string: ")  
print("Longest palindromic substring:",longest_palindrome(s))
