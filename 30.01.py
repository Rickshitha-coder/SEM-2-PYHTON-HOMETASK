'''Benedict needs to write a simple code to ask the user his name and also the number of times 
he wants his name to be printed. Use class and method to validate. The format to display has 
been given below 
INPUT: 
Enter your Name: 
Enter your Password: 
Enter your Email Address: 
How many times to want to Print? 
OUTPUT: 
<<Name>> Wants to Print <<N>> Times and send Mail to <<email-id>>. 
Your password <<password>> will be encrypted and will be stored. 
Condition: 
Include Password to your program 
Name Validation: Should allow only one Number & one special character 
Password: Must not contain any Number and Special characters except (#, _ and @). Should not be 
greater than 8 in length 
Email Id: Should be valid format. 
User must be allowed to continue till he enters in correct format'''
import re

class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def validate_name(self):
        if re.search(r'\d', self.name) and re.search(r'[^a-zA-Z0-9\s]', self.name):
            return True
        else:
            return False

    def validate_password(self):
        if len(self.password) <= 8 and re.search(r'[^a-zA-Z#_@]', self.password) is None:
            return True
        else:
            return False

    def validate_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, self.email):
            return True
        else:
            return False

def main():
    while True:
        name = input("Enter your Name: ")
        password = input("Enter your Password: ")
        email = input("Enter your Email Address: ")

        user = User(name, password, email)

        if user.validate_name() and user.validate_password() and user.validate_email():
            break
        else:
            print("Invalid input. Please try again.")

    while True:
        try:
            n = int(input("How many times to want to Print? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"{name} Wants to Print {n} Times and send Mail to {email}. Your password {password} will be encrypted and will be stored.")

if __name__ == "__main__":
    main()

