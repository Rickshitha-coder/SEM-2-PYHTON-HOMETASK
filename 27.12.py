'''Polymarphism --> only if the parameters are same  and method name also same IF IT IS NOT SAE ITS SHOW AN ERROR''' 

class CreditCardPayment:
    def pay(self,amount):
        return f"paid {amount} using creditcard"
class PayPalPayment:
    def pay(self,amount):
        return f"paid {amount} using PayPal"
class DebitCardPayment:
    def pay(self,amount):
        return f"paid {amount} using debitcard"
def process_payment(payment_method,amount):
    print(payment_method.pay(amount))
print("-->  Creditcard Payment  <--")
cc=CreditCardPayment()
process_payment(cc,200)   #cc-->payment 200--amount
print("-->  PayPal Payment  <--")
pp=PayPalPayment()
process_payment(pp,500)
print("-->  DebitCard Payment  <--")
dc=DebitCardPayment()
process_payment(dc,100)
