from classes.AdminUser import AdminUser
from classes.RegisteredUser import RegisteredUser
from classes.LoginUser import LoginUser

from classes.UsersCollection import UsersCollection
from classes.ItemCollection import ItemCollection

from classes.Displayer import Displayer
from  classes.Helpers import Helpers

from classes.Cart import Cart


uc = UsersCollection()
uc.getAllFromDataBase()

ic = ItemCollection()
ic.getAllFromDataBase()

displayer = Displayer()
'''
print("""
\nYou want to loggin or register?
1 - login
2 - register

""")
choice = int(input("enter your choice: "))

if choice == 1:

	dct = Helpers.logger()
	if len(dct.keys()) == 3:
		user = AdminUser()
		user.SetFields(dct)
	elif len(dct.keys()) > 3:
		user = LoginUser()
		user.SetFields(dct)

elif choice == 2:
	user = RegisteredUser()



if str(type(user)) == "<class 'classes.AdminUser.AdminUser'>":
	print("Item Collection")
	displayer.display(ic.listOfContent)
	print("User Collection")
	displayer.display(uc.listOfContent)
	ic.listOfContent = user.addElementToBase(ic.listOfContent, "item")	


elif str(type(user)) == "<class 'classes.LoginUser.LoginUser'>":
	pass	

elif str(type(user)) == "<class 'classes.RegisteredUser.RegisteredUser'>": 
	uc.listOfContent.append(user.setFieldsAndReturnDataDict())


if str(type(user)) == "<class 'classes.LoginUser.LoginUser'>" or str(type(user)) == "<class 'classes.RegisteredUser.RegisteredUser'>":
	print("Item Collection")
	displayer.display(ic.listOfContent)
	cart = Cart()
	user.addElementToCart(cart.cartList,ic.listOfContent)
	user.delElementFromCart(cart.cartList)



ic.addToFile()
uc.addToFile()
'''

print(type(ic.listOfContent))
print(type(ic.listOfContent[0]))