from abc import ABC

class User(ABC):

    def __init__(self):
        self.__name = "" 
        self.__email = ""
        self.__password = "" 

    @property
    def name(self):
        return self.__name
     
    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @name.setter
    def name(self, name):
        self.__name = name

    @email.setter
    def email(self, email):
        self.__email = email

    @password.setter
    def password(self, password):
        self.__password = password