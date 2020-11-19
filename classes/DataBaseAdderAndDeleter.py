from abc import ABC, abstractmethod


class DataBaseAdderAndDeleter(ABC):
	@abstractmethod
	def addElementToBase(self, l: list, t: str):
		pass

	@abstractmethod
	def deleteElementsFromBase(self, l: list, t: str):
		pass
