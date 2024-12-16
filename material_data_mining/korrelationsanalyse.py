import intake
import pandas as pd
import numpy as np
import plotly.express as px

# Öffnen des Datenkatalogs
catalog = intake.open_catalog('data_catalog.yml')

# Lesen der Wetterdaten aus dem Katalog
df = catalog['weather_data'].read()

# Entfernen nicht benötigter Spalten
df = df.drop(columns=["Date", "Location", "WindGustDir", "WindDir9am", "WindDir3pm"])

# Umwandlung der "RainToday" und "RainTomorrow" Spalten von Ja/Nein zu 1/0
rain_map = {"No": 0, "Yes": 1}
df.RainToday = df.RainToday.map(rain_map)
df.RainTomorrow = df.RainTomorrow.map(rain_map)

# Berechnung der Korrelationsmatrix
correlation_matrix = df.corr()

# Ausgabe der Korrelationsmatrix
print(correlation_matrix)

# Visualisierung der Korrelationsmatrix mit Plotly
fig = px.imshow(
    correlation_matrix,
    text_auto=True
)
fig.show()