import pandas as pd
import mplfinance as mpf
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# connection to mysql database
db = mysql.connector.connect(host = "localhost",
                             user = "root",
                             password = "A1b2C3d4&",
                             db ="564project")

# get pd dataframe from query result (search as an example)
# TODO: replace query with variables and different queries, just an example query here
query = "SELECT * FROM assets a WHERE symbol=%a;"

daily = pd.read_sql(query, db)
daily.index.name = 'Date'

# plot daily candlestick chart with volume
fig = mpf.plot(daily,type='candle',mav=(20),volume=True, 
                       style='yahoo')

# plot daily candlestick chart with volume
fig = mpf.plot(daily,type='line',mav=(20),volume=True, 
                       style='yahoo')

canvas = FigureCanvasTkAgg(fig)

db.close()
