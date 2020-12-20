import tkinter as tk
from tkinter.ttk import *
from classes.RegAndLogWindow import ChoiceWindow


if __name__ == '__main__':
	root = tk.Tk()
	choice = ChoiceWindow(root)
	root.mainloop()
	
	