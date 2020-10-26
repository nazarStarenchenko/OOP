from abc import ABC


class Collection(ABC):
    pass


class ItemCollection(Collection):
    __allItems = []

    def __init__(self, _list):
        self._list = list

    def __setitem__(self, key, value):
        self._list[key] = value

    def __getitem__(self, key):
        return self._list[key]
