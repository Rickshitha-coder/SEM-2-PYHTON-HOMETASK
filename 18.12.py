'''Date : 18-12-24 Task – Method overloading
Implement a class Calculator with a method calculate that performs different 
operations based on the input parameters:
1. If one argument is provided, return its square.
2. If two arguments are provided, return their sum.
3. If three arguments are provided, return their product.
If any of the arguments are not integers or floats, or if the input doesn't match 
the constraints, raise a ValueError'''
class Calculator:
    def calculate(self,a,b=0,c=0):
         result=0
         for i in (a,b,c):
             if type(i) not in (int,float):
                 raise ValueError("It must Be in Integer and float")
         if a!=0 and b==0 and c==0:
             result=a*a
             return result
         elif a!=0 and b!=0 and c==0:
             result=a+b
             return result
         else:
             result=a*b*c
             return result
ad=Calculator()
try:
    ans=ad.calculate(3)
    print(ans)
    ans1=ad.calculate(5,2)
    print(ans1)
    ans2=ad.calculate(5,3,4)
    print(ans2)
    ans3=ad.calculate(5,3,"A")
except ValueError as e:
    print(e)

        
