from ComputerLike import ComputerLike

class PC(ComputerLike):
    def __init__(self, hasDisplay):
        self.__mHasDisplay = hasDisplay
        super().__init__()

    def sethasDisplay(self, hasDisplay):
        self.__mHasDisplay = hasDisplay

    def gethasDisplay(self):
        return self.__mHasDisplay



