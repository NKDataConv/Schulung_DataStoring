import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLAlchemy engine
engine = create_engine('postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase')

df = pd.read_csv("daten/cars.csv")
df.head()

# Use the SQLAlchemy engine with to_sql
df.to_sql('cars', engine, if_exists='replace', index=False)

## Abfrage
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM cars"))
    for row in result:
        print(row)

# alternativ mit pandas
df = pd.read_sql_query("SELECT * FROM cars", engine)
df.head()

engine.dispose()
