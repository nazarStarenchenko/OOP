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

    class CartWindow:

        def __init__(self, root):
            self.root = root
            root.title("CART")
            root.geometry("300x220")

            self.label1 = Label(root, text="Items added to the cart:")
            self.label1.pack()

            self.cartlist = cartList

            self.label_cart = Label(root, text=self.cartlist, font='bold')
            self.label_cart.pack(pady=10)

            self.label_entry = Label(root, text="Enter name of product to delete from cart:")
            self.label_entry.pack()
            self.entry = Entry(root, width=20)
            self.entry.focus()
            self.entry.pack()

            self.delete_button = Button(root, text="Delete", command=self.to_delete)
            self.delete_button.pack()

            self.label_buy = Label(root, text="To buy products click on the button")
            self.label_buy.pack(ipady=5)
            self.buy_button = Button(root, text="Buy", command=self.to_buy)
            self.buy_button.pack()

        def to_delete(self):
            self.res = self.entry.get()
            if self.res in self.cartlist:
                self.cartlist.remove(self.res)
                self.label_cart.configure(text=self.cartlist)
                self.entry.delete(0, END)
            else:
                self.entry.delete(0, END)

                self.destroy_obj = [self.label_buy,
                                    self.buy_button]
                for each in self.destroy_obj:
                    each.destroy()
                self.label_noitem = Label(root, text="There is no such item in the cart")
                self.label_noitem.pack()
                self.label_noitem.after(3000, self.label_noitem.destroy)

                self.label_buy = Label(root, text="To buy products click on the button")
                self.label_buy.pack(ipady=5)
                self.buy_button = Button(root, text="Buy", command=self.to_buy)
                self.buy_button.pack()

        def to_buy(self):
            self.destroy_object = [self.label1, self.label_cart,
                                   self.label_entry, self.label_buy, self.entry,
                                   self.buy_button, self.delete_button]

            for each in self.destroy_object:
                each.destroy()

            self.label_inbuy = Label(root, text="YOUR ORDER WAS CONFIRMED!")
            self.label_inbuy.pack(pady=40)
            self.label_inbuy.after(2000, root.destroy)

    @staticmethod
    def CartWindowMain():
        root = Tk()
        Adaptee.CartWindow(root)
        root.mainloop()

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

    go_cart = Button(text="Go To Cart", font='sans 14', command=Adaptee.CartWindowMain)
    go_cart.pack(pady=0)

    remove_one = Button(text="Details", font='sans 14', command=Adaptee.details)
    remove_one.pack(pady=0)

    root.mainloop()
