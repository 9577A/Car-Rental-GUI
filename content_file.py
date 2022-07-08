from tkinter import ttk
from tkinter import *
from tkcalendar import *
from GUI_func import Client, car_brand_all, car_model_all, car_table, what_car_id
from datetime import datetime


def content_page(id_user):
    page = Tk()
    page.title("Car Rental Company")
    page.geometry("700x400")

    # columns and rows numbers
    r = 2
    c = 0
    user = Client(id_user)

    # create list of all brands
    car_brands = car_brand_all()
    # create list of all models

    # function creates list of cars with selected requirements
    cars = ttk.Treeview(page)
    def tbl():
        global table
        table = car_table(marka=car_brand.get(), model=car_model.get(), min_cost=min_cost.get(), max_cost=max_cost.get())
        global car_models
        car_models = car_model_all(car_brand.get())
        print("Table:", table)
        print("Modele:", car_brand.get(), car_models)
        print()
        refresh_tree(cars)

    # function changes car_brand variable and runs function tbl()
    def update_brand(inf):
        car_brand.set(inf)
        tbl()

    # function changes car_brand variable and runs function tbl()
    def update_cost(infmax, infmin):
        min_cost.set(infmin)
        max_cost.set(infmax)
        tbl()

    # functon calls for renting window
    def r_car(inf):
        selected = cars.focus()
        hoh = cars.item(selected, 'values')
        print(hoh[0], hoh[1], hoh[2], what_car_id(hoh[0], hoh[1]))
        print(what_car_id(hoh[0], hoh[1]))
        rent_window(user, what_car_id(hoh[0], hoh[1]), hoh)

    # create variables for brand and model of looked car
    car_brand = StringVar(page, "ALL")
    car_model = StringVar(page, "ALL")
    # create variables for maximum and minimum cost of looked car
    min_cost = StringVar(page, "ALL")
    max_cost = StringVar(page, "ALL")
    # create list with selected requirements
    table = car_table(marka=car_brand.get(), model=car_model.get(), min_cost=min_cost.get(), max_cost=max_cost.get())

    # create a client name and surname in top left corner
    Label(page, text=f"Name: {user.name} {user.surname}").grid(row=0, column=0)

    # create OptionMenu responsible for Brand requirement
    Label(page, text=f"Brand:").grid(row=r, column=c)
    clicked = StringVar()
    clicked.set(car_brands[0])

    drop = OptionMenu(page, clicked, *car_brands, command=lambda *args: update_brand(clicked.get()))
    drop.grid(row=r + 1, column=c)

    # create Entry for maximal cost
    max_cost = infield(page, "Maximal Cost", r+1, c+1)
    # create Entry for minimal cost
    min_cost = infield(page, "Minimal Cost", r+1, c+2)
    # create button updating minimal and maximal cost
    Button(page, text="Search", height=2, width=10, command=lambda: tbl()).grid(row=r, column=c+3)

    #
    # create treeview of cars with set requirement
    cars = ttk.Treeview(page)
    cars['columns'] = ('Brand', 'Model', 'Cost')
    # create columns for treeview cars
    cars.column('#0', width=0, minwidth=0)
    cars.column('Brand', anchor=W, width=100)
    cars.column('Model', anchor=W, width=100)
    cars.column('Cost', anchor=W, width=100)
    # create headings cor treeview cars
    cars.heading("Brand", text="Brand")
    cars.heading("Model", text="Model")
    cars.heading("Cost", text="Cost")

    # add data to cars treeview
    for i in table:
        Checkbutton(page, text="ss",)
        cars.insert(parent='', index='end', text="Parent", values=i)
    # grid treeview cars
    cars.grid(column=0, row=4)
    # Binding cars treeview
    cars.bind("<Double-1>", r_car)

    Button(page, text='Show my rents', height=10, width=20, command=lambda: rented_cars(user)).grid(row=4, column=1)

    page.mainloop()


# creates new window used to rent a car
def rent_window(client, car_id, car_inf):
    rentwindow = Tk()
    rentwindow.title("Rent Your Car")
    rentwindow.geometry("620x300")

    title = Label(rentwindow, text=f"Rent {car_inf[0]} {car_inf[1]}")
    title.grid(row=0, column=1)

    # we get current day, month and year
    current_date = datetime.now()
    date = current_date.date()

    # Calendars for first and last day
    Label(rentwindow, text='First Day').grid(row=1, column=0)
    fday = Calendar(rentwindow, selectmode='day', year=date.year, month=date.month, day=date.day, date_pattern='d/m/yy')
    fday.grid(row=2, column=0)
    Label(rentwindow, text='',).grid(row=3, column=0)

    Label(rentwindow, text='Last Day').grid(row=1, column=2)
    lday = Calendar(rentwindow, selectmode='day', year=date.year, month=date.month, day=date.day, date_pattern='d/m/yy')
    lday.grid(row=2, column=2)
    communicate = Label(rentwindow, text='',)
    communicate.grid(row=5, column=1)
    Button(rentwindow, text="Rent a car", command=lambda: communicate.config(text=client.rent_car(car_id, fday.get_date(), lday.get_date()))).grid(row=4, column=1)
    #rentwindow.mainloop()
    #client.rent_car(car_id, fday.get(), lday.get())


# creates new window contaning all rents a customer has booked
def rented_cars(customer):
    booked_window = Tk()
    booked_window.title('All Rented Cars')
    booked_window.geometry("353x227")

    # create treeview of all rents made by logged customer
    allrents = ttk.Treeview(booked_window)
    allrents['columns'] = ('Car', 'First Date', 'Last Date')
    # create columns for allrents treeview
    allrents.column('#0', width=0, minwidth=0)
    allrents.column('Car', anchor=W, width=150)
    allrents.column('First Date', anchor=W, width=100)
    allrents.column('Last Date', anchor=W, width=100)
    # create headings for allrents treeview
    allrents.heading('Car', text='Car')
    allrents.heading('First Date', text='First Date')
    allrents.heading('Last Date', text='Last Date')

    all_rents_table = customer.all_rents()

    for i in all_rents_table:
        Checkbutton(booked_window, text="ss",)
        allrents.insert(parent='', index='end', text="Parent", values=i)

    # grid treeview cars
    allrents.grid(column=1, row=3)


# refreshes cars Treeview
def refresh_tree(cars):
    cars.delete(*cars.get_children())
    for i in table:
        cars.insert(parent='', index='end', text="Parent", values=i)


# creates Label and Entry of certain name and position
def infield(page, text, r, c):
    Label(page, text=f"{text.capitalize()}:").grid(row=r-1, column=c)
    variable = Entry(page, width=15)
    variable.grid(row=r, column=c)
    return variable


"""
#
    # create treeview of all rents made by logged customer
    allrents = ttk.Treeview(page)
    allrents['columns'] = ('Car', 'First Date', 'Last Date')
    # create columns for allrents treeview
    allrents.column('#0', width=0, minwidth=0)
    allrents.column('Car', anchor=E, width=150)
    allrents.column('First Date', anchor=E, width=100)
    allrents.column('Last Date', anchor=E, width=100)
    # create headings for allrents treeview
    allrents.heading('Car', text='Car')
    allrents.heading('First Date', text='First Date')
    allrents.heading('Last Date', text='Last Date')

    # grid treeview cars
    allrents.grid(column=1, row=3)
    # Binding cars treeview
    #cars.bind("<Double-1>", r_car)
"""