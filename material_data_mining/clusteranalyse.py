import pandas as pd  # Importiere die Pandas-Bibliothek und benenne sie als 'pd'
pd.set_option("display.max_columns", None)  # Setze die Pandas-Option, um alle Spalten anzuzeigen
df = pd.read_csv("daten/cars.csv")  # Lese die CSV-Datei 'cars.csv' in ein DataFrame 'df' ein

print(df.head())  # Gib die ersten fünf Zeilen des DataFrames aus

print(df.describe())  # Gib eine statistische Zusammenfassung des DataFrames aus

# definiere cluster:
def assign_cluster(price):  # Definiere eine Funktion zur Zuordnung von Clustern basierend auf dem Preis
    if price < 25:  # Wenn der Preis kleiner als 25 ist
        return "komfort"  # Ordne dem Cluster 'komfort' zu
    elif price < 50:  # Wenn der Preis kleiner als 50 ist
        return "mittelklasse"  # Ordne dem Cluster 'mittelklasse' zu
    else:  # Für alle anderen Fälle
        return "premium"  # Ordne dem Cluster 'premium' zu

df["cluster"] = df["Purchase_price"].apply(assign_cluster)  # Wende die Funktion auf die Spalte 'Purchase_price' an und speichere die Ergebnisse in einer neuen Spalte 'cluster'

df["cluster"].value_counts()  # Zähle die Häufigkeit der einzelnen Cluster und gib sie aus

