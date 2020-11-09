# from Cart import values


class Cart:
    pass


class NoProductInCard(Exception):
    def __init__(self, item):
        self.item = item


class InCart:
    def __init__(self, item):
        if item not in Cart.values:
            raise NoProductInCard(f"This product not in the cart!")
        self.__item = item

    @property
    def item(self):
        return self.__item
