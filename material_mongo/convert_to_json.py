import pandas as pd
import json


def convert_tsv_to_json(tsv_path, json_path, chunksize=100000):
    """
    Konvertiert eine TSV-Datei in eine JSON-Datei und stellt sicher, dass numerische Werte korrekt gespeichert werden.

    Args:
        tsv_path (str): Pfad zur Eingabe-TSV-Datei.
        json_path (str): Pfad zur Ausgabe-JSON-Datei.
        chunksize (int): Größe der Datenblöcke beim Einlesen.
    """
    with open(json_path, 'w') as json_file:
        for chunk in pd.read_csv(tsv_path, sep='\t', chunksize=chunksize):
            # Fehlende Werte auffüllen
            chunk = chunk.fillna('')

            # Typkonvertierung: Spaltennamen anpassen!
            if 'runtimeMinutes' in chunk.columns:
                chunk['runtimeMinutes'] = pd.to_numeric(chunk['runtimeMinutes'], errors='coerce').fillna(0).astype(int)

            if 'startYear' in chunk.columns:
                chunk['startYear'] = pd.to_numeric(chunk['startYear'], errors='coerce').fillna(0).astype(int)

            if 'endYear' in chunk.columns:
                chunk['endYear'] = pd.to_numeric(chunk['endYear'], errors='coerce').fillna(0).astype(int)

            # Konvertiere zu JSON
            chunk.to_json(json_file, orient='records', lines=True)

# Convert title.basics.tsv to JSON
convert_tsv_to_json("/tmp/title.basics.tsv", "/tmp/movies.json")

# Convert title.crew.tsv to JSON
convert_tsv_to_json("/tmp/title.crew.tsv", "/tmp/crew.json") 