#1.Scenario: Food Delivery System
#Create a system where:
#• Restaurant handles the menu and food preparation.• Delivery manages the delivery details and rider information.• Order combines both Restaurant and Delivery to process food orders 
and manage delivery logistics
class Library:
    def __init__(self,library_name,library_address):
        self.library_name=library_name
        self.library_address=library_address
    def displayLibraryinfo(self):
        print(f"Name of Library:{self.library_name}\nLibrary Address:{self.library_address}")
class Members:
    def __init__(self,member_name,member_contact):
        self.member_name=member_name
        self.member_contact=member_contact
    def displaymembersinfo(self):
        print(f"Name of Members:{self.member_name}\nMember Contact:{self.member_contact}")
class Librarymanagement(Library,Members):
    def __init__(self,library_name,library_address,member_name,member_contact):
        super().__init__(library_name,library_address)
        Members.__init__(self,member_name,member_contact)
    def display(self):
        self.displayLibraryinfo()
        self.displaymembersinfo()
lib=Librarymanagement("A to Z","No.59,Kamber Street","Rickshi",9094563354)
lib.display()

#2.Scenario: Food Delivery System
 #Create a system where:
#  • Restaurant handles the menu and food preparation.  • Delivery manages the delivery details and rider information. • Order combines both Restaurant and Delivery to process food orders 
and manage delivery logistics
class Restaurant:
    def __init__(self,Restaurant_name,Items):
        self.Restaurant_name=Restaurant_name
        self.Items=Items
    def displayrestaurantInfo(self):
        print(f"Name of the Restaurant:{self.Restaurant_name}\nItems Available:{self.Items}")
class Delivery:
    def __init__(self,Deliveryboy_name,boy_contact):
        self.Deliveryboy_name=Deliveryboy_name
        self.boy_contact=boy_contact
    def displaydelieryinfo(self):
        print(f"Name of the delivery Boy:{self.Deliveryboy_name}\nBoy's COntact:{self.boy_contact}")
class Order(Restaurant,Delivery):
    def __init__(self,Restaurant_name,Items,Deliveryboy_name,boy_contact):
        super().__init__(Restaurant_name,Items)
        Delivery.__init__(self,Deliveryboy_name,boy_contact)
    def display(self):
        self.displayrestaurantInfo()
        self.displaydelieryinfo()
Del=Order("ABC Kitchen","Idly,Dosa,Poori,Chappthi","Rakshan",8072688557)
Del.display()
