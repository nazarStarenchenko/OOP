from abc import ABC
from Collection import  Collection


class UsersCollection(Collection):
    
    def __init__(self):
        self.__allUsers = []

    def getAllUsers(self, key):
        return	self.__allUsers 

    def setAllUsers(self, l):
        self.__allUsers = l



