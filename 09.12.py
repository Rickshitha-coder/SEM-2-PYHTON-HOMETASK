'''Multiple inheritance example - Imagine a Smartphone that combines features of a Camera and a 
Phone. Use multiple inheritance to implement the following.'''
class Camera:
 def __init__(self):
     self.resolution=input("Enter the resolution")
     self.Lens=input("Enter the Lens name")
 def display_camera(self):
     print("Resolution:",self.resolution)
     print("Lens Name:",self.Lens)
class Phone:
 def __init__(self):
     self.phone_no=int(input("Enter the phone number:"))
 def display_phone(self):
     print("Phone Number:",self.phone_no)
class SmartPhone(Camera,Phone):
 def __init__(self):
     Camera.__init__(self)
     Phone.__init__(self)
     self.brand=input("Enter the brand")
     self.model=input("Enter the model")
 def displaydevice(self):
     print("Model:",self.model)
     print("Brand:",self.brand)
     self.display_camera()
     self.display_phone()
s=SmartPhone()
s.displaydevice()

'''Single inheritance example - Student as the parent class, providing attributes and methods related 
to education (e.g., studentInfo()).'''
class Student:
 def __init__(self):
     self.name=input("Enter the student name")
     self.department=input("Enter the department:")

 def studentInfo(self):
     print("Student Name:",self.name)
     print("Department:",self.department)
 
class StudentAthelete(Student):
 def __init__(self):
     Student.__init__(self)
     self.sports_name=input("Enter the sports that student going to participate:")
 def atheletedetails(self):
     self.studentInfo()
     print("Sports Name:",self.sports_name)
s=StudentAthelete()
s.atheletedetails()
