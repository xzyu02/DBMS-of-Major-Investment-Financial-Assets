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
home.geometry('300x300')
home.title('Financial Assets Explorer')

# username label and text entry box
usernameLabel = Label(home, text="Username").place(relx=0.5,rely=0.2,anchor='center')
username = StringVar()
usernameEntry = Entry(home, textvariable=username).place(relx=0.5,rely=0.3,anchor='center')

# password label and password entry box
passwordLabel = Label(home,text="Password").place(relx=0.5,rely=0.4,anchor='center') 
password = StringVar()
passwordEntry = Entry(home, textvariable=password, show='*').place(relx=0.5,rely=0.5,anchor='center') 


# login button
loginButton = Button(home, text="Login", command=submit, height=1, width = 8).place(relx=0.5,rely=0.6,anchor='center')


if __name__ == "__main__":
    home.mainloop()