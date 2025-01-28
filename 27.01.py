'''1.Keerthana has to design a method that will accept the UserName and
Password from the user and also print the same in the required format.
Input:
Enter your Name:
Enter your Department:
Enter your Password:
Re-Type your Password:
Output:
Your Encoded Name is: XXXXX – Fresher
Your Department is: XXXX
Your Password is: XXXXX
Re-Type your Password: XXXXX
Condition:
1. User Name Validation: Should not allow Numbers & any special characters
to be entered.
2. Password: Must contain at least one number and one Special character.
Should not be greater than 8 in length
3. User must be allowed to continue till he enters in the correct format'''
def details():
 while True:
     name=input("Enter your name:")
     if not name.isalpha() or name in "!@#$%^&*_":
         print("Username should contain only letters and should not have any special  characters")
         continue
     dep=input("Enter your Department:")
     password=input("Enter your password:")
     if not any(i.isdigit() for i in password) or not any(i in "!@#$%^&*_" for i in 
password) or len(password)<=8:
         print("Password must be 8 characters or less, with at least one number and one special character. Try again")
         continue
     retype=input("Re-Type your Password: ")
     if password!=retype:
         print("Passwords does not match.Try again")
         continue
     encoded_name="X"*len(name)
     encoded_dep="X"*len(dep)
     encoded_pass="X"*len(password)
     encoded_retype="X"*len(retype)
     print(f"Your Encoded Name is: {encoded_name}")
     print(f"Your Department is: {encoded_dep}")
     print(f"Your Password is: {encoded_pass}")
     print(f"Re-Type your Password: {encoded_retype}")
     break
details()


'''2.Write a Python program to remove the first occurrence of a specified
element from an array.
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Remove the first occurrence of 3 from the said array:
New array: array('i', [1, 5, 3, 7, 1, 9, 3])
'''
n=int(input("Enter the number of items in the list"))
t=int(input("Enter the target"))
arr=[]
for i in range(n):
    e=int(input())
    arr.append(e)
print(arr)
for i in arr:
 if i==t:
     arr.remove(i)
     break
print("New array:",arr)



'''3.Create an array with limited Input size and Print Inverse and Non Inverse
Order.
The Array is - [Face, Prep, Campus, Tech, Solutions]
Sample Output Your Inverse order Array is - [Solutions ,Tech, Campus,
Prep, Face]
Your Non - Inverse Order Array is - [Face, Prep, Campus, Tech, Solutions]'''
n=int(input("Enter the number of elements in the array"))
arr=[]
for i in range(n):
 e=input()
 arr.append(e)
arr.reverse()
print("Your Inverse order Array is -",arr)
arr.reverse()
print("Your Non - Inverse Order Array is -",arr)
