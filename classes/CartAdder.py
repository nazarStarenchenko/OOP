from abc import ABC, abstractmethod, metaclass

class Collection(ABC):
    pass
class Cart():
    pass
class ItemsCollection(Collection):
    pass

# cart = [1, 2, 3, 4, 5]

class CartAdder(ABC):
    @abstractmethod
    def addElementToTheCart(self, key, cart):
        pass
    @abstractmethod
    def pickItemFromTheCart(self, key, cart):
        pass