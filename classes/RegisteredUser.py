from classes.Helpers import Helpers
from classes.RegularUser import RegularUser

class RegisteredUser(RegularUser):

    def __init__(self):
        super().__init__()


    def setFieldsAndReturnDataDict(self):
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

        

