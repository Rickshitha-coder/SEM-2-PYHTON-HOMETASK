'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer than the other, append the additional letters 
onto the end of the merged string.
Return the merged string.
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r
Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1: a b 
word2: p q r s
merged: a p b q r s'''
def merge_strings(word1, word2):
    merged = ""
    min_length = min(len(word1), len(word2))
    
    # Alternate characters from both strings
    for i in range(min_length):
        merged += word1[i] + word2[i]
    
    # Append remaining characters from the longer string
    merged += word1[min_length:] + word2[min_length:]
    
    return merged

# Test the function
print(merge_strings("abc", "pqr"))  # Output: "apbqcr"
print(merge_strings("ab", "pqrs"))  # Output: "apbqrs"

'''You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means 
not empty, and an integer n, return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length'''

def canPlaceFlowers(flowerbed, n):  #[1,0,0,0,1],n=1
    count = 0
    flowerbed = [0] + flowerbed + [0] #{0,1,0,0,0,1,0}
    
    for i in range(1, len(flowerbed) - 1): #1,6-1=5
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
    else:
        return False
print(canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
print(canPlaceFlowers([1,0,0,0,1], 2))  # Output: False
print(canPlaceFlowers([1,0,0,0,1], 3))  # Output: False
print(canPlaceFlowers([1,0,0,0,1], 4))  # Output: False
print(canPlaceFlowers([1,0,0,0,1], 5))  # Output: False
