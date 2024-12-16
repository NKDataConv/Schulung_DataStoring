import pandas as pd

# Setzt die Pandas-Option, um alle Spalten anzuzeigen
pd.set_option('display.max_columns', None)

# Liest die CSV-Datei ein und speichert sie in einem DataFrame
df = pd.read_csv("daten/BTC_daily.csv")
# Gibt die ersten fünf Zeilen des DataFrames aus
print(df.head())

# Gibt die Datentypen der Spalten aus
print(df.dtypes)
# Konvertiert die "Date"-Spalte in das Datumsformat
df["Date"] = pd.to_datetime(df["Date"])
# Gibt die aktualisierten Datentypen der Spalten aus
print(df.dtypes)

# Gibt die ersten fünf Zeilen des DataFrames erneut aus
print(df.head())
# Setzt die "Date"-Spalte als Index des DataFrames
df = df.set_index("Date")
# alternativ:
# df.set_index("Date", inplace=True)

# Gibt die ersten fünf Zeilen des DataFrames mit dem neuen Index aus
print(df.head())
# Gibt die Spaltennamen des DataFrames aus
df.columns

# Selektionen:
# Auswahl einer einzelnen Spalte
df["Close"]

# Auswahl eines einzelnen Wertes
print(df.loc["2024-10-02", "Close"])
df.iloc[0, 0]

# Aggregation
# Fügt eine neue Spalte "year" hinzu, die das Jahr des Indexes enthält
df["year"] = df.index.year
# Gibt die ersten fünf Zeilen des DataFrames mit der neuen Spalte aus
print(df.head())
# Gruppiert den DataFrame nach Jahr und berechnet den Durchschnitt der "Open"-Spalte
df_agg = df.groupby("year").agg({"Open": "mean"})
# Gibt das aggregierte Ergebnis aus
print(df_agg)

# Fügt eine neue Spalte "month" hinzu, die den Monat des Indexes enthält
df["year"] = df.index.year
df["month"] = df.index.month
# Gibt die ersten fünf Zeilen des DataFrames mit den neuen Spalten aus
print(df.head())
# Gruppiert den DataFrame nach Jahr und Monat und berechnet den Durchschnitt der "Open"-Spalte
df_agg = df.groupby(["year", "month"]).agg({"Open": "mean"})
# Setzt den Index des aggregierten DataFrames zurück
df_agg = df_agg.reset_index()
# Gibt das aggregierte Ergebnis aus
print(df_agg)

# Sortiert den aggregierten DataFrame nach Jahr aufsteigend und Monat absteigend
df_agg.sort_values(by=["year", "month"], ascending=[True, False])
