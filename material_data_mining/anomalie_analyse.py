import intake
import pandas as pd
import numpy as np
import plotly.express as px

# Öffnen des Datenkatalogs
catalog = intake.open_catalog('data_catalog.yml')

# Lesen der Bitcoin-Daten
df = catalog['bitcoin_data'].read()

# Konvertieren der "Date"-Spalte in ein Datumsformat
df["Date"] = pd.to_datetime(df["Date"])
# Extrahieren des Jahres aus dem Datum
df["year"] = df["Date"].dt.year

# Gruppieren der Daten nach Jahr und Berechnen des durchschnittlichen Volumens
df_agg = df.groupby("year").agg({"Volume": "mean"}).reset_index()
print(df_agg)

# Erstellen einer Liniendiagramm für das durchschnittliche Volumen pro Jahr
px.line(df_agg, x="year", y="Volume").show()

# Erstellen eines Streudiagramms für das Volumen über die Zeit
px.scatter(df, x="Date", y="Volume").show()

# Berechnen des gleitenden Durchschnitts des Volumens über ein Fenster von 30 Tagen
df["rolling_volume"] = df["Volume"].rolling(window=30).mean()

# Berechnen der Differenz zwischen dem aktuellen Volumen und dem gleitenden Durchschnitt
df["volume_diff"] = df["Volume"] - df["rolling_volume"]
# Erstellen eines Streudiagramms für die Volumendifferenz über die Zeit
px.scatter(df, x="Date", y="volume_diff").show()

# Berechnen der Standardabweichung des gleitenden Volumens
df["rolling_volume_std"] = df["Volume"].rolling(window=30).std()
# Berechnen des Z-Scores für die Volumendifferenz
df["z_score"] = df["volume_diff"] / df["rolling_volume_std"]
# Filtern der Daten für Z-Scores mit einem absoluten Wert größer als 4
df = df[df.z_score.abs() > 4]

print(df)
# Sortieren der Daten nach Z-Score in absteigender Reihenfolge
print(df.sort_values(by="z_score", ascending=False))

# Lesen der Wetterdaten
df = catalog['weather_data'].read()
# Erstellen eines Boxplots für die Minimaltemperatur
px.box(df, y="MinTemp").show()

max_z_score = 0

# Iterieren über alle einzigartigen Standorte in den Wetterdaten
for location in df.Location.unique():
    # Filtern der Daten für den aktuellen Standort
    df_location = df.loc[df.Location == location, :].copy()
    # Berechnen des gleitenden Durchschnitts der Minimaltemperatur
    df_location["rolling_min_temp"] = df_location["MinTemp"].rolling(window=30).mean()
    # Berechnen der absoluten Differenz zwischen der aktuellen und der gleitenden Minimaltemperatur
    df_location["min_temp_diff"] = abs(df_location["MinTemp"] - df_location["rolling_min_temp"])
    # Berechnen der Standardabweichung der gleitenden Minimaltemperatur
    df_location["rolling_min_temp_std"] = df_location["MinTemp"].rolling(window=30).std()
    # Berechnen des Z-Scores für die Minimaltemperaturdifferenz
    df_location["z_score"] = df_location["min_temp_diff"] / df_location["rolling_min_temp_std"]
    # Aktualisieren des maximalen Z-Scores, falls der aktuelle Standort einen höheren Wert hat
    if df_location.z_score.max() > max_z_score:
        max_z_score = df_location.z_score.max()
        print(location)

# Extrahieren des Jahres und Monats aus dem Datum
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month

# Gruppieren der Daten nach Standort, Jahr und Monat und Berechnen von Temperaturstatistiken
df_agg = df.groupby(["Location", "year", "month"]).agg({"MinTemp": ["mean", "min", "max"], "Date": "min"}).reset_index()
# Umbenennen der Spalten
df_agg.columns = ["Location", "year", "month", "MeanTemp", "MinTemp", "MaxTemp", "Date"]
print(df_agg)

# Erstellen eines Streudiagramms für die Minimaltemperatur pro Monat für die ersten 10 Standorte
for location in df_agg.Location.unique()[:10]:
    df_location = df_agg.loc[df_agg.Location == location, :].copy()

    px.scatter(df_location, x="month", y="MinTemp", color="Location").show()
