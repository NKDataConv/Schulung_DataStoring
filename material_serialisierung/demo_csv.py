import csv

# Beispiel-Daten
data = [
    ["Name", "Alter", "Stadt"],
    ["Max", 30, "Berlin"],
    ["Anna", 25, "Hamburg"]
]

# Schreiben der Daten in eine CSV-Datei
with open('daten/example_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


# Lesen der Daten aus einer CSV-Datei
with open('daten/example_data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Ausgabe der gelesenen Zeilen


import pandas as pd

df = pd.DataFrame(data)

# Schreiben des DataFrames in eine CSV-Datei
df.to_csv('daten/example_data_pd.csv', index=False)  # `index=False` um den Index nicht mitzuschreiben

# Lesen der CSV-Datei als DataFrame
df = pd.read_csv('daten/example_data_pd.csv')
print(df)  # Ausgabe des DataFrames