'''Find the Longest Common Prefix in a Tuple of Strings
Sample input:
Flower
Flow
Flight
Sample Output:
Fl'''
def common_prefix(strs):
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len) #fly
    
    for i, char in enumerate(shortest_str): #0,f  1,l  2,y
        for other_str in strs: #fly-->f flower-->f flew-->f | fly-->l flower-->l flew-->l | fly-->y flower-->w flew-->e
            if other_str[i] != char: # y!=w
                return shortest_str[:i] #fl
    return shortest_str
strs=input("Enter the Elements in list:").split()  #fly flower flew

print(strs)

'''2. Create a program that models a Person class and a Student class that inherits from Person.
Base Class (Person):
The Person class defines the basic attributes of a person (name and age) and a method 
display_info() to display these details.
Derived Class (Student):
The Student class inherits from Person and adds two new attributes: student_id and course. 
It also overrides the display_info() method to include these new attributes while still calling 
the base class display_info() method using super().
Object Creation and Method Calls:
• person1 is an instance of the Person class and only displays the name and age.
• student1 is an instance of the Student class, which also displays the student's name, age, 
student ID, and course.'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    def display_info(self):
        super().display_info()
    print(f"Student ID: {self.student_id}")
    print(f"Course: {self.course}")
    print("Enter details for Person:")
name = input("Enter name: ")
age = input("Enter age: ")
person1 = Person(name, age)
print("\nEnter details for Student:")
name = input("Enter name: ")
age = input("Enter age: ")
student_id = input("Enter student ID: ")
course = input("Enter course: ")
student1 = Student(name, age, student_id, course)
print("\nPerson Details:")
person1.display_info()
print("\nStudent Details:")
student1.display_info()
