list=[]


class ProductAlreadyExists:
    def __delitem__(self, l):
        if l in list:
            raise IndexError('Item already exists')
            del list.index(l)
