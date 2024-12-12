'''1. Create a class that validates the password which contains various methods to validate the 
password.
Get input from the user and validate the password.
Write a program to validate the password based on these rules and provide feedback(Valid 
or invalid).
Password rules:
At least one uppercase letter.
At least one lowercase letter.
At least one digit.
At least one special character.
Minimum length of 8 characters.'''
class Password:
    def validate(text):
        u_count=0
        l_count=0
        d_count=0
        s_count=0
        length=len(text)
        for i in text:
            if i.isupper():
                u_count+=1
            elif i.islower():
                l_count+=1
            elif i.isdigit():
                d_count+=1
            else:
                s_count+=1
        if u_count>=1 and l_count>=1 and d_count>=1 and s_count>=1 and length>=8:
            print("your password is vaild")
        else:
            print("Your password is invaild")
user=input("Enter the Password:")
Password.validate(user)
























        



