'''
Date : 7-2-25
2. Count how many trailing zeros are in n! (n factorial).
Input: 10 
Output: 2 (since 10! = 3,628,800)'''
import math
n=int(input("Enter a number: "))
factorial=str(math.factorial(n))
print(f"Factoral of {n} is: ",factorial)
count_zero=0
for i in factorial:
 if i=='0':
     count_zero+=1
print(f"Count of zero's in {n}! is: ",count_zero)

'''
1. To convert an integer to English words, we need to break it down into groups of thousands 
and handle each group separately.
Sample Input: 45
Sample Output : "Forty Five"
Sample Input: 12345
Sample Output : Twelve Thousand Three Hundred Forty Five'''
def num_to_words(n):
    ones=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens=["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if n==0:
        return "Zero"
    elif n<10:
        return ones[n]
    elif n<20:
        return teens[n-10]
    elif n<100:
        return tens[n//10]+(" " +ones[n%10] if n%10!=0 else "")
    elif n<1000:
        return ones[n//100]+" Hundred"+(" " +num_to_words(n%100) if n%100!=0 else "")
    elif n < 1000000:
        return num_to_words(n//1000)+"Thousand"+(" "+num_to_words(n%1000) if n%1000!=0 else "") 
    else:
        return "Number too large"
num=int(input("Enter a number: "))
print(num_to_words(num))
