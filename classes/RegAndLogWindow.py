import tkinter as tk
from tkinter.ttk import *
from classes.Helpers import Helpers
from classes.RegisteredUser import RegisteredUser
from classes.LoginUser import LoginUser
from classes.Displayer import Adaptee

#class log window
class LogWindow(tk.Toplevel):

	def __init__(self, root=None):
		
		super().__init__(master=root)
		self.geometry("300x150") 
		self.r = root

		tk.Label(self, text ="enter login").pack()
		self.logFuncLoginEntry = tk.Entry(self)
		self.logFuncLoginEntry.pack()

		tk.Label(self, text ="enter password").pack()
		self.logFuncPassEntry = tk.Entry(self)
		self.logFuncPassEntry.pack()

		self.submitButton = tk.Button(self,text="Submit",command=self.checkInDataBaseForLog)
		self.submitButton.pack()


	def checkInDataBaseForLog(self):
		self.dictToCheck = dict()
		self.dictToCheck["login"] = self.logFuncLoginEntry.get()
		self.dictToCheck["password"] = self.logFuncPassEntry.get()	
		
		resDict = Helpers.logger(self.dictToCheck)
		counter = 0

		if bool(resDict)== False:
			if counter == 0:
				counter += 1
				tk.Label(self, text="there is no user with this email or password,\nor you entered invalid data", fg="red").pack()
		elif bool(resDict) == True:
			lu = LoginUser().SetFields(resDict)
			print(lu)
			self.destroy()
			Adaptee.mainDisplay()
			

#class reg window
class RegWindow(tk.Toplevel):

	def __init__(self, root=None):

		super().__init__(master=root)
		self.r = root
		self.geometry("300x448")

		#email
		tk.Label(self, text ="enter email").pack()
		self.regFuncEmailEntry = tk.Entry(self)
		self.regFuncEmailEntry.pack()
		#password
		tk.Label(self, text ="enter password").pack()
		self.regFuncPassEntry = tk.Entry(self)
		self.regFuncPassEntry.pack() 
		#name
		tk.Label(self, text ="enter name").pack()
		self.nameEntry = tk.Entry(self)
		self.nameEntry.pack() 
		#age
		tk.Label(self, text ="enter age").pack()
		self.ageEntry = tk.Entry(self)
		self.ageEntry.pack() 
		#card number
		tk.Label(self, text ="enter card number").pack()
		self.cardNumberEntry = tk.Entry(self)
		self.cardNumberEntry.pack() 
		#cvv
		tk.Label(self, text ="enter cvv").pack()
		self.cvvEntry = tk.Entry(self)
		self.cvvEntry.pack() 
		#card date year
		tk.Label(self, text ="enter card date year").pack()
		self.cardDateYearEntry = tk.Entry(self)
		self.cardDateYearEntry.pack() 
		#card date month
		tk.Label(self, text ="enter card date month").pack()
		self.cardDateMonthEntry = tk.Entry(self)
		self.cardDateMonthEntry.pack() 
		#card password
		tk.Label(self, text ="enter card password").pack()
		self.cardPasswordEntry = tk.Entry(self)
		self.cardPasswordEntry.pack() 

		self.submitButton = tk.Button(self,text="Submit",command=self.checkInDataBaseForReg)
		self.submitButton.pack()


	def checkInDataBaseForReg(self):
		self.dictToCheck = dict()
		self.dictToCheck["email"] = self.regFuncEmailEntry.get()
		self.dictToCheck["password"] = self.regFuncPassEntry.get()
		self.dictToCheck["name"] = self.nameEntry.get()
		self.dictToCheck["age"] = self.ageEntry.get()
		self.dictToCheck["cardNumber"] = self.cardNumberEntry.get()
		self.dictToCheck["cvv"] = self.cvvEntry.get()
		self.dictToCheck["cardDateYear"] = self.cardDateYearEntry.get()
		self.dictToCheck["cardDateMonth"] = self.cardDateMonthEntry.get()
		self.dictToCheck["cardPassword"] = self.cardPasswordEntry.get()
		
		resDict = Helpers.getDataFromUser(self.dictToCheck)
		counter = 0
		print(resDict)

		if bool(resDict)== False:
			if counter == 0:
				tk.Label(self, text="you entered ivalid data", fg="red").pack()
				counter += 1
				return False
		elif bool(resDict) == True:
			userBase.appendToUserCollection(resDict)
			ru = RegisteredUser().setFields(resDict)
			print(ru)
			self.destroy()
			Adaptee.mainDisplay()
			

class ChoiceWindow:

	def __init__(self, root):

		self.window = tk.Toplevel(root)	
		self.window.geometry("200x50")
		root.withdraw()
		#class of chioce	
		self.lb = tk.Label(self.window,text="You want to register or login?")
		self.logButton = tk.Button(self.window, text="login", width=10)
		self.regButton = tk.Button(self.window, text="reg", width=10)

		self.logButton.bind("<Button 1>", lambda e: self.closeLog(root))
		self.regButton.bind("<Button 1>", lambda e:	self.closeReg(root))
		self.lb.pack()
		self.logButton.pack(side=tk.LEFT)
		self.regButton.pack(side=tk.RIGHT)

	def closeReg(self, root):
		a = RegWindow(root)
		self.window.destroy()
		return a

	def closeLog(self, root):
		a = LogWindow(root)
		self.window.destroy()
		return a

