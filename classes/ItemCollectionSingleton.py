from classes.Singleton import Singlemeta


class ItemCollectionSingleton(metaclass=Singlemeta):

    def __init__(self):
        self.__listOfContent = []
    
    def getAllFromDataBase(self):
        file = open('itemBase.txt', 'r')
        self.__listOfContent = file.readlines() 
        file.close()
        for i in range(0, len(self.__listOfContent)):
            self.__listOfContent[i] = eval(self.__listOfContent[i][:-1])

    def addToFile(self):
        file = open('itemBase.txt', 'w')
        for l in self.__listOfContent:
            file.write(str(l)+"\n")
        file.close()

    @property
    def listOfContent(self):
        return self.__listOfContent

    @listOfContent.setter
    def listOfContent(self, l):
        self.__listOfContent = l
   
if __name__ == "__main__":

    a = ItemCollectionSingleton()
    a.getAllFromDataBase()

    b = ItemCollectionSingleton()
    b.getAllFromDataBase()

    print(a,b)
    print(a == b)
    