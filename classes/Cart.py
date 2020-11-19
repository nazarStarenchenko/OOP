class Cart:

    def __init__(self):
        self.__cartList = []

    def confimOrder():
        print(
'''
Do you want to confim order?
1 - yes
2 - no
''')
        choice = int(input("enter your choice: "))
        if  choice == 1:
             return True 
        elif choice == 2:
            return False


    @property
    def cartList(self):
        return self.__cartList

    @cartList.setter
    def cartList(self, cart):
        self.__cartList = cart