import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
#from classes.CartAdder import CartAdder
#from classes.Cart import Cart

class MultiColumnListbox(object):

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        s = """ """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
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
def add():
    pass
def details():
    pass
def go():
    pass

def sortby(tree, col, descending):
    data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))


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
    button1 = tk.Button(root, text="Додати", command=add).pack(fill=tk.X)
    button2 = tk.Button(root, text="Детальніше", command=details).pack(fill=tk.X)
    button3 = tk.Button(root, text="Перейти до кошика", command=go).pack(fill=tk.X)
    root.mainloop()