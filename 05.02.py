'''Date : 5-2-25
1. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''
def common_prefix(strs):
    if not strs:
        return ""
    
    shortest_str = min(strs) #fly
    for i, char in enumerate(shortest_str): #0,f  1,l  2,y
        for other_str in strs: #fly-->f flower-->f flew-->f | fly-->l flower-->l flew-->l | fly-->y flower-->o flew-->e
            if other_str[i] != char: # y!=o
                return shortest_str[:i] #fl
    return shortest_str
strs=input("Enter the Elements in list:").split()  #fly flower flew
print(strs)
print(common_prefix(strs))  # Output: "fl"

'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can 
be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
def is_subsequence(s, t): #abc aghbdec
    t_index = 0
    s_index = 0

    while t_index < len(t) and s_index < len(s): #0<7 and 0<3| 1<7 and 1<3| 2<7 and 1<3 |3<7 and 1<3| 4<7 and 2<3| 5<7 and 2<3| 6<7 and 2<3 | 7<7 and #<3-->failed
        if t[t_index] == s[s_index]: #a==a g!=b h!=b b==b d==c e==c c==c
            s_index += 1 #1| 2 | 3
        t_index += 1 #1 | 2 | 3 | 4 | 5 | 6

    return s_index == len(s)

s=input("Enter the substring:")  #abc
t=input("Enter the main string:") #aghbdec
print(is_subsequence(s,t)) #abc
