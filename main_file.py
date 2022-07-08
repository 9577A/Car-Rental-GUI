from tkinter import *
import GUI_func
from content_file import content_page


# function creates loging window, inserting correct login and password will take you to your account
def login_page():
    page = Tk()
    page.title("Car Rental Company")
    page.geometry("400x300")

    Label(page, text="Log in Page", font=("Antipasto Pro", 20, "bold")).pack()

    login = infield(page, "login")
    password = infield(page, "password")

    Button(page, text="Log in", height=2, width=40, command=lambda: log_in(page, login.get(), password.get())).pack()
    Button(page, text="Go to register page", command=lambda: to_register_page(page), height=2, width=20).pack(side=BOTTOM)
    page.mainloop()


# function creates register window, inserting values to "spaces" allows you to register those values in users table,
def register_page():
    page = Tk()
    page.title("Car Rental Company")
    page.geometry("400x300")

    Label(page, text="Register Page", font=("Antipasto Pro", 20, "bold")).pack()

    name = infield(page, 'name')
    surname = infield(page, 'surname')
    login = infield(page, 'login')
    password = infield(page, 'password')

    Button(page, text="Register", height=2, width=40, command=lambda: reg(page, name, surname, login, password)).pack()
    Button(page, text="Go to log in page", command=lambda: to_login_page(page), height=2, width=20).pack(side=BOTTOM)
    page.mainloop()


# function takes us to log in page and destroys current page
def to_login_page(page):
    page.destroy()
    login_page()


# function takes us to registration page and destroys current page
def to_register_page(page):
    page.destroy()
    register_page()


# function takes us to main or content page and destroys current page
def to_content_page(page, id_user):
    page.destroy()
    content_page(id_user)


# creates Label and Entry space for
def infield(page, text):
    Label(page, text=f"{text.capitalize()}:").pack()
    variable = Entry(width=30)
    variable.pack()
    return variable


# create Label with given text
def lbl(page, text):
    Label(page, text=text).pack()


# creates button with given text, and command
def btt(page, text, command):
    Button(page, text=text, command=command).pack()


# creates new client with given data
def reg(page, name, surname, login, password):
    GUI_func.add_client(name, surname, login, password, 'B')
    to_login_page(page)


# if password and login is correct opens client window
def log_in(page, login, password):
    id_user, log, pssw = GUI_func.log_me_in(login)
    if log == login and pssw == password:
        to_content_page(page, id_user)
