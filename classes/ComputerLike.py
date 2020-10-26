from abc import ABC

class Item:
    pass


class ComputerLike(ABC, Item):
    
   def __init__(self, CPU, GPU, Memory):
        self.__CPU = CPU
        self.__GPU = GPU
        self.__Memory = Memory

    def getCPU(self):
        return self.__CPU
    def getGPU(self):
        return self.__GPU
    def getMemory(self):
        return self.__Memory

    def setCPU(self, value):
        self.__CPU = value
    def setGPU(self, value):
        self.__GPU = value
    def setMemory(self, value):
        self.__Memory = value

