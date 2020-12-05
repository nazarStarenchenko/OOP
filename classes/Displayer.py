import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import *
#from classes.RegularUser import RegularUser
#from classes.CartAdder import CartAdder


class MultiColumnListbox(object):

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()




    def _setup_widgets(self):

        s = """Оберіть товари: """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n", padding=(10, 2, 10, 6), text=s, width=120)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        self.tree = ttk.Treeview(columns=column, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)


    def _build_tree(self):
        for col in column:
            self.tree.heading(col, text=col.title(), command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col, width=tkFont.Font().measure(col.title()))

        for item in l:
            self.tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(column[ix], width=None) < col_w:
                    self.tree.column(column[ix], width=col_w)


def sortby(tree, col, descending):
    data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

#Observed
class Button:
    def __init__(self):
        self.__handlers = {}

    def add_handler(self, event, handler):
        if event not in self.EVENTS or event not in handler.EVENTS:
            raise "Unsupported event type: '{}'".format(event)
        if event not in self.__handlers:
            self.__handlers[event] = []
        if handler not in self.__handlers[event]:
            self.__handlers[event].append(handler)

    def remove_handler(self, event, handler):
        if event in self.__handlers:
            self.__handlers[event].remove(handler)

    def notify(self, event):
        if event in self.__handlers:
            for handler in self.__handlers[event]:
                handler.handle(event)


class Button1(Button):
    EVENTS = ['click']


class Button2(Button):
    EVENTS = ['click']


class Button3(Button):
    EVENTS = ['click']


# class ExitButton2(Button):
#     EVENTS = ['click']


class Handler1:
    EVENTS = ['click', 'hover']

    def handle(self, event):
        if event == 'click':
            # cartList.append([tree.item(x) for x in tree.selection()])
            pass



class Handler2:
    EVENTS = ['click']

    def handle(self, event):
        if event == 'click':
            Details().mainloop()


class Handler3:
    EVENTS = ['click']

    def handle(self, event):
        if event == 'click':
            Cart().mainloop()

# class Handler4:
#     EVENTS = ['click']
#
#     def handle(self, event):
#         if event == 'click':
#             Cart().mainloop()


def add(cartList):
    btn.notify('click')


def details():
    btn2.notify('click')


def go():
    btn3.notify('click')


class Details(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        label = Label(self, text='Details', width=120, height=30)
        label.pack()


class Cart(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        label = Label(self, text='Cart', width=120, height=30)
        label.pack()


column = ['Назва товару', 'Ціна']
file = open("C:\\Users\\VivoBook\\PycharmProjects\\OOP-1\\itemBase.txt", "r")
line = file.readlines()
l = []
for i in line:
    dct = eval(i)
    p = dct['name'], dct['price']
    l.append(p)
file.close()




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Список товарів")
    listbox = MultiColumnListbox()
    cartList = []
    btn = Button1()
    handler1 = Handler1()
    btn.add_handler('click', handler1)
    btn2 = Button2()
    handler2 = Handler2()
    btn2.add_handler('click', handler2)
    btn3 = Button3()
    handler3 = Handler3()
    btn3.add_handler('click', handler3)
    button1 = tk.Button(root, text="Додати", command=add(cartList)).pack(fill=tk.X)
    button2 = tk.Button(root, text="Детальніше", command=details).pack(fill=tk.X)
    button3 = tk.Button(root, text="Перейти до кошика", command=go).pack(fill=tk.X)
    exit_button = tk.Button(root, text="Вихід", command=root.quit).pack(fill=tk.X)
    root.mainloop()

