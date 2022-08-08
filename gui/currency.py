from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt


def currency_page(root, db, mycur):
    global curr
    curr = Toplevel(root)
    curr.geometry('300x300')
    curr.title('Select a currency') 

    Label(curr, text="Select a currency:").pack(ipadx=10, ipady=10, expand=False)

    df = pd.read_csv("dataset/_metadata_exchangeRate.csv")

    namelist = ["..."]
    for i, row in df.iterrows():
        namelist.append(row["Name"] + " (" + row["Symbol"] + ")")

    global selected
    selected = StringVar()
    combo1 = ttk.Combobox(curr, textvariable=selected, value=namelist, state='readonly')
    combo1.current(0)
    combo1.pack(ipadx=10, ipady=10, expand=False)

    Button(curr, text="Get Result Graph", command=lambda: get_result(db)).pack(ipadx=10, ipady=10, expand=False)

def get_result(db):
    str = selected.get()
    if str == "...":
        messagebox.showinfo("Oops", "You have not choose a currency!")
        return
    symbol = str[str.find("(")+1:str.find(")")]

    sql = "SELECT date, price FROM currency WHERE symbol = \"{}\"".format(symbol)
    df = pd.read_sql(sql, db)
    
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index('date')
    df["price"] = pd.to_numeric(df["price"])
    #print(df["price"].head(10))
    df["price"].plot()
    plt.show()
    '''
    fig, ax = plt.subplots()
    ax.plot(df.index, df["price"])
    plt.show()
    '''

#get_result("CNY", db)
