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
db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
sql = "SELECT a.date, a.open, a.high, a.low, a.close, a.volume FROM assets a, commo b WHERE a.symbol = b.symbol AND b.name = \"Gold\""
# chart(db, sql)
df = pd.read_sql(sql, db, index_col="date", parse_dates=True)
df.index = pd.DatetimeIndex(df.index.values)

df_metadata = pd.read_csv("./dataset/zzz_all_metadata.csv")

# def drawChart(df):
#     # Generate the plots and retunr the figure
#     fig, _ = mpf.plot(df, type='line', mav=(20), volume=True, style='yahoo')

#     # Add a canvas containing the figure
#     canvas = FigureCanvasTkAgg(fig)

#     # Draw the chart
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# Plot the "query result" page
def result():
    
    # Plot window
    global result
    result = Tk()
    result.geometry('300x400')
    result.title('Query Result Page')

    # Row 0 introduction words
    Label(result, text="Historical Line Chart with Volume").pack(ipadx=10, ipady=10, expand=False)

    
    symbol = df.at[df.index[0], 'Symbol']
    name = df_metadata.loc[df_metadata["Symbol"] == symbol, "Name"].to_string(index=None).strip()
    # Add symbol
    Label(result, text="Current Asset: %s" % symbol).pack(ipadx=10, ipady=10, expand=False)

    # Add asset name
    Label(result, text="Name: %s" % name).pack(ipadx=10, ipady=10, expand=False)

    # Define the figure
    fig = mpf.figure(figsize=(18,12), style='yahoo')

    # Add a subplot in layout
    ax = fig.add_subplot(1,1,1)
    
    mpf.plot(df, type='line', ax=ax, mav=(20), style='yahoo')
    
    # Add a canvas containing the figure
    canvas = FigureCanvasTkAgg(fig)

    # Draw the chart
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    result()
    result.mainloop()
