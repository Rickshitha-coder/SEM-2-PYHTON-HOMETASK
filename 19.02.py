'''Create a payment system where different payment methods (CreditCard, PayPal, UPI) can be used interchangeably.
Each payment method should have a pay(amount) method that prints how the payment is processed.
Use polymorphism to process multiple payment methods dynamically.
Output:
Paid 500 using Credit Card. 
Paid 500 using PayPal. 
Paid 500 using UPI
'''
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)
credit_card = CreditCard()
paypal = PayPal()
upi = UPI()
processor = PaymentProcessor()
processor.process_payment(credit_card, 500)
processor.process_payment(paypal, 500)
processor.process_payment(upi, 500)



'''Given a list of numbers, find the first duplicate element. If no duplicates exist, return -1.
Use a set to optimize performance.
Sample input:
[3, 1, 4, 2, 5, 3, 2]
Sample Output:
3

'''

def find_first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

nums = list(map(int, input("Enter the elements in the list separated by space: ").split()))
print("Original List:", nums)
print("First Duplicate:", find_first_duplicate(nums))
