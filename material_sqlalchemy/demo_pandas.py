import pandas as pd
from sqlalchemy import create_engine

# Datenbankverbindung
engine = create_engine('sqlite:///example.db', echo=True)

df = pd.read_sql("SELECT * FROM sales", engine)
print(df.head())

df = pd.read_sql("SELECT * FROM products", engine)
print(df.head())

df = pd.read_sql("SELECT sales_extended.product_name, products.description, sales_extended.quantity_sold FROM sales_extended JOIN products ON sales_extended.product_id = products.id", engine)
print(df.head())