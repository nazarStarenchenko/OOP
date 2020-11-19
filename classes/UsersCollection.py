from abc import ABC
from classes.Collection import  Collection


class UsersCollection(Collection):
    
    def __init__(self):
        self.__listOfContent = []
	
    def getAllFromDataBase(self):
    	file = open('userBase.txt', 'r')
    	self.__listOfContent = file.readlines() 
    	file.close()
        for i in range(0, len(self.__listOfContent)):
            self.__listOFContent[i] = eval(self.__listOFContent[i][:-1])

    def addToFile(self):
        file = open('userBase.txt', 'w')
        file.write(str(__listOfContent)+ "\n")
        file.close()

    @property
    def listOfContent(self):
    	return self.__listOfContent
 
    @listOfContent.setter
    def listOfContent(self, l):
        self.__listOfContent = l
