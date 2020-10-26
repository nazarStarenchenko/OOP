from abc import ABC
from HasDisplay import HasDisplay
class Monitor(HasDisplay):
    def __init__(self, Backlight, Interfaces):
        self.__mBacklight = Backlight
        self.__mInterfaces = Interfaces
        super().__init__()

    def setBacklight(self, Backlight):
        self.__mBacklight = Backlight

    def getBacklight(self):
        return self.__mBacklight

    def setInterfaces(self, Interfaces):
        self.__mInterfaces = Interfaces

    def getInterfaces(self):
        return self.__mInterfaces




