from abc import ABC , abstractmethod

class Collection(ABC):
    @abstractmethod
    def getAllFromDataBase(self):
    	pass
        
