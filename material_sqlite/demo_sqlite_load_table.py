import pandas as pd
import sqlite3

df = pd.read_csv('daten/BTC_daily.csv')
print(df.head())

conn = sqlite3.connect('example.db')
df.to_sql('BTC_daily', conn, if_exists='replace', index=False)
conn.close()

# --- Abfrage
conn = sqlite3.connect('example.db')
df = pd.read_sql_query("SELECT * FROM BTC_daily WHERE Date > '2024-01-01'", conn)
print(df.head())
conn.close()