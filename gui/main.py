import time
from tkinter import *
from tkinter import messagebox
#import mysql.connector

from pages import pages

#connecting to the database
db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
mycur = db.cursor()

def login_validator():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    # query from db
    query = "SELECT * FROM login WHERE user = %s AND password = %s"
    mycur.execute(query,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        home.destroy()
        pages(username_varify) # open the main portal
    else:
        # username-password pair not in db
        messagebox.showinfo("Oops", "Incorrect Username or Password. Please try again!")

def register_validator():
    username_info = username_re.get()
    password_info = password_re.get()
    if username_info == "":
        messagebox.showerror("Error", "Please enter Username")
    elif password_info == "":
        messagebox.showerror("Error", "Please enter Password")
    else:
        sql = "INSERT INTO login values(%s,%s)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.50)
        messagebox.showinfo("Success", "Congrats! You have successfully created a new account!")
        register.destroy()

def registration():
    # register page
    global register
    register = Toplevel(home)   
    register.title("Registration Portal")
    register.geometry("300x250")
    global username_re
    global password_re
    # title
    Label(register,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    username_re = StringVar()
    password_re = StringVar()
    Label(register,text="").pack()
    # username
    Label(register,text="Username :",font="bold").pack()
    Entry(register,textvariable=username_re).pack()
    Label(register, text="").pack()
    # password
    Label(register, text="Password :").pack()
    Entry(register, textvariable=password_re,show="*").pack()
    Label(register, text="").pack()
    # register button
    Button(register,text="Register",bg="red",command=register_validator).pack()


def main_screen():
    # window
    global home, username_varify, password_varify
    home = Tk()
    home.geometry('300x450')
    home.title('Financial Assets Explorer')
    # title
    Label(home, text="Welcome to Financial Assets Explorer! \n Please login in!", font="bold", bg="grey",fg="black",width=300).pack(ipadx=10, ipady=10, expand=False)
    # username label and text entry box
    Label(home, text="Username").pack(ipadx=10, ipady=10, expand=False)
    username_varify = StringVar()
    Entry(home, textvariable=username_varify).pack(ipadx=10, ipady=10, expand=True)
    # password label and password entry box
    Label(home,text="Password").pack(ipadx=10, ipady=10, expand=False)
    password_varify = StringVar()
    Entry(home, textvariable=password_varify, show='*').pack(ipadx=10, ipady=10, expand=True)
    # login button
    Button(home, text="Login", command=login_validator, height=1, width = 10).pack(ipadx=10, ipady=10, expand=True)
    # create account
    Button(home, text="Register", command=registration, height=1, width = 10).pack(ipadx=10, ipady=10, expand=True)




main_screen()
home.mainloop()