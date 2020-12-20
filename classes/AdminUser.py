from classes.DataBaseAdderAndDeleter import DataBaseAdderAndDeleter
from classes.Helpers import Helpers
from classes.User import User
from classes.ItemCollectionSingleton import ItemCollectionSingleton

class AdminUser(User, DataBaseAdderAndDeleter):
	
	def __init__(self):
		super().__init__()

	def SetFields(self, dataDict): 
		self.name = dataDict["name"]
		self.email = dataDict["email"]
		self.password = dataDict["password"]


	def addElementToBase(self, listOfElements : list, typeOfBase: str):
		if typeOfBase == "item":
			#working with items collection
			data = Helpers.getItemFields()
			while data in listOfElements:
				print("enter data that is not in base")
				data = Helpers.getItemFields()
			listOfElements.append(data)

		elif typeOfBase == "user":
			#working with users colleciton
			data = Helpers.getDataFromUser()
			while data in listofelements:
				print("enter data that is not in base")
				data = Helpers.getDataFromUser()
			listOfElements.append(data)

		return listOfElements


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

