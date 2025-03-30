''' Date:20.03
Given an unsorted array of integers, rearrange the array so that: 
All even-indexed elements are greater than their adjacent odd-indexed elements. 
All odd-indexed elements are less than their adjacent even-indexed elements. 
Input:  [5, 3, 1, 2, 3, 7, 6, 4] 
Output: [5, 1, 3, 2, 7, 3, 6, 4]
'''
def rearrange_array(arr):
    for i in range(len(arr) - 1):
        if i % 2 == 0 and arr[i] <= arr[i + 1]:  # Even index, should be greater
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i % 2 == 1 and arr[i] >= arr[i + 1]:  # Odd index, should be smaller
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Example
arr = [5, 3, 1, 2, 3, 7, 6, 4]
print(rearrange_array(arr))  # Output: [5, 1, 3, 2, 7, 3, 6, 4]
'''Iteration 1 (i = 0, Even Index)
arr[0] = 5, arr[1] = 3
✅ 5 > 3, no swap.
Iteration 2 (i = 1, Odd Index)
arr[1] = 3, arr[2] = 1
❌ 3 > 1, swap → [5, 1, 3, 2, 3, 7, 6, 4]
Iteration 3 (i = 2, Even Index)
arr[2] = 3, arr[3] = 2
✅ 3 > 2, no swap.
Iteration 4 (i = 3, Odd Index)
arr[3] = 2, arr[4] = 3
✅ 2 < 3, no swap.
Iteration 5 (i = 4, Even Index)
arr[4] = 3, arr[5] = 7
❌ 3 < 7, swap → [5, 1, 3, 2, 7, 3, 6, 4]
Iteration 6 (i = 5, Odd Index)
arr[5] = 3, arr[6] = 6
✅ 3 < 6, no swap.
Iteration 7 (i = 6, Even Index)
arr[6] = 6, arr[7] = 4
✅ 6 > 4, no swap.Iteration 1 (i = 0, Even Index)
arr[0] = 5, arr[1] = 3
✅ 5 > 3, no swap.
Iteration 2 (i = 1, Odd Index)
arr[1] = 3, arr[2] = 1
❌ 3 > 1, swap → [5, 1, 3, 2, 3, 7, 6, 4]
Iteration 3 (i = 2, Even Index)
arr[2] = 3, arr[3] = 2
✅ 3 > 2, no swap.
Iteration 4 (i = 3, Odd Index)
arr[3] = 2, arr[4] = 3
✅ 2 < 3, no swap.
Iteration 5 (i = 4, Even Index)
arr[4] = 3, arr[5] = 7
❌ 3 < 7, swap → [5, 1, 3, 2, 7, 3, 6, 4]
Iteration 6 (i = 5, Odd Index)
arr[5] = 3, arr[6] = 6
✅ 3 < 6, no swap.
Iteration 7 (i = 6, Even Index)
arr[6] = 6, arr[7] = 4'''
✅ 6 > 4, no swap.
