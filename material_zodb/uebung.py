from ZODB import FileStorage, DB
import transaction
from BTrees.OOBTree import OOBTree
from persistent import Persistent


class Person(Persistent):
    def __init__(self, name, adresse, alter):
        self.name = name
        self.adresse = adresse
        self.alter = alter


# Schritt 1: Datenbank und Verbindung einrichten
storage = FileStorage.FileStorage('data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

# Schritt 2: OOBTree verwenden
if 'tree' not in root:
    root['tree'] = OOBTree()  # OOBTree wird an der Datenbankwurzel gespeichert

tree = root['tree']

tree["Alice"] = Person("Alice", "Wunderland", 30)
tree["Bob"] = Person("Bob", "Wunderland", 40)
tree["Charlie"] = Person("Charlie", "Wunderland", 50)

del tree["Alice"]

transaction.commit()

# Verbindung und Speicher schließen
connection.close()
db.close()

# Öffne die Datenbank erneut, um die gespeicherten Daten zu überprüfen
storage = FileStorage.FileStorage('data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

# Drucke die Wurzel der Datenbank (zur Überprüfung)
print(root)

# Weise den OOBTree der Variable 'tree' zu
tree = root['tree']

# Iteriere über die Elemente im Baum und drucke sie
for item in tree.items():
    print(item)

# Auskommentierter Code, um die Details der Personenobjekte zu drucken
# for name, person in tree.items():
#     print(person)
#     print(person.alter)
    # print(f"Name: {person.name}, Alter: {person.alter}, Adresse: {person.adresse}")

# Verbindung und Speicher schließen
connection.close()
db.close()
