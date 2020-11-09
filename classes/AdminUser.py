from DataBaseAdderAndDeleter import DataBaseAdderAndDeleter
from Helpers import Helpers
from User import User
from UserWithThisDataAlreadyExists import UserWithThisDataAlreadyExists

class AdminUser(User, DataBaseAdderAndDeleter):
	
	def __init__(self):
		super().__init__()

	def SetFields(self, dataDict): 
		self.name = dataDict["name"]
		self.email = dataDict["email"]
		self.password = dataDict["password"]
       	
	def __getItemFields(self):

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
		valueDict["width"] =	 float(input("enter width: "))
		valueDict["height"] = float(input("enter heigth: "))
		valueDict["length"] = length(input("enter length: "))
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
				valueDict["batteryCapacity"] = float("enter batary capacity in Wh: ")

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


	def addElementToBase(self, listOfElements : list):
		if len(l[0].keys()) > 9:
			#working with items collection
			data = __getItemFields()
			listOfElements.append(data)
		else: 
			#working with users colleciton
			data = Helpers.getDataFromUser()
			try:
				for el in listOfElements:
					if data in listOfElements:
						raise UserWithThisDataAlreadyExists(data, listOfElements)
			except UserWithThisDataAlreadyExists as e:
				data = e.enterRightData()	
				
			listOfElements.append(data)


	def deleteElementsFromBase(self, l: list):
		if len(l[0].keys()) > 9:
			name = input("enter name of item you want to delete")
			for i in range(len(l)):
				if l[i]["name"] == name:
					del l[i]
		else:
			email = Helpers.getEmailFromUser()
			for i in range(len(l)):
				if l[i]["email"] == email:
					del l[i]	
	


ad = AdminUser()
l = [{"email": "ana"}]
ad.addElementToBase(l)