import datetime
from unicodedata import category
from numpy.core.defchararray import center
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from numpy import pad
from sqlalchemy import null  
import mysql.connector 

def connect_db():
    db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
    mycur = db.cursor()
    return db, mycur

db, mycur = connect_db()
    
# Below is the code for plotting the "search" page; can be packed into the search_asset() (commented line 18) 
# basic layout follow plotted diagram published
#def search_asset():

def search():
    # plot window
    global search
    search = Tk()
    search.geometry('300x500')
    search.title('Search for an asset') 
    # ROW 0 introducing words
    Label(search, text="Search assets by type in the name / symbol:").pack(ipadx=10, ipady=10, expand=False)
    # Entry box for users to type asset name/symbol
    global enter_asset_box
    enter_asset_box = StringVar()
    Entry(search, textvariable=enter_asset_box).pack(ipadx=10, ipady=10, expand=False)
    # Drop down box #1: Category of the assets to search
    global asset_category
    asset_category = StringVar()
    combo1 = ttk.Combobox(search, textvariable=asset_category, value=["Category of Asset is ...", "Commodity", "CryptoCurrency", "Foreign Currency", "Stock"], state='readonly')
    combo1.current(0)
    combo1.pack(ipadx=10, ipady=10, expand=False)
    # Drop down box #2: Search by symbol or name
    global asset_name_symbol
    asset_name_symbol = StringVar()
    combo2 = ttk.Combobox(search, textvariable=asset_name_symbol, value=["Search by ...", "Symbol", "Name"], state='readonly')
    combo2.current(0)
    combo2.pack(ipadx=10, ipady=10, expand=False)
    # start and end time title
    Label(search, text="Enter the time period you want to query\n NOTE: enter date in yyyy-mm-dd format").pack(ipadx=10, ipady=10, expand=False)
    # start
    Label(search, text="Start from:").pack(ipadx=10, ipady=10, expand=False)
    global start_date_entry
    start_date_entry = StringVar()
    Entry(search, textvariable=start_date_entry).pack(ipadx=10, ipady=10, expand=False)
    # end
    Label(search, text="To:").pack(ipadx=10, ipady=10, expand=False)
    global end_date_entry
    end_date_entry = StringVar()
    Entry(search, textvariable=end_date_entry).pack(ipadx=10, ipady=10, expand=False)
    # Click "Search" to start searching process button
    Button(search, text="Search", command=search_now).pack(ipadx=10, ipady=10, expand=False)

# helper method to verify the entered date format
# try section code from: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def verify_date(str):
    try:
        datetime.datetime.strptime(str, '%Y-%m-%d')
    except ValueError:
        messagebox.showinfo("Oops", "Warning! Invalid date format entry.")
    
# helper method to conduct query in sql database
def search_now():
    category_select = asset_category.get() # receive the asset category user selects
    type_select = asset_name_symbol.get() # receive the query type (name / symbol) user selects
    start_date = start_date_entry.get() # query start date user types
    end_date = end_date_entry.get() # query end date user types
    
    # verify user's date input format
    if start_date != "":  
        verify_date(start_date)
    if start_date != "":  
        verify_date(end_date)

    # error case
    if category_select == "Search by ..." or type_select == "Category of Asset is ...": 
        messagebox.showinfo("Oops", "You have not choose a search category / search method!")
        return

    dic = {
        "Commodity": "commo",
        "Stock": "stock",
        "CryptoCurrency": "crypto"
        # "Foreign Currency":
    }

    sql = "SELECT * FROM assets a, {} b WHERE a.symbol = b.symbol AND b.{}=\"{}\"".format(dic[category_select], type_select, enter_asset_box.get())
    if start_date != "" and end_date != "":
        sql += "AND a.date BETWEEN \"{}\" AND \"{}\"".format(start_date, end_date)
    # querying in database
    mycur.execute(sql)
    result = mycur.fetchall()

    # record not found
    if not result: 
        messagebox.showinfo("Oops", "Sorry, but the asset you are searching is not found...")
    else:
        # import gui from result
        messagebox.showinfo("got", result)
        pass



search()
search.mainloop()


# utilizing the calendar function
# start_text_button = Button(
#     search, text="Start Date:", command=lambda: getdate('start'))
# start_text_button.grid(row=3, column=0)

# # Start Date calendar entry
# start_date_calendar = Entry(search, textvariable=query_start_date)
# start_date_calendar.grid(row=3, column=1, padx=10, pady=10)

# end_text_button = Button(
#     search, text="End Date:", command=lambda: getdate('end'))
# end_text_button.grid(row=3, column=2)

# # End date calendar entry
# end_date_calendar = Entry(search, textvariable=query_end_date)
# end_date_calendar.grid(row=3, column=3, padx=10, pady=10)

# NOT USED: helper method for getting date (from same source as the Calendar.py)
# def getdate(type):  # 获取选择的日期
#     for date in [Calendar().selection()]:
#         if date:
#             if(type == 'start'):  # 如果是开始按钮，就赋值给开始日期
#                 query_start_date.set(date.split(" ")[0])
#                 #print(1)
#             elif(type == 'end'):
#                 query_end_date.set(date.split(" ")[0])
#                 #print(1)
