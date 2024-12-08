import json

# Beispiel-Daten
data = {
    "Name": "Max",
    "Alter": 30,
    "Stadt": "Berlin"
}

# Schreiben der Daten in eine JSON-Datei
with open('daten/example_data.json', 'w') as file:
    json.dump(data, file)

# Lesen der Daten aus einer JSON-Datei
with open('daten/example_data.json', 'r') as file:
    data = json.load(file)

print(data)  # Ausgabe der gelesenen Daten


import pandas as pd

data = {
    "Name": ["Max", "Anna"],
    "Alter": [30, 25],
    "Stadt": ["Berlin", "Hamburg"]
}

df = pd.DataFrame(data)

# Schreiben des DataFrames in eine JSON-Datei
df.to_json('daten/example_data_pd.json', orient='records')  # `orient='records'` für eine Liste von Objekten

# Lesen der JSON-Datei als DataFrame
df = pd.read_json('daten/example_data_pd.json')
print(df)  # Ausgabe des DataFrames
