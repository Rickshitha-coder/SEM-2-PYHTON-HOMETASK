from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
    @abstractmethod
    def welcome(self):
        pass

    @abstractmethod
    def test_data(self, name):
        pass

    @abstractmethod
    def count_vowels(self, name):
        pass

    @abstractmethod
    def calculate_grade(self, name, mark1, mark2):
        pass
class Student(AbstractClassExample):
    def welcome(self):
        print("Welcome To WTS! WewishyoutheBest!")
    def test_data(self,name):
        self.name=name
        print(f"Welcome {self.name} ! Have a nice day!")
    def count_vowels(self,name):
        vowels = 'aeiou'
        count = 0
        vowel_counts = {}
        for char in self.name.lower():
            if char in vowels:
                count += 1
                vowel_counts[char] = vowel_counts.get(char, 0) + 1
        print(f"Count of Vowels are : {count}")
        for vowel, count in vowel_counts.items():
            print(f"{vowel} : {count}")
    def calculate_grade(self,name,mark1,mark2):
        self.anme=name
        self.mark1=mark1
        self.mark2=mark2
        self.tot=mark1+mark2
        print("Total Marks:",{self.tot})
        if self.tot>95:
            print("Grade E")
        elif self.tot>=80:
            print("Grade A+")
        elif self.tot>=75:
            print("Grade A")
        elif self.tot>60 and self.tot<=50:
            print("Grade B")
        else:
            print("Grade F")
        
class PasswordPrinter:
    def print_password(self, password):
        for char in password:
            if char.isdigit():
                break
            else:
                print(char, end='')

    def print_password_skip_numerics(self, password):
        for char in password:
            if not char.isdigit():
                print(char, end='')




student = Student()
student.welcome()
name = input("Please input a name : ")
student.test_data(name)
student.count_vowels(name)
mark1 = float(input("Please input mark1 : "))
mark2 = float(input("Please input mark2 : "))
student.calculate_grade(name, mark1, mark2)
password_printer = PasswordPrinter()
password = input("Enter Your Password: ")
print("Your Output will Break here")
password_printer.print_password(password)
print("\n","Your output will Continue")
password_printer.print_password_skip_numerics(password)





        
