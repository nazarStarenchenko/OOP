from ComputerLike import ComputerLike
from abc import ABC

class HasCamera(ComputerLike, ABC):
    def init(self, name, resolution, fps):
        self._name = name
        self._resolution = resolution
        self._fps = fps

    @property
    def my_resolution(self):
        return self._resolution

    @property
    def my_fps(self):
        return self._fps

    @my_resolution.setter
    def my_resolution(self, value):
        if isinstance(value, (int, float)):
            self._resolution = value
        else:
            raise ValueError('Expecting only values')

    @my_fps.setter
    def my_fps(self, speed):
        if isinstance(speed, (int, float)):
            self._fps = speed
        else:
            raise ValueError('Expecting only values')

    @my_resolution.deleter
    def my_resolution(self):
        del self._resolution

    @my_fps.deleter
    def my_fps(self):
        del self._fps
