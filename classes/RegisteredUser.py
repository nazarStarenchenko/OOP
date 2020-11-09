from User import User
from Helpers import Helpers
from RegularUser import RegularUser

class RegisteredUser(RegularUser):

    def __init__(self):
        super().__init__()


    def addToDataBaseAndSetFields(self):
        dataDict = Helpers.getDataFromUser()

        #set fields
        self.email = dataDict["email"]
        self.password = dataDict["password"] 
        self.name = dataDict["name"]
        self.age = dataDict["age"] 
        self.cardPassword = dataDict["cardPassword"]
        self.cardNumber =  dataDict["cardNumber"] 
        self.cvv =  dataDict["cvv"] 
        self.cardDateYear = dataDict["cardDateYear"] 
        self.cardDateMonth = dataDict["cardDateMonth"] 

        #write into the file
        file = open('../../userBase.txt', 'a+') 
        file.write(str(dataDict)+ "\n") 
        file.close()

