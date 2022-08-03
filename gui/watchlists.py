from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
from soupsieve import select


def read_csv():
    selected = select_type.get()
    if selected == "Type of Asset ...":
        print(selected)
        messagebox.showinfo(
            "Oops", "You have to choose a type of this asset for query.")

#def watchlist_page(root):
    # window
    #global watchlists
watchlists = Tk()
watchlists.geometry("400x500")
watchlists.title("My WatchList")
# title
Label(watchlists, text="My Watchlist", font="bald", bg="grey",fg="white",width=300).pack(ipadx=10, ipady=10, expand=False)
# Note words
Label(watchlists, text="Click 'Add' to query the asset you want to add\n After find your assets, manually input in the chart below\n Click 'Exit' to close the program").pack(ipadx=10,ipady=10, expand=False)

# Exit & Add top Button section
# add new watchlist
Button(watchlists, text="Exit", command=None, height=1,
       width=10).pack(ipadx=10, ipady=10, expand=False) # was True before
global select_type
select_type = StringVar()
combo2 = ttk.Combobox(watchlists, textvariable=select_type, value=[
    "Type of Asset.. ", "Commodity", "Cryptocurrency","Foreign currency","Stock"], state='readonly')
combo2.current(0)
combo2.pack(ipadx=10, ipady=10, expand=False)

Button(watchlists, text="Add", command=read_csv, height=1,
       width=10).pack(ipadx=10, ipady=10, expand=False)
# .pack(side=LEFT, expand=True)
# Watchlist chart section
# From LHS to RHS, it contains following col: No. Name, Symbol, Type,
# inspired by: https://blog.51cto.com/u_13488416/2861499

# crate chart
columns = ('Symbol','Name','Type')
list_chart = ttk.Treeview(watchlists,height=20,columns=columns,show='headings')
list_chart.pack(ipadx=10, ipady=10, expand=False)

# 设置列宽度
list_chart.column('Name',width=200)
list_chart.column('Symbol',width=100)
list_chart.column('Type',width=100)

# 添加列名
list_chart.heading('Name',text='Name')
list_chart.heading('Symbol',text='Symbol')
list_chart.heading('Type',text='Asset Type')

    


watchlists.mainloop()


