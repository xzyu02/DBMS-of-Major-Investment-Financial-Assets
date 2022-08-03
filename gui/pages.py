from tkinter import *


from watchlists import watchlist_page
def pages(user, db, mycur):
    root = Tk()
    root.geometry('300x300')
    root.title('Welcome {}'.format(user.get()))

    Label(root, text="User Portal", font="bold", bg="grey",fg="black",width=300).pack(ipadx=10, ipady=10, expand=False)

    def none():
        pass

    watchlist_button = Button(root, text="Watchlists", command=none, height=1, width = 8)
    watchlist_button.pack(ipadx=10, ipady=10, expand=True)

    from currency import currency_page
    def currency_button_func():
        currency_page(root, db, mycur)

    currency_button = Button(root, text="Currency", command=currency_button_func, height=1, width = 8)
    currency_button.pack(ipadx=10, ipady=10, expand=True)

    from search import search
    def search_button_func():
        search(root, db, mycur)

    search_button = Button(root, text="Search Assets", command=search_button_func, height=1, width = 8) # pop out a new page to the search page
    search_button.pack(ipadx=10, ipady=10, expand=True)

    exit_button = Button(root, text="Exit", command=root.destroy, height=1, width = 8)
    exit_button.pack(ipadx=10, ipady=10, expand=True)

    root.mainloop()