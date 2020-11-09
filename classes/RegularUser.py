from abc import ABC
from User import User

class RegularUser(User, ABC):
    def __init__(self):
        super().__init__()
        self.__age = 0
        self.__cardNumber = 0
        self.__cvv = 0
        self.__cardDateMonth = 0
        self.__cardDateYear = 0
        self.__cardPassword = 0
        

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def cardNumber(self):
        return self.__cardNumber

    @cardNumber.setter
    def cardNumber(self, value):
        self.__cardNumber = value

    @property
    def cvv(self):
        return self.__cvv
    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @property
    def cardDateMonth(self):
        return self.__cardDateMonth

    @cardDateMonth.setter
    def cardDateMonth(self, value):
        self.__cardDateMonth = value

    @property
    def cardDateYear(self):
        return self.__cardDateYear

    @cardDateYear.setter
    def cardDateYear(self, value):
        self.__cardDateYear = value

    @property
    def cardPassword(self):
        return self.__cardPassword
        
    @cardPassword.setter
    def cardPassword(self, value):
        self.__cardPasswordr = value


