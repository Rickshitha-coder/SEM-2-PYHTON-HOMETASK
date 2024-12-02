class Library:
    def __init__(self,library_name,library_address):
        self.library_name=library_name
        self.library_address=library_address
    def displayLibraryinfo(self):
        print(f"Name of Library:{library_name}\nLibrary Address:{library_address}")
class Members:
    def __init__(self,member_name,member_contact):
        self.member_name=member_name
        self.member_contact=member_contact
    def displaymembersinfo(self):
        print(f"Name of Members:{member_name}\nMember Contact:{member_contact}")
class Librarymanagement(Library,Members):
    def __init__(self,library_name,library_address,member_name,member_contact):
        super().__init__(library_name,library_address)
        Members.__init__(self,member_name,member_contact)
    def display(self):
        self.displayLibraryinfo()
        self.displaymembersinfo()
lib=Librarymanagement("A to Z","No.59,Kamber Street","Rickshi",9094563354)
lib.display()
