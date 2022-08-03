from tkinter import *

def watchlist_page(root):
    # window
    global watchlists
    home = Tk()
    # page
    global page
    page = Toplevel(root)
    home.geometry('300x450')
    home.title('My Watchlist')
    # title
    Label(home, text="Watchlist", font="bold", bg="grey",fg="black",width=300).pack(ipadx=10, ipady=10, expand=False)
    # add new watchlist
    Button(home, text="Add", command=registration, height=1, width = 10).pack(ipadx=10, ipady=10, expand=True)
