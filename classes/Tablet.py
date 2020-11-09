from HasDisplay import HasDisplay
from HasCamera import HasCamera

class Tablet(HasDisplay, HasCamera):

    def __init__(self, hasSimCard):
        self.__hasSimCard = hasSimCard
        super(HasDisplay, HasCamera, self).__init__() 

    @property
    def hasSimCard(self):
        return self.__hasSimCard

    @hasSimCard.setter
    def hasSimCard(self, value):
        self.__hasSimCard = value
