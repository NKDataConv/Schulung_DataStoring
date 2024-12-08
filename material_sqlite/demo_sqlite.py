import sqlite3

# 1. Verbindung zur SQLite-Datenbank herstellen (wenn die Datei nicht existiert, wird sie erstellt)
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# 2. Tabelle erstellen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')
print("Tabelle 'users' erstellt.")

# 3. Daten einfügen
try:
    cursor.execute(f"INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com')")
    cursor.execute(f"INSERT INTO users (name, age, email) VALUES ('Bob', 25, 'bob@example.com')")
    cursor.execute(f"INSERT INTO users (name, age, email) VALUES ('Charlie', 35, 'charlie@example.com')")
    print("Daten eingefügt.")
except sqlite3.IntegrityError:
    print("Einige Einträge existieren bereits.")

# Änderungen bestätigen
connection.commit()

# 4. Daten abfragen
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("Alle Benutzer:")
for user in users:
    print(user)

# 5. Daten aktualisieren
cursor.execute(f"UPDATE users SET age = 32 WHERE name = 'Alice'")
print("Alter von Alice aktualisiert.")

# Änderungen bestätigen
connection.commit()

# 6. Daten abfragen mit Bedingung
cursor.execute("SELECT * FROM users WHERE age > 30")
older_users = cursor.fetchall()
print("Benutzer älter als 30:")
for user in older_users:
    print(user)

# 7. Daten löschen
cursor.execute(f"DELETE FROM users WHERE name = 'Charlie'")
print("Benutzer 'Charlie' gelöscht.")

# Änderungen bestätigen
connection.commit()

# 8. Tabelle leeren
cursor.execute("DELETE FROM users")
print("Alle Benutzer gelöscht.")

# Änderungen bestätigen und Verbindung schließen
connection.commit()
connection.close()
