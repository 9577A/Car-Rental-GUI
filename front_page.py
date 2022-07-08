from tkinter import *
from tkinter import ttk

front_page = Tk()
front_page.title("Front Page")
front_page.geometry("400x300")


cars = ttk.Treeview(front_page)
cars['columns'] = ('Brand', 'Model')

cars.column('#0', width=120, minwidth=25)
cars.column('Brand', anchor=W, width=80)
cars.column('Model', anchor=CENTER, width=120)

cars.heading("#0", text="Label")
cars.heading("#0", text="siema")
cars.heading("#1", text="Label")

cars.pack()



mainloop()