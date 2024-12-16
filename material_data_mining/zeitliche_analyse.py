import intake
import pandas as pd
import numpy as np
import plotly.express as px

# Öffnet den Datenkatalog
catalog = intake.open_catalog('data_catalog.yml')

# Liest die Wetterdaten aus dem Katalog
df = catalog['weather_data'].read()

# Konvertiert die "Date"-Spalte in ein Datumsformat
df["Date"] = pd.to_datetime(df["Date"])

# Filtert die Daten für den Standort "Melbourne"
df = df[df.Location == "Melbourne"]

# Erstellt ein Streudiagramm für Sonnenschein über die Zeit
fig = px.scatter(df, x="Date", y="Sunshine")
fig.show()

# Erstellt ein Liniendiagramm für Sonnenschein über die Zeit
fig = px.line(df, x="Date", y="Sunshine")
fig.show()

# Berechnet den gleitenden Durchschnitt des Sonnenscheins über ein 30-Tage-Fenster
df["rolling_sunshine"] = df["Sunshine"].rolling(window=30).mean()

# Erstellt ein Liniendiagramm für den gleitenden Durchschnitt des Sonnenscheins
fig = px.line(df, x="Date", y="rolling_sunshine")
fig.show()

# Untersucht, ob das Maximum der Temperatur im Laufe der Jahre zunimmt
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month

# Aggregiert die Daten, um das monatliche Maximum der Temperatur zu berechnen
df_agg = df.groupby(["year", "month"]).agg({"MaxTemp": "max", "Date": "min"}).reset_index()

# Erstellt ein Liniendiagramm für das monatliche Maximum der Temperatur
fig = px.line(df_agg, x="Date", y="MaxTemp")
fig.show()

# Konvertiert die Monatsnummer in den Monatsnamen
df_agg["month"] = df_agg["Date"].dt.month_name()

# Erstellt ein polares Liniendiagramm, um die monatlichen Maximaltemperaturen im Jahresvergleich darzustellen
fig = px.line_polar(df_agg, r="MaxTemp", theta="month", color="year", line_close=True)
fig.show()