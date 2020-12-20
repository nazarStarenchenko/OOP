from tkinter import *
from tkinter import ttk
from classes.UsersCollection import UsersCollection
from classes.ItemCollection import ItemCollection
import sys


class Adaptee:
    # def specific_request(self) -> str:
    #    return ".eetpadA eht fo roivaheb laicepS"

    @staticmethod
    def add_record():
        x = my_tree.selection()[0]
        cartList.append(list(dict.values(alllist[int(x)]))[0])
        print(cartList)
        return cartList

    @staticmethod
    def CartWindow():

        def to_delete():
            res = txt.get()
            cartList.remove(res)
            lbl1.configure(text=cartList)
            txt.delete(0, END)

        def to_buy():

            destroy_object = [lbl, lbl1, lbl2, lbl3, btn, btn2, txt]
            for object_name in destroy_object:
                if object_name.winfo_viewable():
                    object_name.grid_remove()
                else:
                    object_name.grid()

            lbl_buy = Label(window, text="Your order was confirmed!\nProgram will close itself")
            lbl_buy.grid(column=2, row=0)
            lbl_buy.after(2000, close_window)
            root1.after(2, sys.exit())

        def close_window():
            window.destroy()

        window = Tk()
        window.title("Cart")
        window.geometry('600x250')
        lbl = Label(window, text="Items added to the cart", font=("Arial Bold", 12))
        lbl.grid(column=1, row=0)
        lbl1 = Label(window, text=cartList)
        lbl1.grid(column=0, row=2)

        lbl3 = Label(window, text="Enter name of product to delete from cart:")
        lbl3.grid(column=0, row=4)
        global txt
        txt = Entry(window, width=20)
        txt.grid(column=1, row=4)
        txt.focus()

        btn = Button(window, text="Delete", command=to_delete)
        btn.grid(column=1, row=5, pady=5)

        lbl2 = Label(window, text="To buy products click on the button")
        lbl2.grid(column=0, row=7)
        btn2 = Button(window, text="Buy", command=to_buy)
        btn2.grid(column=1, row=7)

        window.mainloop()

    @staticmethod
    def details():
        x = my_tree.selection()[0]
        root2 = Tk()
        root2.title("Item Information")
        root2.geometry("290x450+-10+0")
        for key, value in alllist[int(x)].items():
            text = f"{key} : {value}"
            Label(root2, text=text).grid()
        root2.mainloop()

    @staticmethod
    def mainDisplay():
        global my_tree, cartList, alllist, root1
        root1 = Tk()
        root1.title('Tree')
        root1.geometry("400x450+-10+0")
        my_tree = ttk.Treeview(root1)
        file = open("itemBase.txt", "r")
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
        cartList = []


        my_tree['columns'] = ("Name", "Amount", "Price")

        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Name", anchor=W, width=140)
        my_tree.column("Amount", anchor=CENTER, width=100)
        my_tree.column("Price", anchor=W, width=140)

        my_tree.heading("#0", text='', anchor=W)
        my_tree.heading("Name", text='Name', anchor=W)
        my_tree.heading("Amount", text='Amount', anchor=CENTER)
        my_tree.heading("Price", text='Price', anchor=W)

        count = 0
        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
            count += 1
        my_tree.pack(pady=20)
        

        add_record = Button(root1,text="Add To Cart", font='sans 14', command=Adaptee.add_record)
        add_record.pack()

        go_cart = Button(root1,text="Go To Cart", font='sans 14', command=Adaptee.CartWindow)
        go_cart.pack()

        remove_one = Button(root1, text="Details", font='sans 14', command=Adaptee.details)
        remove_one.pack()
        root1.mainloop()



