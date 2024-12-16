import intake
import pandas as pd

# Öffnen des Datenkatalogs
catalog = intake.open_catalog('data_catalog.yml')

# Lesen der Wetterdaten aus dem Katalog
df = catalog['weather_data'].read()

# Konvertieren der "Date"-Spalte in ein Datumsformat
df["Date"] = pd.to_datetime(df["Date"])

# Ausgabe der ersten Zeilen des DataFrames
print(df.head())

# Ausgabe des gesamten DataFrames
print(df)
# Ausgabe der Spaltennamen
print(df.columns)

# Ausgabe des frühesten Datums
print(df["Date"].min())
# Ausgabe des spätesten Datums
print(df["Date"].max())

# Ausgabe der einzigartigen Standorte
print(df["Location"].unique())
# Ausgabe der Häufigkeit der Standorte
print(df["Location"].value_counts())

# Berechnung der Standardabweichung der Minimaltemperatur pro Standort und Sortierung nach Standardabweichung
df.groupby(df["Location"]).agg({"MinTemp": "std"}).sort_values(by="MinTemp")

# Berechnung des Medians der Maximaltemperatur
df.MaxTemp.median()

# Häufigkeitsverteilung der Windrichtung um 15 Uhr
df.WindDir3pm.value_counts()

# Berechnung des 75. Perzentils und des Medians der Temperatur um 15 Uhr
df.Temp3pm.quantile(0.75)
df.Temp3pm.median()

# Anzahl der fehlenden Werte in jeder Spalte
df.isna().sum()

# Zeilen mit fehlenden Minimaltemperaturwerten
df[df.MinTemp.isna()]

# Ausgabe der Anzahl der Zeilen im DataFrame
print(len(df))

# Entfernen aller Zeilen mit fehlenden Werten
df = df.dropna(how="any")

# Ausgabe der neuen Anzahl der Zeilen und der fehlenden Werte
print(len(df))
print(df.isna().sum())

# Berechnung der Korrelation zwischen "RainTomorrow" und "RainToday"
df[["RainTomorrow", "RainToday"]].corr()

import plotly.express as px

# Erstellen eines Boxplots der Temperatur um 15 Uhr nach Standort
fig = px.box(df, x="Location", y="Temp3pm")
fig.show()

# Erstellen eines Histogramms der Temperatur um 15 Uhr
fig = px.histogram(df, x="Temp3pm")
fig.show()
