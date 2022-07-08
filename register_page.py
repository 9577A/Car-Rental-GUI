from tkinter import *
import GUI_func

register_page = Tk()
register_page.title("Finance Schedule")
register_page.geometry("400x300")

# reg() function adds new user to database and logs user in
def reg():
    person = GUI_func.Client(name.get(), surname.get(), login.get(), password.get(), 'B')
    person.add_client()


# we create input fields and their titles, and variable we later use
def infield(text):
    Label(register_page, text=f"{text.capitalize()}:").pack()
    variable = Entry(width=30)
    variable.pack()
    return variable

# this creates label with text we want
tit = Label(register_page, text="Register now!", font=("Antipasto Pro", 20, "bold"))
tit.pack()

name = infield("Name")
surname = infield("Surname")
login = infield("Login")
password = infield("Password")


bt = Button(register_page, text="Register", command=reg).pack()

register_page.mainloop()