from tkinter import *
from tkinter import ttk

# from OOP.CartWindowFrame import CartWindow

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


class Target:
    def request(self) -> str:
        pass


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

            lbl_buy = Label(window, text="Your order was confirmed!")
            lbl_buy.grid(column=2, row=0)
            lbl_buy.after(2000, close_window)
            root.after(2, root.destroy)
            
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
        root2.geometry("1280x650+-10+0")
        for key, value in alllist[int(x)].items():
            text = f"{key} : {value}"
            Label(root2, text=text).grid()
        root2.mainloop()


class Adapter(Target, Adaptee):
    def request(self):
        pass


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
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
    cartList = []

    add_record = Button(text="Add To Cart", font='sans 14', command=Adaptee.add_record)
    add_record.pack(pady=0)

    go_cart = Button(text="Go To Cart", font='sans 14', command=Adaptee.CartWindow)
    go_cart.pack(pady=0)

    remove_one = Button(text="Details", font='sans 14', command=Adaptee.details)
    remove_one.pack(pady=0)
    root.mainloop()
