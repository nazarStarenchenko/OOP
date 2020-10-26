from HasDisplay import HasDisplay
from HasCamera import HasCamera

class Laptop(HasCamera, HasDisplay):

    def __init__(self, batteryCapacity):
        self.__batteryCapacity = batteryCapacity
        super().__init__()

    @property
    def batteryCapacity(self):
        return self.__batteryCapacity

    @batteryCapacity.setter
    def batteryCapacity(self, mBatteryCapacity):
        self.__batteryCapacity = batteryCapacity