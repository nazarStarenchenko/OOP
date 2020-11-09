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
        cardPassword = int(input("enter your password: "))
        while len(cardPassword) != 4:
            print("enter 4 digit number")
            cardPassword = int(input("enter your password: "))    
        return password

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
        file = open('../../adminBase.txt', 'r') 
        f1 = file.readlines()
        for row in f1:
            dictRow = eval(row)
            if email == dictRow["email"] or password == dictRow["password"]:
                return dictRow 
        file.close()

               
        #opening and working with lines in user base
        file = open('../../userBase.txt', 'r') 
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
        
