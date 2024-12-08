from ZODB import FileStorage, DB
import transaction
from BTrees.OOBTree import OOBTree

# Schritt 1: Datenbank und Verbindung einrichten
storage = FileStorage.FileStorage('data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

# Schritt 2: OOBTree verwenden
if 'tree' not in root:
    root['tree'] = OOBTree()  # OOBTree wird an der Datenbankwurzel gespeichert

tree = root['tree']

# Daten hinzufügen
tree['key1'] = "value1"
tree['key2'] = "value2"
tree['key3'] = "value3"

# Änderungen speichern
transaction.commit()

# Schritt 3: Daten auslesen
for key, value in tree.items():
    print(f"{key}: {value}")

# Verbindung schließen
connection.close()
db.close()
