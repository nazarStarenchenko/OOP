from classes.Helpers import Helpers
from classes.User import User
from classes.RegularUser import RegularUser

class LoginUser(RegularUser):

    def __init__(self):
        super().__init__()


    def SetFields(self, dataDict):

        dataDict = Helpers.logger()

        self.email = dataDict["email"]
        self.password = dataDict["password"]    
        self.name = dataDict["name"] 
        self.age =  dataDict["age"] 
        self.cardPassword = dataDict["cardPassword"]
        self.cardNumber = dataDict["cardNumber"] 
        self.cvv = dataDict["cvv"] 
        self.cardDateYear = dataDict["cardDateYear"] 
        self.cardDateMonth = dataDict["cardDateMonth"]

