from abc import ABC
from ComputerLike import ComputerLike

class HasDisplay(ComputerLike, ABC):
    def __init__(self, displayName,displaySize,displayResolution,matrixType,displayFPS):
        self.__DisplayName = displayName
        self.__DisplaySize = displaySize
        self.__DisplayResolution = displayResolution
        self.__MatrixType = matrixType
        self.__DisplayFPS = displayFPS

    def setDisplayName(self, displayName):
        self.__mDisplayName = displayName

    def getDisplayName(self):
        return self.__DisplayName

    def setDisplaySize(self, displaySize):
        self.__mDisplaySize = displaySize

    def getDisplaySize(self):
        return self.__mDisplaySize

    def setDisplayResolution(self, displayResolution):
        self.__mDisplayResolution = displayResolution

    def getDisplayResolution(self):
        return self.__mDisplayResolution

    def setMatrixType(self, matrixType):
        self.__mDisplayResolution = matrixType

    def getMatrixType(self):
        return self.__mMatrixType

    def setDisplayFPS(self, displayFPS):
        self.__mDisplayFPS = displayFPS

    def getDisplayFPS(self):
        return self.__mDisplayFPS