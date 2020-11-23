import tkinter as tk

from classes.AdminUser import AdminUser
from classes.RegisteredUser import RegisteredUser
from classes.LoginUser import LoginUser

from classes.UsersCollection import UsersCollection
from classes.ItemCollection import ItemCollection

from classes.Displayer import Displayer
from  classes.Helpers import Helpers

from classes.Cart import Cart


userBase = UsersCollection()
userBase.getAllFromDataBase()


root = tk.Tk()
root.geometry("200x50")


def createLogWindow():

		global logFuncLoginEntry, logFuncPassEntry, logWindow;
		logWindow = tk.Toplevel(root)
		logWindow.geometry("300x150") 

		tk.Label(logWindow, text ="enter login").pack()
		logFuncLoginEntry = tk.Entry(logWindow)
		logFuncLoginEntry.pack()

		tk.Label(logWindow, text ="enter password").pack()
		logFuncPassEntry = tk.Entry(logWindow)
		logFuncPassEntry.pack()

		submitButton = tk.Button(logWindow,text="Submit",command=checkInDataBaseForLog)
		submitButton.pack()


def checkInDataBaseForLog():
	dictToCheck = dict()
	dictToCheck["login"] = logFuncLoginEntry.get()
	dictToCheck["password"] = logFuncPassEntry.get()	
	
	resDict = Helpers.logger(dictToCheck)
	coutner = 0

	if bool(resDict)== False:
		if counter == 0:
			counter += 1
			tk.Label(logWindow, text="there is no user with this email or password,\nor you entered invalid data", fg="red").pack()
	elif bool(resDict) == True:
		global lu
		lu = LoginUser().SetFields(resDict)
		logWindow.destroy()


def createRegWindow():

		global regFuncEmailEntry, regFuncPassEntry, regWindow, nameEntry,ageEntry
		global cardNumberEntry, cvvEntry, cardDateYearEntry, cardDateMonthEntry ,cardPasswordEntry
		#creating frame of window
		regWindow = tk.Toplevel(root)
		regWindow.geometry("300x480") 

		#email
		tk.Label(regWindow, text ="enter email").pack()
		regFuncEmailEntry = tk.Entry(regWindow)
		regFuncEmailEntry.pack()
		#password
		tk.Label(regWindow, text ="enter password").pack()
		regFuncPassEntry = tk.Entry(regWindow)
		regFuncPassEntry.pack() 
		#name
		tk.Label(regWindow, text ="enter name").pack()
		nameEntry = tk.Entry(regWindow)
		nameEntry.pack() 
		#age
		tk.Label(regWindow, text ="enter age").pack()
		ageEntry = tk.Entry(regWindow)
		ageEntry.pack() 
		#card number
		tk.Label(regWindow, text ="enter card number").pack()
		cardNumberEntry = tk.Entry(regWindow)
		cardNumberEntry.pack() 
		#cvv
		tk.Label(regWindow, text ="enter cvv").pack()
		cvvEntry = tk.Entry(regWindow)
		cvvEntry.pack() 
		#card date year
		tk.Label(regWindow, text ="enter card date year").pack()
		cardDateYearEntry = tk.Entry(regWindow)
		cardDateYearEntry.pack() 
		#card date month
		tk.Label(regWindow, text ="enter card date month").pack()
		cardDateMonthEntry = tk.Entry(regWindow)
		cardDateMonthEntry.pack() 
		#card password
		tk.Label(regWindow, text ="enter card password").pack()
		cardPasswordEntry = tk.Entry(regWindow)
		cardPasswordEntry.pack() 

		submitButton = tk.Button(regWindow,text="Submit",command=checkInDataBaseForReg)
		submitButton.pack()


def checkInDataBaseForReg():
	dictToCheck = dict()
	dictToCheck["email"] = regFuncEmailEntry.get()
	dictToCheck["password"] = regFuncPassEntry.get()
	dictToCheck["name"] = nameEntry.get()
	dictToCheck["age"] = ageEntry.get()
	dictToCheck["cardNumber"] = cardNumberEntry.get()
	dictToCheck["cvv"] = cvvEntry.get()
	dictToCheck["cardDateYear"] = cardDateYearEntry.get()
	dictToCheck["cardDateMonth"] = cardDateMonthEntry.get()
	dictToCheck["cardPassword"] = cardPasswordEntry.get()
	
	resDict = Helpers.getDataFromUser(dictToCheck)
	counter = 0
	print(resDict)

	if bool(resDict)== False:
		if counter == 0:
			tk.Label(regWindow, text="you entered ivalid data", fg="red").pack()
			counter += 1
	elif bool(resDict) == True:
		global ru
		userBase.appendToUserCollection(resDict)
		ru = RegisteredUser().setFields(resDict)
		regWindow.destroy()


if __name__ == '__main__':
	
	lb = tk.Label(text="You want to register or login?")
	logButton = tk.Button(text="login",
						width=10,
						command=createLogWindow)
	regButton = tk.Button(text="reg", width=10, command=createRegWindow)
	lb.pack()
	logButton.pack(side=tk.LEFT)
	regButton.pack(side=tk.RIGHT)
	root.mainloop()

	userBase.addToFile()