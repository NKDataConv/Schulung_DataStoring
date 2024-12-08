import pandas as pd
import sqlite3


df = pd.read_csv("daten/user_data.csv", sep=";")

print(df.head())

## connect to sqlite and load data into user_data table
conn = sqlite3.connect("example.db")

# schreibe zu sql mit primary key: index
df.to_sql("user_data", conn, if_exists="replace", index=True)

# --- Abfrage
df = pd.read_sql_query("SELECT * FROM user_data", conn)
df.head()
