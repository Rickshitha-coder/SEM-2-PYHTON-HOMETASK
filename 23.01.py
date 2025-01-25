'''Create a Python class HotelRoom to manage details of a hotel room. The class should have the 
following:
Attributes:
A private attribute __room_number (an integer).
A private attribute __is_occupied (a boolean to indicate if the room is occupied).
A private attribute __rate_per_night (a float to store the rate for the room).
Methods:
A getter and setter for room_number with validation to ensure it is always a positive integer.
A getter and setter for rate_per_night with validation to ensure the rate is greater than zero.
A method check_in() to mark the room as occupied. Raise an exception if the room is already 
occupied.
A method check_out() to mark the room as unoccupied. Raise an exception if the room is already 
vacant.
A method display_details() to print the room details in the format:
Input:
# Create a room instance
room = HotelRoom()
# Set room details
room.set_room_number(101)
room.set_rate_per_night(200.50)
# Display details
room.display_details()
Output:
Room Number: 101
Rate per Night: $200.50
Occupied: No'''
class HotelRoom:
    def __init__(self):
        self.__room_number = None
        self.__is_occupied = True
        self.__rate_per_night = None

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        if not isinstance(room_number, int) or room_number <= 0:
            raise ValueError("Room number must be a number and positive integer")
        self.__room_number = room_number

    def get_rate_per_night(self):
        return self.__rate_per_night

    def set_rate_per_night(self, rate_per_night):
        if not isinstance(rate_per_night, (int, float)) or rate_per_night <= 0:
            raise ValueError("Rate per night must be anumber and  greater than zero")
        self.__rate_per_night = rate_per_night

    def get_occupation_status(self):
        return self.__is_occupied

    def check_in(self):
        if self.__is_occupied:
            raise Exception("Room is already occupied")
        self.__is_occupied = True

    def check_out(self):
        if not self.__is_occupied:
            raise Exception("Room is  vacant")
        self.__is_occupied = False

    def display_details(self):
        occupied_status = "Yes" if self.__is_occupied else "No"
        print(f"Room Number: {self.__room_number}")
        print(f"Rate per Night: ${self.__rate_per_night:.2f}")
        print(f"Occupied: {occupied_status}")

# Test the class
try:
    room = HotelRoom()
    room_no=int(input("Enter the room no:"))
    room.set_room_number(room_no)
    room_cost=int(input("Enter the amount of per night:"))
    room.set_rate_per_night(room_cost)
    room.display_details()
    
    room.check_in()


except Exception as e:
    print(e)







  
