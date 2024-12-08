from ZODB import FileStorage, DB
import transaction
import persistent

# Schritt 1: Storage und Datenbank erstellen
storage = FileStorage.FileStorage('material_zodb/data.fs')
db = DB(storage)

# Schritt 2: Verbindung zur Datenbank herstellen
connection = db.open()
root = connection.root()

# Schritt 3: Persistenten Datentyp definieren
class Person(persistent.Persistent):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Schritt 4: Daten hinzufügen
if 'people' not in root:
    root['people'] = {}  # Ein Dictionary für Personen

people = root['people']
people['alice'] = Person("Alice", 30)
people['bob'] = Person("Bob", 25)

# Änderungen speichern
transaction.commit()

# Schritt 5: Daten lesen
for name, person in people.items():
    print(f"Name: {person.name}, Alter: {person.age}")

# Verbindung und Speicher schließen
connection.close()
db.close()