import pandas as pd
import mysql.connector

# connection to mysql database
db = mysql.connector.connect(host = "localhost",
                             user = "root",
                             password = "A1b2C3d4++",
                             db ="user")
cursor = db.cursor() # needed for Option 2
# A cursor allows you to iterate a set of rows returned by a query and process each row to get the desired information.

# get pd dataframe from query result (search as an example)
# TODO: replace query with variables and different queries, just an example query here
query = "SELECT * FROM assets a WHERE symbol=%s;"
df = pd.read_sql(query, db)

# plot a line chart
# choose one from the below 3 options
# N.B.: after deciding which option to go with, 
# reorgaize code to conform to a specific coding style

# Option 1. using pd built-in pandas.DataFrame.plot.line function
# the easiest but simplest one
plot = df.plot.line(title="Historical Price Change", x='Date', y='Price')


# Option 2. using matplotlib.pyplot -> I prefer this one for now
import matplotlib.pyplot as plt

rows = cursor.fetchall()
Date, Price = [], []

# choose from open, high, low, close as Price
for row in rows:
    Date.append(row[0])
    Price.append(row[1]) # assume the specific col of price we choose resides in index 1

# plot x-axis, Date, and y-axis, Price
plt.plot(Date, Price, color)

# name x-axis and y-axis
plt.xlabel("Date")
plt.ylabel("Price")

# name the chart
plt.title(Symbol) # to create a symbol varaible to pass in to the function

plt.show()


# Option 3. using plotly.express and graph_objs
import plotly.express as px

fig = px.line(data_frame=df
                , x='Date'
                , y='Price'
                , title="Historical Price Change")
fig.show()


db.close()
