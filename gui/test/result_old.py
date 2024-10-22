import matplotlib as matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd
import mplfinance as mpf

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import mysql.connector

# for testing purpose only

# chart(db, sql)
# df = pd.read_sql(sql, db, index_col="date", parse_dates=True)
# df.index.name = 'Date'

# df_metadata = pd.read_csv("./dataset/zzz_all_metadata.csv")


# Plot the "query result" page
def result(db, query):
    df = pd.read_sql(query, db, index_col="date", parse_dates=True)
    df.index = pd.DatetimeIndex(df.index.values)

    # Plot window
    global result
    result = Tk()
    result.geometry('600x800')
    result.title('Query Result Page')

    # Row 0 introduction words
    Label(result, text="Historical Line Chart with Volume").pack(ipadx=10, ipady=10, expand=False)

    # Add symbol as a variable
    # Label(result, text="Current Asset: %s" % df.at[df.index[0], 'Symbol']).pack(side=tk.LEFT, pady=10)

    # Add asset name as a variable
    Label(result, text="Name").pack(side=tk.LEFT, pady=10)

    # Define the figure
    fig = mpf.figure(figsize=(18,12), style='yahoo')

    # Add a subplot in layout
    ax = fig.add_subplot(1,1,1)
    
    mpf.plot(df, type='line', ax=ax, mav=(20), style='yahoo')
    
    # Add a canvas containing the figure
    canvas = FigureCanvasTkAgg(fig)

    # Draw the chart
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

if __name__ == '__main__':
    db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
    sql = "SELECT a.date, a.open, a.high, a.low, a.close, a.volume FROM assets a, commo b WHERE a.symbol = b.symbol AND b.name = \"Gold\""
    result(db, sql)
    result.mainloop()