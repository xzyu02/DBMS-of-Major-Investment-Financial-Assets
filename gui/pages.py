from tkinter import *


from watchlists import watchlist_page
from search import search
from currency import currency_page

def pages(user, db, mycur):
    root = Tk()
    root.geometry('300x300')
    root.title('Welcome {}'.format(user))

    Label(root, text="User Portal", font="bold", bg="grey",fg="black",width=300).pack(ipadx=10, ipady=10, expand=False)


    watchlist_button = Button(root, text="Watchlists", command=lambda: watchlist_page(root, db, mycur, user), height=1, width = 8)
    watchlist_button.pack(ipadx=10, ipady=10, expand=True)

    currency_button = Button(root, text="Currency", command=lambda: currency_page(root, db, mycur), height=1, width = 8)
    currency_button.pack(ipadx=10, ipady=10, expand=True)

    search_button = Button(root, text="Search Assets", command=lambda: search(root, db, mycur), height=1, width = 8) # pop out a new page to the search page
    search_button.pack(ipadx=10, ipady=10, expand=True)

    exit_button = Button(root, text="Exit", command=root.destroy, height=1, width = 8)
    exit_button.pack(ipadx=10, ipady=10, expand=True)

    root.mainloop()