'''Date : 10-2-25
1. find the Kth largest element in an unsorted list
Input:
Space separated input
K value
Sample Input:
6 2 4 5 7
3
Sampel Output: 
5'''
arr=list(map(int, input("Enter the elements:").split()))
k=int(input("Which largest element you want:"))
arr.sort(reverse=True)
print(f"The {k} Largest Elements is {arr[k-1]}")


arr=list(map(int, input("Enter the elements:").split()))
k=int(input("Which largest element you want:"))
max_val=float('-inf')
for i in range(k):
    temp_max=float('-inf')
    for num in arr:
        if num>temp_max:
            temp_max=num
    max_val=temp_max
    arr.remove(max_val)
print(f"The {k}  largest element is {max_val}")

'''2. Check if a Number is a Disarium Number
A Disarium number is a number where the sum of its digits raised to their respective positions is 
equal to the number itself.
Example: 135 is a Disarium number because 1^1 + 3^2 + 5^3 = 135'''
num=int(input())  #135
digits=list(map(int, str(num))) #[1,3,5]
disarium_sum=sum(d **(i+1) for i,d in enumerate(digits)) #1^1 + 3^2 + 5^3 = 135
if disarium_sum == num:  #135===135
    print("Disarium Number")
else:
    print("Not a Disarium Number")
