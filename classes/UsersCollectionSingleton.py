from classes.Singleton import Singlemeta


class UsersCollectionSingleton(metaclass=Singlemeta):
    
    def __init__(self):
        self.__listOfContent = []
        self.getAllFromDataBase()
	
    def getAllFromDataBase(self):
        file = open('userBase.txt', 'r')
        self.__listOfContent = file.readlines() 
        file.close()
        for i in range(0 ,len(self.__listOfContent)):
            self.__listOfContent[i] = eval(self.__listOfContent[i][:-1])

    def appendToUserCollection(dictToAppend: dict):
        self.__listOfContent.append(dictToAppend)

    def addToFile(self):
        file = open('userBase.txt', 'w')
        for i in range(0, len(self.__listOfContent)):
            file.write(str(self.__listOfContent[i])+ "\n")
        file.close()

    @property
    def listOfContent(self):
    	return self.__listOfContent
 
    @listOfContent.setter
    def listOfContent(self, l):
        self.__listOfContent = l
