from abc import ABC, abstractmethod 
from classes.Cart import Cart


class CartAdder(ABC):
    @abstractmethod
    def addElementToCart(self):
        pass
    @abstractmethod
    def delElementFromCart(self):
        pass