from abc import ABC
import re
import time

class Helpers(ABC):
    @staticmethod
    def validEmailFromUser(email):
        pattern = r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        if(re.match(pattern , email) == None):
            return False
        else:
            return True
        
    @staticmethod
    def validCardPasswordFromUser(cardPassword):
        if len(str(cardPassword)) != 4:
            return False
        else:
            return True

    @staticmethod
    def validMonthFromUser(number):
        if number == '' or int(number) < 1 or int(number) > 12:
            return False 
        else:
            return True

    @staticmethod
    def validYearFromUser(number):
        currentYear = int(time.strftime("%y", time.localtime()))
        if number == '' or int(number) < currentYear:
            return False
        else:
            return True

    @staticmethod
    def logger(dictToCheck: dict):
        #getting password and email form user
        email = dictToCheck["login"]
        password = dictToCheck["password"]
        if Helpers.validEmailFromUser(email) == False:
            print("RETURN EMPTY DICT")
            return dict()
        else: 
            #opening and working with lines in user base
            file = open('userBase.txt', 'r') 
            f1 = file.readlines()
            for row in f1:
                dictRow = eval(row)
                if email == dictRow["email"] or password == dictRow["password"]:
                    print("RETURN FILLED DICT")
                    return dictRow 
            file.close()

    @staticmethod
    def getDataFromUser(dictToCheck: dict):
        email = Helpers.validEmailFromUser(dictToCheck["email"])
        cardDateYear = Helpers.validYearFromUser(dictToCheck["cardDateYear"])
        cardDateMonth = Helpers.validMonthFromUser(dictToCheck["cardDateMonth"])
        cardPassword = Helpers.validCardPasswordFromUser(dictToCheck["cardPassword"])
      
        if email == False or cardDateMonth == False or cardDateYear == False or cardPassword == False:
            return dict()
        else: 
            dataDict =  {"email": dictToCheck["email"], "name": dictToCheck["name"], "age": dictToCheck["age"], 
                        "password": dictToCheck["password"], "cardNumber": dictToCheck["cardNumber"], 
                        "cvv":dictToCheck["cvv"], "cardDateMonth": dictToCheck["cardDateMonth"],
                        "cardDateYear": dictToCheck["cardDateYear"], "cardPassword": dictToCheck["cardPassword"]}
            return dataDict
        

    @staticmethod
    def getItemFields():

        listOfTypesOfProducts = ["laptop", "PC", "mobile phone", "tablet", "monitor", "smart watch"]

        for i in range(len(listOfTypesOfProducts)):
            print("{}. {}".format(i+1, listOfTypesOfProducts[i]))

        typeOfObjToAdd = int(input("enter number of object listed before: "))

        while(typeOfObjToAdd > 6 or typeOfObjToAdd < 1):
            print("try one more time")
            typeOfObjToAdd = int(input("enter number of object listed before: "))   

        valueDict = dict()
        valueDict["name"] = input("enter name of product: ")
        valueDict["price"] = float(input("enter price of product: "))
        valueDict["number"] = int(input("enter number of product: "))
        valueDict["discount"] = int(input("enter discount: "))
        valueDict["weight"] = float(input("enter weigth: "))
        valueDict["width"] =     float(input("enter width: "))
        valueDict["height"] = float(input("enter heigth: "))
        valueDict["length"] = float(input("enter length: "))
        valueDict["color"] = input("enter color: ")
        valueDict["amountAvalible"] = int(input("enter amount avalible: "))

        #roiting choice of user
        if typeOfObjToAdd == 1 or typeOfObjToAdd == 4 or typeOfObjToAdd == 5 or typeOfObjToAdd == 6: 

            valueDict["displayName"] = input("enter display name: ")
            valueDict["displaySize"] = input("enter display size: ")
            valueDict["displayResolution"] = input("enter display resolution: ")
            valueDict["matrixType"] = input("enter matrix type: ")
            valueDict["displayFps"] = input("enter display fps: ")

            if typeOfObjToAdd == 1:
                valueDict["batteryCapacity"] = float(input("enter batary capacity in Wh: "))

            elif typeOfObjToAdd == 4:
                print("1 - tablet has sim card")
                print("2 - tablet has no sim card")
                choice = int(input("enter 1 or 2: "))
                if choice == 1:
                    valueDict["hasSimCard"] = True
                elif choice == 2:
                    valueDict["hasSimCard"] = False

            elif typeOfObjToAdd == 5:
                valueDict["backlight"] = input("enter kind of backlight: ")
                interfaceStr = input("enter type of interfaces with space between: ")
                interfaces = interfaceStr.split(" ")
                valueDict["interfaces"] = interfaces

            elif typeOfObjToAdd == 6:
                print("1 - watch has water resistance")
                print("2 - watch has no water resistance")
                choice = int(input("enter 1 or 2: "))
                if choice == 1:
                    valueDict["waterResistance"] = True
                elif choice == 2:
                    valueDict["waterResistance"] = False

        if typeOfObjToAdd == 2 or typeOfObjToAdd == 3:

            valueDict["GPU"] = input("enter GPU type: ")
            valueDict["CPU"] = input("enter CPU type: ")
            valueDict["memory"] = input("input type of memory: ")
            if typeOfObjToAdd == 2:
                print("1 - tablet has display")
                print("2 - tablet has no dislay")
                choice = int(input("enter 1 or 2: "))
                if choice == 1:
                    valueDict["hasDisplay"] = True
                elif choice == 2:
                    valueDict["hasDisplay"] = False
            elif typeOfObjToAdd == 3:
                valueDict["numberOfSimCards"] = int(input("enter number of sim cards"))

        if  typeOfObjToAdd == 3 or typeOfObjToAdd == 1 or typeOfObjToAdd == 4:
            valueDict["cameraResolution"] = input("enter camera resolution: ")
            valueDict["cameraFps"] = int(input("enter camera fps: "))


        return valueDict
