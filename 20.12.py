import random
import re
class Member:
    def __init__(self,member_id,name,email):
        self.member_id=member_id
        self.name=name
        self.email=email
    def verify_email(self):
        ex=r'^[a-z0-9._%+-]+@gmail\.com$'
        if re.match(ex,email):
            print("Valid email id")
        else:
            print("Email id is not valid")
    def verify_member_id(self):
        mem=r'^LIB\d{4}$'
        if re.match(mem,member_id):
            print("Valid member id")
        else:
            self.generate_member_id()
    def generate_member_id(self):
        self.member_id="LIB"+str(random.randint(1000,9999))
        
class Library(Member):
    def __init__(self,member_id,name,email,book_id,title,author):
        Member.__init__(self,member_id,name,email)
        self.book_id=book_id
        self.title=title
        self.author=author
    def display_overall(self):
        print("Member id:",self.member_id)
        print("Name:",self.name)
        print("Email:",self.email)
        print("Book borrowed or returned id:",self.book_id)
        print("Book titile:",self.title)
        print("Author:",self.author)
member_id=input("Enter the id of the member:")
name=input("Enter the name:")
email=input("Enter the email id")
book_id=input("Enter the book id:")
title=input("Enter the book title:")
author=input("Enter the name of the author:")

l=Library(member_id,name,email,book_id,title,author)
l.verify_email()
l.verify_member_id()
l.display_overall()
