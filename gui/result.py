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

df = pd.read_sql(sql, db, index_col="date", parse_dates=True)

# def chart(db, query):
#     daily = pd.read_sql(sql, db, index_col="date", parse_dates=True)
#     daily.index = pd.DatetimeIndex(daily.index.values)
#     # plot daily candlestick chart with volume
#     fig = mpf.plot(daily,type='line',mav=(20),volume=True, style='yahoo')

# test only

# db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
# sql = "SELECT a.date, a.open, a.high, a.low, a.close, a.volume FROM assets a, commo b WHERE a.symbol = b.symbol AND b.name = \"Gold\""
# chart(db, sql)

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

    # Add symbol
    Label(result, test="Symbol").pack(side=tk.LEFT, pady=10)

    # Add asset name
    Label(result, test="Name").pack(side=tk.LEFT, pady=10)

    # Insert the mpf line chart
    # Generate the plots and return the figure
    fig, _ = mpf.plot(df, type='line', mav=(20), volume=True, style='yahoo')

    # Add a canvas containing the figure
    canvas = FigureCanvasTkAgg(fig)

    # Draw the chart
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    result()
    result.mainloop()
