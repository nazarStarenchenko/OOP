from abc import ABC
import re
import time

class Helpers(ABC):
    @staticmethod
    def getEmailFromUser():
        pattern = r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        address = input('enter email address: ')
        while(re.match(pattern , address) == None):
            print("enter something like this: 'example@email.com' ")
            address = input('enter email address: ')
        return address

    @staticmethod
    def getPasswordFromUser():
        password = input("enter your password: ")
        return password
        
    @staticmethod
    def getCardPasswordFromUser():
        cardPassword = int(input("enter your card password: "))
        while len(str(cardPassword)) != 4:
            print("enter 4 digit number")
            cardPassword = int(input("enter your card password: "))    
        return cardPassword

    @staticmethod
    def getMonthFromUser():
        number = int(input("enter month of your card (number between 1 and 12): "))
        while number < 1 or number > 12:
            number = int(input("enter month of your card (number between 1 and 12): "))
        
        return number

    @staticmethod
    def getYearFromUser():
        currentYear = int(time.strftime("%y", time.localtime()))
        number = int(input("enter year of your card (number that bigger then {}): ".format(currentYear)))
        while number < currentYear:
            number = int(input("enter year of your card (number that bigger then {}): ".format(currentYearcardNumber = Helpers.getNumberFromUser(1))))
        return number

    @staticmethod
    def getNumberFromUser(length, text):

        number = input(text)
        while(len(number) != length):
            if length == 12:
                print("enter 12 digit number")
            if length == 3:
                print("enter 3 digit number")
            
            number = input(text)
        return number

    @staticmethod
    def logger():
        #getting password and email form user
        email = Helpers.getEmailFromUser()
        password = Helpers.getPasswordFromUser()
        #opening user base
        
        #opening admin base and working with it
        file = open('adminBase.txt', 'r') 
        f1 = file.readlines()
        for row in f1:
            dictRow = eval(row)
            if email == dictRow["email"] or password == dictRow["password"]:
                return dictRow 
        file.close()

               
        #opening and working with lines in user base
        file = open('userBase.txt', 'r') 
        f1 = file.readlines()
        for row in f1:
            dictRow = eval(row)
            if email == dictRow["email"] or password == dictRow["password"]:
                return dictRow 
        file.close()

    @staticmethod
    def getDataFromUser():
        
        email = Helpers.getEmailFromUser()
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        password = Helpers.getPasswordFromUser()
        cardNumber = Helpers.getNumberFromUser(12, "enter 12 digit card number: ")
        cvv = Helpers.getNumberFromUser(3, "enter 3 digit cvv number: ")
        cardDateYear = Helpers.getYearFromUser()
        cardDateMonth = Helpers.getMonthFromUser()
        cardPassword = Helpers.getCardPasswordFromUser()
        dataDict =  {"email": email, "name": name, "age": age, "password": password, 
                    "cardNumber": cardNumber, "cvv":cvv, "cardDateMonth": cardDateMonth,
                    "cardDateYear": cardDateYear, "cardPassword": cardPassword}

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
