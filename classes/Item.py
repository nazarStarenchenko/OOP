from abc import ABC

class Item(ABC):

    def init(self, *args):
        self.values = list(args)

    def repr(self):
        return str(self.values)

    for i in *args:
        print(*args[0], 'cost', *args[1], 'has number', *args[2], 'with discount', *args[3],
              'weight,width,height,length,color=', *args[4], *args[5], *args[6], *args[7],
             ';Amount:', *args[8])

