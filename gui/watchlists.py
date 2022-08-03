from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
import mysql.connector 

def show_assets():
    global show_assets
    show_assets = Toplevel(watchlists)
    show_assets.geometry("400x500")
    show_assets.title("Query your asset")
    
    # Note words
    Label(show_assets, text="Find assets you want to add, \n then manually input back to previous page").pack(ipadx=10,ipady=10, expand=False)
    # select and Add currency
    global selected1
    selected1 = StringVar()
    combo1 = ttk.Combobox(
        show_assets, textvariable=selected1, value=get_combobox_list("dataset/_metadata_exchangeRate.csv"), state='readonly')
    combo1.pack(ipadx=10, ipady=10, expand=False)
    
    Button(show_assets, text="Add a currency", command=lambda: insert_to_db(user, selected1, "currency")).pack(ipadx=10, ipady=10, expand=False)
    
    # select and add stock
    global selected2
    selected2 = StringVar()
    combo2 = ttk.Combobox(
        show_assets, textvariable=selected2, value=get_combobox_list("dataset/_metadata_stock.csv"), state='readonly')
    combo2.pack(ipadx=10, ipady=10, expand=False)

    Button(show_assets, text="Add a Stock", command=lambda: insert_to_db(user, selected2, "stock")).pack(ipadx=10, ipady=10, expand=False)
    # # select and add Commo
    namelist = get_combobox_list("dataset/_metadata_commo.csv")
    global selected3
    selected3 = StringVar()
    combo3 = ttk.Combobox(show_assets, textvariable=selected3, value=namelist, state='readonly')
    combo3.pack(ipadx=10, ipady=10, expand=False)

    Button(show_assets, text="Add a Commodity", command=lambda: insert_to_db(user, selected3, "commo")).pack(ipadx=10, ipady=10, expand=False)

    namelist = get_combobox_list("dataset/_metadata_crypto.csv")
    global selected4
    selected4 = StringVar()
    combo4 = ttk.Combobox(show_assets, textvariable=selected4, value=namelist, state='readonly')
    combo4.pack(ipadx=10, ipady=10, expand=False)

    Button(show_assets, text="Add a Crypto", command=lambda: insert_to_db(user, selected4, "crypto")).pack(ipadx=10, ipady=10, expand=False)
    
def get_combobox_list(filename):
    df = pd.read_csv(filename)
    namelist = []
    for i, row in df.iterrows():
        namelist.append(row["Name"] + " (" + row["Symbol"] + ")")
    return namelist

def insert_to_db(_user, str, _type):
    str = str.get()
    _name = str[:str.find("(")-1]
    _symbol = str[str.find("(")+1:str.find(")")]
    sql = "INSERT INTO watchlist values(%s,%s,%s,%s)"
    t = (_user, _symbol, _name, _type)
    mycur.execute(sql, t)
    db.commit()
    messagebox.showinfo("Success", "Insert Success!! \n Reopen watchlist page to get your latest watchlist list!")
    watchlists.destroy()

    
def watchlist_page(root, _db, _mycur, _user):
    global db, mycur, user
    db = _db
    mycur = _mycur
    user = _user
    # window
    global watchlists
    watchlists = Toplevel(root)
    watchlists.geometry("400x500")
    watchlists.title("My WatchList")
    # title
    Label(watchlists, text="My Watchlist", font="bald", bg="grey",fg="white",width=300).pack(ipadx=10, ipady=10, expand=False)
    # Note words
    Label(watchlists, text="Click 'Add' to query the asset you want to add\n After find your assets, manually input in the chart below\n Click 'Exit' to close the program").pack(ipadx=10,ipady=10, expand=False)

    # Exit & Add top Button section
    # add new watchlist
    Button(watchlists, text="Exit", command=watchlists.destroy, height=1, width=10).pack(ipadx=10, ipady=10, expand=False) # was True before
    Button(watchlists, text="Add", command=show_assets, height=1, width=10).pack(ipadx=10, ipady=10, expand=False)

    # Watchlist chart section
    # From LHS to RHS, it contains following col: No. Name, Symbol, Type,
    # inspired by: https://blog.51cto.com/u_13488416/2861499

    # crate chart
    columns = ('Symbol','Name','Type')
    global list_chart
    list_chart = ttk.Treeview(watchlists,height=20,columns=columns,show='headings')
    list_chart.pack(ipadx=10, ipady=10, expand=False)

    # column width
    list_chart.column('Name',width=200)
    list_chart.column('Symbol',width=100)
    list_chart.column('Type',width=100)

    # column names
    list_chart.heading('Name',text='Name')
    list_chart.heading('Symbol',text='Symbol')
    list_chart.heading('Type',text='Asset Type')

    get_watchlist(user)

def get_watchlist(username):
    sql = "SELECT symbol, name, type FROM watchlist WHERE user = \"{}\"".format(username)
    df = pd.read_sql(sql, db)
    tup = list(df.itertuples(index=False, name=None))
    for i in tup:
        list_chart.insert('', END, values=i)


'''
watchlist_page()
watchlists.mainloop()
'''
