import datetime
from unicodedata import category
from numpy.core.defchararray import center
from tkinter import *
from tkinter import ttk
from numpy import pad
from sqlalchemy import null  
import mysql.connector 

# handle connecting to database
# TODO: pending further modification; used in search_now() method at line 111
# NOTE: comment these db session to see the GUI interface; this code may not run
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="A1b2C3d4&",
                             db="users")
cursor = db.cursor()
    
# Below is the code for plotting the "search" page; can be packed into the search_asset() (commented line 18) 
# basic layout follow plotted diagram published
#def search_asset():

# plot window
search_assets = Tk()
search_assets.geometry('800x500')
search_assets.title('Search for an asset') 
    
# ROW 0 introducing words
begin_label = Label(
    search_assets, text="Search assets by type in the name / symbol:")
begin_label.grid(row=0,column=1)

# Begin Row 1, noting words
note_text_1 = Label(search_assets, text="You are searching:")
note_text_1.grid(row=1, column=0)

# Entry box for users to type asset name/symbol
enter_asset_box = Entry(search_assets)
enter_asset_box.grid(row=1, column=1)

# Drop down box #1: Category of the assets to search
asset_category = ttk.Combobox(search_assets, value=[
    "Category of Asset is ...", "Commodity", "CryptoCurrency", "Foreign Currency", "Stock"])
asset_category.current(0)
asset_category.grid(row=1, column=2)

# Drop down box #2: Search by symbol or name
asset_name_symbol = ttk.Combobox(
    search_assets, value=["Search by ...", "Symbol", "Name"])
asset_name_symbol.current(0)
asset_name_symbol.grid(row=1,column=3)

# ROW 2: entry for user enter start/end time 
start_end_text = Label(
    search_assets, text="Enter the time period you want to query\n NOTE: enter date in yyyy-mm-dd format")
start_end_text.grid(row=2, column=1)

start_text = Label(search_assets, text="Start from:")
start_text.grid(row=4, column=0)

start_date_entry = Entry(search_assets)
start_date_entry.grid(row=4, column=1)

end_text = Label(search_assets, text="To:")
end_text.grid(row=4, column=2)

end_date_entry = Entry(search_assets)
end_date_entry.grid(row=4, column=3)

# helper method to verify the entered date format
# try section code from: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def verify_date(str):
    try:
        datetime.datetime.strptime(str, '%Y-%m-%d')
    except ValueError:
        pop_msg = Label(
            search_assets, text="Warning! Invalid date format entry.")
        pop_msg.grid(row=6, column=0)
    
# helper method to conduct query in sql database
def search_now():
    category_select = asset_category.get() # receive the asset category user selects
    type_select = asset_name_symbol.get() # receive the query type (name / symbol) user selects
    start_date = str(start_date_entry.get()) # query start date user types
    end_date = str(end_date_entry.get()) # query end date user types
    
    # verify user's date input format 
    verify_date(start_date)
    verify_date(end_date)

    # handle each selection case
    # in total, it should be 4 * 1 + 1 (query by symbol) + 1(non selected) + 1(not found) = 7 cases
    # TODO: case #5 & #6 subject to change due to lack of metadata / non-cleaning work done
    if category_select == "Search by ..." or type_select == "Category of Asset is ...": # case 1 either dropbox not selected
        pop_msg = Label(
            search_assets, text="You have not choose a search category / search method!")
        pop_msg.grid(row=6, column=0)
    if type_select == "symbol": #2 any time when user query via symbol
        sql = "SELECT * FROM assets a WHERE symbol=%s"
    if category_select == "Commodity" and type_select == "Name": #3 query name of a commodity
        sql = "SELECT * FROM assets a, commo c WHERE a.symbol=c.symbol AND c.name=%s"    
    if category_select == "Stock" and type_select == "Name": #4 query name of a stock
        sql = "SELECT * FROM assets a, stock s WHERE a.symbol=s.symbol AND s.name=%s"
    if category_select == "CryptoCurrency" and type_select == "Name": #5 query name of a cryptocurrency
        sql = "SELECT * FROM assets a, crypto c WHERE a.symbol = c.symbol AND c.name=%s"
    if category_select == "Foreign Currency" and type_select == "Name": #6 query name of a foreign currency
        sql = "SELECT * FROM assets a, currency c WHERE a.symbol = c.symbol AND c.name=%s"

    # done querying in database
    asset_querying = enter_asset_box.get() # receive the name/symbol of asset user enters
    entered_asset = (asset_querying, )
    result = cursor.execute(sql, entered_asset)

    if not result: # case 7: record not found
        result = "Sorry, but the asset you are searching is not found..."

    # print out the searched result in the diagram
    # TODO: this part can be adjusted if new page need to created for displaying diagram stuff
    searched_label = Label(search_assets, text=result)
    searched_label.grid(row=6, column=0)


# Click "Search" to start searching process button
search_button = Button(search_assets, text="Search", command=search_now)
search_button.grid(row=5, column=1)


if __name__ == "__main__":
    search_assets.mainloop()


# utilizing the calendar function
# start_text_button = Button(
#     search_assets, text="Start Date:", command=lambda: getdate('start'))
# start_text_button.grid(row=3, column=0)

# # Start Date calendar entry
# start_date_calendar = Entry(search_assets, textvariable=query_start_date)
# start_date_calendar.grid(row=3, column=1, padx=10, pady=10)

# end_text_button = Button(
#     search_assets, text="End Date:", command=lambda: getdate('end'))
# end_text_button.grid(row=3, column=2)

# # End date calendar entry
# end_date_calendar = Entry(search_assets, textvariable=query_end_date)
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
