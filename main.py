import tkinter as tk
from tkinter.ttk import *

from classes.RegisteredUser import RegisteredUser
from classes.LoginUser import LoginUser

from classes.UsersCollectionSingleton import UsersCollectionSingleton
from classes.ItemCollectionSingleton import ItemCollectionSingleton
from  classes.Helpers import Helpers


if __name__ == '__main__':
	i = ItemCollectionSingleton()
	a = ItemCollectionSingleton()
	i.getAllFromDataBase()
	a.getAllFromDataBase()


	c = UsersCollectionSingleton()
	b = UsersCollectionSingleton()
	c.getAllFromDataBase()
	b.getAllFromDataBase()

	print(i == a, i ,a)
	print("\n", b == c, b, c)