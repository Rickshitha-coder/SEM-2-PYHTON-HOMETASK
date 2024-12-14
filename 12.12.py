'''Create a Student class to manage basic student information.
1. Attributes:
➢ student_id: Unique identifier for the student in the format STU1234.
➢ name: The name of the student. ( Must be at least 2 characters long and should only 
contain alphabets and spaces.)
➢ grade: The grade/class of the student. (Should only accept specific valid grades, e.g., 
"1st Grade", "2nd Grade", ..., "12th Grade".Ensure the grade follows the format: 
<number>th Grade)
2. Methods:
➢ Validatedetails()
➢ display_details()'''


import random
class Student:
 def __init__(self, student_id, name):
     self.student_id = student_id
     self.name = name
     
 def gen_rand_id(self):
     s_id = random.randint(1000, 9000)
     return f"STU{s_id}"
 def verify_id(self):
     student_id = input("Enter student ID: ")
     student_len = len(student_id)
     if student_len == 7:
        if student_id.startswith("STU"):
            if student_id[3:].isdigit():
                print("Valid")
                return student_id
            else:
                print("Invalid")
        else:
            print("Invalid")
     else:
        print("Invalid")
 def verify_name(self):
     name = input("Enter name: ")
     name_len = len(name)
     if name_len >= 2 and name.replace(" ","").isalpha():
         print("Valid")
         return name
     else:
         print("Invalid")
student = Student("","")
print("Generated Student ID:", student.gen_rand_id())
student_id = student.verify_id()
name = student.verify_name()
