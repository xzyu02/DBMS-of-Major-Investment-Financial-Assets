from tkinter import *
from tkinter import ttk
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

    namelist = []
    for i, row in df.iterrows():
        namelist.append(row["Name"] + " (" + row["Symbol"] + ")")

    global selected
    selected = StringVar()
    combo1 = ttk.Combobox(curr, textvariable=selected, value=namelist, state='readonly')
    combo1.current(0)
    combo1.pack(ipadx=10, ipady=10, expand=False)

    str = selected.get()
    symbol = str[str.find("(")+1:str.find(")")]
    Button(curr, text="Get Result Graph", command=lambda: get_result(symbol, db)).pack(ipadx=10, ipady=10, expand=False)

def get_result(symbol, db):
    sql = "SELECT date, price FROM currency WHERE symbol = \"{}\"".format(symbol)
    df = pd.read_sql(sql, db, parse_dates=True)

    df["date"] = pd.to_datetime(df["date"])

    date = df["date"]
    value = df["price"]   

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(date, value)
    plt.show()

