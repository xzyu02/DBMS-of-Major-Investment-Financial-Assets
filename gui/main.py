from tkinter import *
from tkinter import messagebox
import mysql.connector

from pages import pages

def submit(username, password):
    user = username.get()
    # error case empty username
    if not username:
        messagebox.showerror("Error", "Please enter Username")
        return
    key = password.get()
    # error case empty password
    if not password:
        messagebox.showerror("Error", "Please enter Password")
        return
    # both username and password are filled, connect db
    connect_db(user, key)

def connect_db(user, key):
    db = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "A1b2C3d4++",
                                     db ="user")
    cursor = db.cursor()
    # query from db
    query = "SELECT * FROM login WHERE name = %s AND password = %s"
    cursor.execute(query, [(user), (key)])
    result = cursor.fetchall()
    if result:
        pages(username)
        return True
    else:
        # username-password pair not in db
        messagebox.showinfo("Oops", "Incorrect Username or Password. Please try again!")
        return False


# window
home = Tk()
home.geometry('300x450')
home.title('Financial Assets Explorer')

TitleLabel = Label(home, text="Welcome to Financial Assets Explorer! \n Please login in!").pack(ipadx=10, ipady=10, expand=False)

# username label and text entry box
usernameLabel = Label(home, text="Username").pack(ipadx=10, ipady=10, expand=False)
username = StringVar()
usernameEntry = Entry(home, textvariable=username).pack(ipadx=10, ipady=10, expand=True)

# password label and password entry box
passwordLabel = Label(home,text="Password").pack(ipadx=10, ipady=10, expand=False)
password = StringVar()
passwordEntry = Entry(home, textvariable=password, show='*').pack(ipadx=10, ipady=10, expand=True)


# login button
loginButton = Button(home, text="Login", command=submit, height=1, width = 10).pack(ipadx=10, ipady=10, expand=True)

# create account
createButton = Button(home, text="Create Account", command=submit, height=1, width = 10).pack(ipadx=10, ipady=10, expand=True)

if __name__ == "__main__":
    home.mainloop()