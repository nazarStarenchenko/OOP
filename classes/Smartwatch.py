from abc import ABC
from HasDisplay import HasDisplay

class SmartWatch(HasDisplay):
    def __init__(self, WaterResistance, BraceletMaterial):
        self.__mWaterResistance = WaterResistance
        self.__mBraceletMaterial = BraceletMaterial
        super().__init__()

    def setWaterResistance(self, WaterResistance):
        self.__mWaterResistance = WaterResistance

    def getWatreResistance(self):
        return self.__mWaterResistance

    def setBraceletMaterial(self, BraceletMaterial):
        self.__mBraceletMaterial = BraceletMaterial

    def getBraceletMaterial(self):
        return self.__mBraceletMaterial
