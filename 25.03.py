'''Date:25.03.2025
There are n kids with candies. You are given an integer array candies, where 
each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
denoting the number of extra candies that you have. 
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all 
the extraCandies, they will have the greatest number of candies among all the kids, 
or false otherwise. 
Note that multiple kids can have the greatest number of candies. 
Input: candies = [2,3,5,1,3], extraCandies = 3 
Output: [true,true,true,false,true]  
Explanation: If you give all extraCandies to: - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids. - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids. - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids. - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids. - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.'''

def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Find the current maximum number of candies any kid has
    result = []

    # Check if each kid can have the maximum or more candies after getting extraCandies
    for candy in candies:
        result.append(candy + extraCandies >= max_candies)
    
    return result

# Example input
candies = [2, 3, 5, 1, 3]
extraCandies = 3
output = kidsWithCandies(candies, extraCandies)
print(output)  # Output: [True, True, True, False, True]
