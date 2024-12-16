'''Date : 12-12-24       
Task – Class programs 
Create a Student class to manage basic student information. 
1. Attributes: 
➢ student_id: Unique identifier for the student in the format STU1234. 
➢ name: The name of the student. ( Must be at least 2 characters long and should only 
contain alphabets and spaces.) 
➢ grade: The grade/class of the student. (Should only accept specific valid grades, e.g., 
"1st Grade", "2nd Grade", ..., "12th Grade".Ensure the grade follows the format: 
<number>th Grade) 
2. Methods: 
➢ Validatedetails() 
➢ display_details() '''


class Student:
    def __init__(self):
        self.id=input("Enter the id")
        self.name=input("enter the name")
        self.grade=input("enter the grade")
    def validate_id(self):
        
        id_len=len(self.id)
        if id_len==7:
            if self.id[0]=="S" and self.id[1]=="T" and self.id[2]=="U" :
                if self.id[3] and self.id[4] and self.id[5] and self.id[6].isdigit()  ==True:
                    print("Valid")
                else:
                    print("last 4 cases not valid")
            else:
                print("first 4 cases not valid")
        else:
            print("length not valid")
    def validate_name(self):
        if len(self.name)>=2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Valid name")
        else:
            print("Not valid")
    def validate_grade(self):
        if self.grade[0].isdigit()==False:
            print("Invalid")
        number=int(self.grade.split(' ')[0])
        string=self.grade.split(' ')[1:3]
        
        if number<1 and number> 12:
                print("Invalid")
        else:
            if number==1 and  string=="st":
                print("vaLID")
                print(str(number)+string+"Grade")
            if number==2 and string=="nd":
               print("vaLID")
               print(str(number)+string+"Grade")
            if number==3 and string=="rd":
               print("vaLID")
               print(str(number)+string+"Grade")
            if number>3 and string=="th":
               print("vaLID")
               print(str(number)+string+"Grade")
        
            
        
            
            

    def display(self):
        print(self.id)
        print(self.name)
        PRINT(SELF.GRADE)
       
s=Student()
s.validate_id()
s.validate_name()
s.validate_grade()
s.display()
