import pandas as pd
import mplfinance as mpf
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def graph(db, query):
    daily = pd.read_sql(query, db, index_col="date", parse_dates=True)
    daily.index = pd.DatetimeIndex(daily.index.values)
    # plot daily candlestick chart with volume
    fig = mpf.plot(daily,type='line',mav=(20),volume=True, style='yahoo')

# test only
'''
db = mysql.connector.connect(host = "localhost", user = "root", password = "A1b2C3d4&", db ="564project")
sql = "SELECT a.date, a.open, a.high, a.low, a.close, a.volume FROM assets a, commo b WHERE a.symbol = b.symbol AND b.name = \"Gold\""
graph(db, sql)
'''


