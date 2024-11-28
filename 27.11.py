'''#1 Given students details, marks in 5 subjects and we have to find student's grade.In this program, you have to take student name, roll number and marks in 3 subjects and calculating student's grade based on the percentage and printing the all details.
student_name=input("Enter the Student Name:")
student_rollno=int(input("Enter The Roll No:"))
a=int(input("Enter The Mark In Tamil:"))
b=int(input("Enter The Mark In English:"))
c=int(input("Enter The Mark In Maths:"))
d=int(input("Enter The Mark In Science:"))
e=int(input("Enter The Mark In Social:"))
total=a+b+c+d+e
percentage=total/5
print(f"Total Percentage Scored:{percentage}%")
if percentage>=85:
    print(f"Your Grade is S")
elif percentage>=75:
    print("Grade A")
elif percentage>=65:
    print("Grade B")
elif percentage>=55:
    print("Grade C")
elif percentage>=50:
    print("Grade D")
else:
    print("Grade E")
  #or
  '''
class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def calculate_per(self):
        total=self.mark1+self.mark2+self.mark3
        percentage=(total/300)*100
        return percentage
    def display_percentage(self):
        percentage=self.calculate_per()
        print(f"your percentage is {percentage}")
    def grade(self):
        percentage=self.calculate_per()
        if percentage>=85:
            print("your grade is S")
        elif percentage>=75 and percentage <=85:
            print("your grade is A")
        
        elif percentage>=65 and percentage <=75:
            print("your grade is B")
        elif percentage>=55 and percentage <=65:
            print("your grade is C")
        elif percentage>=50 and percentage <=55:
            print("your grade is D")
s=Student("Harini","E24AI012",90,91,86)
s.calculate_per()
s.display_percentage()
s.grade()
#2. Implement destructor and constructors using __del__() and __init__() to display student information.
class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def show(self):
        print(f"student Details-->Student Name {self.name},Student Age {self.age},Student Course {self.course},Student Grade {self.grade}")
    def __del__(self):
        print("ALL Details Are Deleted")
stu1=Student("Rickshi",18,"AI","A")
stu1.show()
del stu1
