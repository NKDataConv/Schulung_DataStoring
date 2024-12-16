import pandas as pd

df = pd.read_csv("daten/cars.csv")

df.to_json("daten/cars.json", orient="records")

