from abc import ABC, abstractmethod, metaclass
from Cart import Cart

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