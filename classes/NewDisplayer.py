from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tree')
# root.iconbitmap()
root.geometry("1280x650+-10+0")

my_tree = ttk.Treeview(root)

my_tree['columns'] = ("Name", "Amount", "Price")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("Amount", anchor=CENTER, width=100)
my_tree.column("Price", anchor=W, width=140)

my_tree.heading("#0", text='', anchor=W)
my_tree.heading("Name", text='Name', anchor=W)
my_tree.heading("Amount", text='Amount', anchor=CENTER)
my_tree.heading("Price", text='Price', anchor=W)

file = open("C:/Users/Nikolay/PycharmProjects/untitled5/OOP/itemBase.txt", "r")
line = file.readlines()
l = []
alllist = []
for i in line:
    dct = eval(i)
    alllist.append(dct)
    p = dct['name'], dct['amountAvalible'], dct['price']
    l.append(p)
file.close()
data = l
print(alllist)


count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
    count += 1

my_tree.pack(pady=20)

cartlist = []
def add_record():
    x = my_tree.selection()[0]
    cartlist.append(list(dict.values(alllist[int(x)]))[0])
    print(cartlist)
    return cartlist


def go_cart():
    root3 = Tk()
    root3.title("Cart Collection")
    root3.geometry("1280x650+-10+0")
    root3.mainloop()

def details():
    x = my_tree.selection()[0]
    root2 = Tk()
    root2.title("Item Information")
    root2.geometry("1280x650+-10+0")
    for key, value in alllist[int(x)].items():
        text = f"{key} : {value}"
        Label(root2, text=text).grid()
    root2.mainloop()

add_record = Button(root, text="Add To Cart", font='sans 14', command=add_record)
add_record.pack(pady=0)

go_cart = Button(root, text="Go To Cart", font='sans 14', command=go_cart)
go_cart.pack(pady=0)

remove_one = Button(root, text="Details", font='sans 14', command=details)
remove_one.pack(pady=0)

root.mainloop()
