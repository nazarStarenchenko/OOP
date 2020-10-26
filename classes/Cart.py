class Cart:

    def init(self, *args):
        self.values = list(args)

    def repr(self):
        return str(self.values)

    def getitem(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Index out of range')

    def setitem(self, key, value):  # a = Item([1],[2],[3],[4],[5],[6],[7],[8],[9],[10])
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Index out of range')

    def delitem(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index out of range')

