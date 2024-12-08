# Achtung, diese Demo ist in Teilen suboptimal und dient nur zur Demonstration der Funktionsweise von FastAPI
# 1. Es findet keine Validierung der Daten statt (siehe post Methode)

import fastapi
import sqlite3
import uvicorn
import pandas as pd
import json
from typing import Generator

app = fastapi.FastAPI()

# Dependency: SQLite-Datenbankverbindung bereitstellen
def get_db_connection():
    conn = sqlite3.connect("../example.db")
    try:
        yield conn
    finally:
        conn.close()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# get data für einen bestimmten Tag
@app.get("/data/date/{date}")
def get_data(date: str, conn = fastapi.Depends(get_db_connection)):
    df = pd.read_sql_query(f"SELECT * FROM weather WHERE Date = '{date}'", conn)
    data = json.dumps(df.to_dict(orient="records"))
    return {"data": data}

# get data für einen bestimmten Ort
@app.get("/data/location/{location}")
def get_data(location: str, conn = fastapi.Depends(get_db_connection)):
    df = pd.read_sql_query(f"SELECT * FROM weather WHERE Location = '{location}'", conn)
    data = json.dumps(df.to_dict(orient="records"))
    return {"data": data}


# get data heißester Ort heute
@app.get("/data/max_temp/{date}")
def get_data(date: str, conn = fastapi.Depends(get_db_connection)):
    df = pd.read_sql_query(f"SELECT Location, MAX(MaxTemp) FROM weather WHERE Date = '{date}'", conn)
    data = json.dumps(df.to_dict(orient="records"))
    return {"data": data}

# insert new data
@app.post("/data")
def insert_data(data: dict, conn = fastapi.Depends(get_db_connection)):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (Date, Location, MinTemp) VALUES (?, ?, ?)",
                   (data["Date"], data["Location"], data["MinTemp"]))
    conn.commit()
    conn.close()
    return {"message": "Data inserted successfully"}


# erstelle docs
@app.get("/docs")
def docs():
    return fastapi.docs(app)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
