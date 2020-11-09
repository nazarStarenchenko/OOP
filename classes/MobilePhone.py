from abc import ABC
from HasDisplay import HasDisplay
from HasCamera import HasCamera

class MobilePhone(HasDisplay, HasCamera):
    # __NumberOfSimCards = 0

    def __init__(self, NumberOfSimCards):
        self.__NumberOfSimCards = NumberOfSimCards
        super(HasDisplay, HasCamera, self).__init__() #??
    def getx(self):
        return self.__NumberOfSimCards
    def setx(self, value):
        self.__NumberOfSimCards = value

