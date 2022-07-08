from tkinter import *
import GUI_func


def to_login_page(page):
    page.destroy()
    login_page()


def to_register_page(page):
    page.destroy()
    main_file.register_page()


def to_content_page(page):
    page.destroy()
    main_file.content_page()


def infield(page, text):
    Label(page, text=f"{text.capitalize()}:").pack()
    variable = Entry(width=30)
    variable.pack()
    return variable


def lbl(page, text):
    Label(page, text=text).pack()


def btt(page, text, command):
    Button(page, text=text, command=command)


def reg(page, name, surname, login, password):
    person = GUI_func.Client(name.get(), surname.get(), login.get(), password.get(), 'B')
    person.add_client()
    to_login_page(page)

