from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd


def show_assets():
    show_assets = Tk()
    show_assets.geometry("600x600")
    show_assets.title("Query your asset")
    
    #chart frame
    chart_frame = Frame(show_assets).pack(pady=20)
    
    # Note words
    Label(show_assets, text="Find assets you want to add, then manually input back to previous page").pack(ipadx=10,ipady=10, expand=False)
    # Select Type combobox
    global asset_type
    asset_type = StringVar()
    combo1 = ttk.Combobox(show_assets, textvariable=asset_type, value=["Type of Asset is ...", "Commodity", "CryptoCurrency", "Foreign Currency", "Stock"], state='readonly')
    combo1.current(0)
    combo1.pack(ipadx=10, ipady=10, expand=False)
    
    Button(show_assets, text="Start Query", command=read_csv).pack(
        ipadx=10, ipady=10, expand=False)
    
    # create Treeview
    global query_result
    query_result = ttk.Treeview(chart_frame)
        
def read_csv():
    file_name = "F:\CODE_FILE\\2022_Summer_UW_MADISON\CS564\CS564-Final-Project\dataset\_metadata_commo.csv"
    selected = asset_type.get()
    if selected == "Type of Asset is ...":
        messagebox.showinfo(
            "Oops", "You have to choose a type of this asset for query.")
        
    elif selected == "Commodity": 
        print("curr file name is", file_name)
        file_name = "../dataset/_metadata_commo.csv"
    elif selected == "CryptoCurrency":
        file_name = "../dataset/_metadata_crypto.csv"
    elif selected == "Foreign Currency":
        file_name = "../dataset/_metadata_exchangeRate.csv"
    elif selected == "Stock":
        file_name = "../dataset/_metadata_stock.csv"
        
    # handle visualization csv file part
    df = pd.read_csv(file_name)
    
    query_result["column"] = list(df.columns)
    query_result["show"] = "headings"
    
    # loop through col list for headers
    for col in query_result["column"]:
        query_result.heading(col, text=col)
    
    # put data into treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        query_result.insert("", "end",values=row)
        
    query_result.pack()   
            
    
    
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
Button(watchlists, text="Add", command=show_assets, height=1,
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
