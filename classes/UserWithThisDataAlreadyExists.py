from Helpers import Helpers

class UserWithThisDataAlreadyExists(Exception):
	def __init__(self, dataToWrite, listOfAllData):
		self.__dataToWrite = dataToWrite
		self.__listOfAllData = listOfAllData
		super().__init__()

		def enterRightData(self):
			while self.__dataToWrite in self.__listOfAllData:
				print("enter data that is not in data base!")
				__dataToWrite = Helpers.getDataFromUser()

			return __dataToWrite