'''Date:17/03
You are given a string s consisting of lowercase English letters. 
Find the longest substring that satisfies all of the following conditions: 
No repeating characters. 
Contains at least one vowel (a, e, i, o, u). 
If multiple substrings have the same length, return the lexicographically smallest one. 
Output: 
The length of the substring. 
The substring itself. 
Sample Input:  
A single string s of length n 
Sample Output: 
7 
Aeioxyz 
Sample Input 2: 
Bcdfghjklmnp 
Sample output:  
0'''
# Input string
s = input().strip().lower()  # Read the input string and make it lowercase
vowels = "aeiou"  # List of vowels
max_len = 0  # To store the maximum length of valid substring
result = ""  # To store the lexicographically smallest valid substring

# Loop through the string and check substrings
for i in range(len(s)):
    seen = set()  # Set to track unique characters in the current substring
    has_vowel = False  # To check if the substring has a vowel
    for j in range(i, len(s)):
        # If we see a repeated character, break the loop
        if s[j] in seen:
            break
        seen.add(s[j])  # Add the current character to the set
        
        # Check if the current character is a vowel
        if s[j] in vowels:
            has_vowel = True
        
        # Only consider substrings that contain at least one vowel
        if has_vowel:
            current_substring = s[i:j+1]
            # Update the result if we find a longer or lexicographically smaller substring
            if len(current_substring) > max_len or (len(current_substring) == max_len and current_substring < result):
                max_len = len(current_substring)
                result = current_substring

# If no valid substring was found, the result will remain empty, so output 0
if max_len == 0:
    print(0)
    print("")  # Empty string
else:
    print(max_len)
    print(result)
