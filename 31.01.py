'''Date : 31-01-25
1.Zampa is required to handle his book stall with certain information. He is trying to formulate his 
information and also automize the discount process. To do this he has to get the following information 
from the customer. [Use class and methods]
INPUT: 
Enter your Book Name: 
Enter your Customer ID: 
OUTPUT: 
Price of the Book is <<XYX>> MRP 
You are eligible for Discounted of <<X>>% 
Your discounted Price for the Book is <<XXX>> MRP 
Do you want to continue? 
Note: This Output is the basic output. But will vary based on the need. 
CONDITION: 
1. Do the basic validation of the input before accepting it from the user 
2. Based on the discount and the price calculate the discounted price to display to the user. 
3. Based on the Customer ID Discount is created. 
a. 1-100 – 50% discount 
b. 101-300 – 30% discount 
c. 301-400 – 20% discount 
d. 401-500 – 10% discount 
e. >500 – No Discount 
4. Customer should not enter the details in the output screen'''

class BookStall:
    def __init__(self):
        self.books = {
            "Python": 500,
            "Maths": 300,
            "Tamil": 200,
            "English": 400,
            "AI": 600
        }
        print(self.books)
    def validate_input(self, book_name, customer_id):
        if book_name not in self.books:
            return "Invalid book name"
        if not customer_id.isdigit():
            return "Invalid customer ID"
        return None

    def calculate_discount(self, customer_id):
        customer_id = int(customer_id)
        if customer_id >= 1 and customer_id <= 100:
            return 50
        elif customer_id >= 101 and customer_id <= 300:
            return 30
        elif customer_id >= 301 and customer_id <= 400:
            return 20
        elif customer_id >= 401 and customer_id <= 500:
            return 10
        else:
            return 0

    def calculate_discounted_price(self, book_price, discount):
        return book_price - (book_price * discount / 100)


book_stall = BookStall()
while True:
    book_name = input("Enter your Book Name: ")
    customer_id = input("Enter your Customer ID: ")
    error = book_stall.validate_input(book_name, customer_id)
    if error:
        print(error)
        continue
    book_price = book_stall.books[book_name]
    discount = book_stall.calculate_discount(customer_id)
    discounted_price = book_stall.calculate_discounted_price(book_price, discount)
    print(f"Price of the Book is {book_price} MRP")
    print(f"You are eligible for Discount of {discount}%")
    print(f"Your discounted Price for the Book is {discounted_price} MRP")
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        break




