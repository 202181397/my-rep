from enum import Enum  # import enum


class RoomFeatures(Enum):  # we create class with categories for enum data
    NO_SMOKING = 1
    DESK = 2
    SAFE = 3
    COFFEE_MAKER = 4
    HAIR_DRYER = 5


class User:  # user class
    def __init__(self, firstname, lastname, email, password):  # contructor to initalize user instance
        self.__firstname = firstname
        self.__lastname = lastname  # attributes of user class
        self.__email = email
        self.__password = password

    # setter and getter functions for each attribute
    def setFirstname(self, firstname):
        self.firstname = firstname

    def getFirstname(self):
        return self.firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def getLastname(self):
        return self.lastname

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.Email

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def __str__(self):  # str function so objects can be readable
        return f"User: {self.__firstname} {self.__lastname}, Email: {self.__email}"


class Reservation:  # reservation class
    def __init__(self, checkindate, checkoutdate, numberofnights,
                 numberofrooms):  # contructor to intialize reservation instance
        self.__checkindate = checkindate  # attrbutes of reservation class
        self.__checkoutdate = checkoutdate
        self.__numberofnights = numberofnights
        self.__numberofrooms = numberofrooms

        # setter and getter functions for each reservation class attribute

    def setCheckindate(self, checkindate):
        self.checkindate = checkindate

    def getCheckindate(self):
        return self.checkindate

    def setCheckoutdate(self, checkoutdate):
        self.checkoutdate = checkoutdate

    def getCheckoutdate(self):
        return self.checkoutdate

    def setNumberofnights(self, numberofnights):
        self.numberofnights = numberofnights

    def getNumberofnights(self):
        return self.numberofnights

    def setNumberofrooms(self, numberofrooms):
        self.numberofrooms = numberofrooms

    def getNumberofrooms(self):
        return self.numberofrooms

    def __str__(self):  # str function so the objects can be readable
        return f"Reservation: Check-in {self.__checkindate}, Check-out {self.__checkoutdate}, Nights: {self.__numberofnights}, Rooms: {self.__numberofrooms}"


class Room:  # room class
    def __init__(self, roomnumber, roomtype, roomfeatures):  # contructor to intialize room instance
        self.__roomnumber = roomnumber  # attributes of room class
        self.__roomtype = roomtype
        self.__roomfeatures = roomfeatures

        # setter and getter functions for room class atributes

    def setRoomnumber(self, roomnumber):
        self.roomnumber = roomnumber

    def getRoomnumber(self):
        return self.roomnumber

    def setRoomtype(self, roomtype):
        self.roomtype = roomtype

    def getRoomtype(self):
        return self.roomtype

    def setRoomfearures(self, roomfeatures):
        self.roomfeatures = roomfeatures

    def getRoomfeatures(self):
        return self.roomfeatures

    def __str__(self):  # str function
        features = ', '.join([f.name.replace('_', ' ') for f in self.__roomfeatures])
        return f"Room Number: {self.__roomnumber}, Type: {self.__roomtype}, Features: {features}"


class Hotel:  # hotel class
    def __init__(self, hotelname, hoteladdress, hotelphone):  # contructor to intialize hotel
        self.__hotelname = hotelname  # attributes of hotel class
        self.__hoteladdress = hoteladdress
        self.__hotelphone = hotelphone

        # setter and getter functions of hotel class attribiutes

    def setHotelname(self, hotelname):
        self.hotelname = hotelname

    def getHotelname(self):
        return self.hotelname

    def setHoteladdress(self, hoteladdress):
        self.hoteladdress = hoteladdress

    def getHoteladdress(self):
        return self.hoteladdress

    def setHotelphone(self, hotelphone):
        self.hotelphone = hotelphone

    def getHotelphone(self):
        return self.hotelphone

    def __str__(self):
        return f"Hotel: {self.__hotelname}, Address: {self.__hoteladdress}, Phone: {self.__hotelphone}"

        # here we create objects for each class


user1 = User("Ted", "Vera", "tedvera@mac.com", "tedvera123")
Reservation1 = Reservation("Sun, Aug22, 2010-3:00PM", "Tue, Aug24, 2010-12:00PM", "2", "1")
Room1 = Room("Room1", "2 Queen Beds",
             [RoomFeatures.NO_SMOKING, RoomFeatures.DESK, RoomFeatures.SAFE, RoomFeatures.COFFEE_MAKER,
              RoomFeatures.HAIR_DRYER])
HotelInn = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinty Drive Los Almos, NM 87544", 5056611110)

print(user1)  # we print the objects
print(Reservation1)
print(Room1)
print(HotelInn)