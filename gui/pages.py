from tkinter import *

def pages(username):
    root = Tk()
    root.geometry('300x300')
    root.title('Welcome %s'.format(username))

    def none():
        pass

    watchlist_button = Button(root, text="Watchlists", command=none, height=1, width = 8)
    watchlist_button.pack(ipadx=10, ipady=10, expand=True)

    portfolio_button = Button(root, text="Portfolio", command=none, height=1, width = 8)
    portfolio_button.pack(ipadx=10, ipady=10, expand=True)

    search_button = Button(root, text="Search", command=search_assets, height=1, width = 8) # pop out a new page to the search page
    search_button.pack(ipadx=10, ipady=10, expand=True)

    exit_button = Button(root, text="Exit", command=root.destroy, height=1, width = 8)
    exit_button.pack(ipadx=10, ipady=10, expand=True)

    root.mainloop()