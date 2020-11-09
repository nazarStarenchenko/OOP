<<<<<<< HEAD
from abc import ABC, abstractmethod, metaclass
from Cart import Cart
from Collection import Collection
from ItemsCollection import ItemsCollection


class CartAdder(ABC):
    @abstractmethod
    def addElementToTheCart(self, key, cart):
        if not isinstance(key, int): # якщо ключ не ціле число raise
            ProtectedDictIntError( ProtectedDictIntError.NON_INTEGER_KEY, "NON_INTEGER_KEY")
        if 0 <= key < len(self.cart):
            self.cart[key] = value
            self.cart.append(value)
        else:
            raise IndexError('index out of range')

    @abstractmethod
    def pickItemFromTheCart(self, key, cart):
        if not isinstance(key, int):  # якщо ключ не ціле число raise
            ProtectedDictIntError(ProtectedDictIntError.NON_INTEGER_KEY, "NON_INTEGER_KEY")
        if 0 <= key < len(self.cart):
            self.cart.pop(key)
        else:
            raise IndexError('index out of range')
=======
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
>>>>>>> 21302021fa5fa1fa7ef5627e0e2971ef338254f5
