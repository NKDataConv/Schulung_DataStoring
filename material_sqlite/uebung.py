# Importiere die notwendigen Bibliotheken
import sqlite3
import pandas as pd

# Lese die CSV-Datei 'weatherAUS.csv' in ein DataFrame ein
df = pd.read_csv('daten/weatherAUS.csv')
# Zeige die ersten fünf Zeilen des DataFrames an
print(df.head())

# Erstelle eine Verbindung zu einer SQLite-Datenbank (erstellt 'example.db' falls nicht vorhanden)
conn = sqlite3.connect('example.db')
# Speichere das DataFrame in der SQLite-Datenbank in einer Tabelle namens 'weather'
# Falls die Tabelle bereits existiert, ersetze sie
df.to_sql('weather', conn, if_exists='replace', index=False)
# Schließe die Datenbankverbindung
conn.close()

# --- Abfrage Wetterdaten in Sydney
# Erstelle erneut eine Verbindung zur SQLite-Datenbank
conn = sqlite3.connect('example.db')
# Führe eine SQL-Abfrage aus, um alle Wetterdaten für den Standort 'Sydney' abzurufen
df = pd.read_sql_query("SELECT * FROM weather WHERE Location = 'Sydney'", conn)
# Zeige die ersten fünf Zeilen des abgerufenen DataFrames an
print(df.head())

# Schließe die Datenbankverbindung
conn.close()

# --- Alternativ Abfrage ohne Pandas
# Erstelle erneut eine Verbindung zur SQLite-Datenbank
conn = sqlite3.connect('example.db')
# Erstelle einen Cursor-Objekt, um SQL-Abfragen auszuführen
cursor = conn.cursor()
# Führe eine SQL-Abfrage aus, um alle Wetterdaten für den Standort 'Sydney' abzurufen
cursor.execute("SELECT * FROM weather WHERE Location = 'Sydney'")
# Hole alle Zeilen des Abfrageergebnisses
rows = cursor.fetchall()
# Iteriere über die Zeilen und drucke jede Zeile
for row in rows:
    print(row)
# Schließe die Datenbankverbindung
conn.close()
