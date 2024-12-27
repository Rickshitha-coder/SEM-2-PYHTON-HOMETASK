'''Date: 24-12-24 Task : function with error handling
Use class and object : Provide the method inside the class and call the method using the object.
You are building an e-commerce platform, and one of the functionalities is to calculate the final price 
of a product after applying a discount and tax. The price calculation is based on the following:
1. A base price of the product.
2. A discount percentage (e.g., 10% off).
3. A tax percentage (e.g., 5% tax).
Write a Python function, calculate_final_price, that takes the following inputs:
• base_price (float): The original price of the product.
• discount_percentage (float): The percentage discount to be applied (default is 0%).
• tax_percentage (float): The percentage tax to be applied (default is 0%).
The function should:
• Return the final price of the product, rounded to two decimal places.
• Include error handling to ensure that negative values for base_price, discount_percentage, 
or tax_percentage raise a ValueError.'''
class Commerce:
 def __init__(self,base_price,discount_percentage=0,tax_percentage=0):
     self.base_price=base_price
     self.discount_percentage=discount_percentage
     self.tax_percentage=tax_percentage
 def final(self):
     if base_price <0 or discount_percentage <0 or tax_percentage<0:
         raise ValueError ("Invalid amount")
     else:
         discount_amount=((discount_percentage)/100)*base_price
         tax_amount=(tax_percentage/100)*base_price
         total_price=(base_price+tax_amount)-discount_amount
         return total_price
base_price=float(input("Enter the base price "))
tax_percentage=float(input("Enter the tax percentage"))
discount_percentage=float(input("enter the discount percentage"))
try:
 c=Commerce(base_price,discount_percentage,tax_percentage)
 result=c.final()
 print(result)
except ValueError as e:
 print(e)
