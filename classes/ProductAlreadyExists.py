

class ProductAlreadyExists:
	def __init__(self):
		self.items = [...]


    def __contains__(self, l:list):
        if l in self.items:
            raise IndexError('Item already exists')
            del list.index(l)
