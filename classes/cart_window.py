from tkinter import *

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
    lbl_buy.after(2000,close_window)


def close_window():
    window.destroy()

cartList = ["computer", "mobile", "tablet"]


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