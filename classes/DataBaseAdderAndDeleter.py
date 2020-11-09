from abc import ABC, abstractmethod


class DataBaseAdderAndDeleter(ABC,ProductAlreadyExists):
	@abstractmethod
	def addElementToBase(self, l: list):
		pass

	@abstractmethod
	def deleteElementsFromBase(self, l: list):
		pass
