import pandas as pd
import mplfinance as mpf
import mysql.connector

def graph(db, query):
    df = pd.read_sql(query, db, index_col="date", parse_dates=True)
    df.index = pd.DatetimeIndex(df.index.values)
    plt = mpf.plot(df, type='line',mav=(20), volume=True, style='yahoo')

