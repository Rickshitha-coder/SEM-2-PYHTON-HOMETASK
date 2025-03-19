'''Date 18.03
Given a nested list like: 
arr = [1, [2, [3, [4, 5]], 6], 7] 
Write a function to flatten it into a single list: 
[1, 2, 3, 4, 5, 6, 7] 
(Without using built-in libraries like itertools!)'''
def flatten(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Test the function
arr = [1, [2, [3, [4, 5]], 6], 7]
print(flatten(arr))  # Output: [1, 2, 3, 4, 5, 6, 7]
