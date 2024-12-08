import fastapi
import sqlite3
import uvicorn
import pandas as pd
import json
from pydantic import BaseModel, Field


# Pydantic Model für die Validierung
class WeatherData(BaseModel):
    Date: str
    Location: str
    MaxTemp: float
    MinTemp: float


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
def insert_data(data: WeatherData, conn = fastapi.Depends(get_db_connection)):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (Date, Location, MinTemp, MaxTemp) VALUES (?, ?, ?, ?)",
                   (data.Date, data.Location, data.MinTemp, data.MaxTemp))
    conn.commit()
    return {"message": "Data inserted successfully"}


# erstelle docs
@app.get("/docs")
def docs():
    return fastapi.docs(app)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
