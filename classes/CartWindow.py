from tkinter import *

class CartWindow:

    def __init__(self, root):
        self.root = root
        root.title("CART")
        root.geometry("300x220")

        self.label1 = Label(root, text="Items added to the cart:")
        self.label1.pack()

        self.cartList = ["computer", "mobile", "tablet"]

        self.label_cart = Label(root, text=self.cartList, font='bold')
        self.label_cart.pack(pady=10)

        self.label_entry = Label(root, text="Enter name of product to delete from cart:")
        self.label_entry.pack()
        self.entry = Entry(root, width=20)
        self.entry.focus()
        self.entry.pack()

        self.delete_button = Button(root, text="Delete", command=self.to_delete)
        self.delete_button.pack()

        self.label_buy = Label(root, text="To buy products click on the button")
        self.label_buy.pack(ipady = 5)
        self.buy_button = Button(root, text="Buy", command=self.to_buy)
        self.buy_button.pack()



    def to_delete(self):
        self.res = self.entry.get()
        if self.res in self.cartList:
            self.cartList.remove(self.res)
            self.label_cart.configure(text=self.cartList)
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

if __name__ == '__main__':

    root = Tk()
    my_gui = CartWindow(root)
    root.mainloop()