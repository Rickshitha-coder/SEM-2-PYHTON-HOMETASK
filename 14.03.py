''' Date:14.03
You are given a 0-indexed array of unique strings words.
A palindrome pair is a pair of integers (i, j) such that:
0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.
You must write an algorithm with O(sum of words[i].length) runtime complexity.
Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"'''
words=input("Enter words (comma-separated):").split() #abcd dcba lls s sssll
results=[]
for i in range(len(words)): #0 #1 #2
    for j in range(len(words)): #0 | 1 |2|3|4  |0,1,2,3,4 |0,
        if i!=j: #0!=1 0!=2 |0!=3 |0!=4 |1!=0 ,1!=2,1!=3, 1!=4| 2!=0,2!=1,2!=2,2!=3,2!=4
            combined=words[i]+words[j]  #abcd+dcba | dcba+abcd | lls+sssll
            if combined==combined[::-1]: #abcddcba==abcddcda | dcbaabcd | llssssll
                results.append([i,j]) #[0,1][1,0] [2,4]
print(results)#[0,1] [1,0] [2,4]
 
