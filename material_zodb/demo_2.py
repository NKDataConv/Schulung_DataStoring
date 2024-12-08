from ZODB import FileStorage, DB
from persistent import Persistent
import transaction

storage = FileStorage.FileStorage('material_zodb/data.fs')
db = DB(storage)

# Persistenten Datentyp definieren
class Container(Persistent):
    def __init__(self):
        self.data = {}  # Normales Python-Dictionary

connection = db.open()
root = connection.root()

root['container'] = Container()
container = root['container']
container.data['some_data'] = 'some_value'
transaction.commit()

# Verbindung und Speicher schließen
connection.close()
db.close()

# Datenbank erneut öffnen und Daten schreiben
storage = FileStorage.FileStorage('material_zodb/data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

container = root['container']
container.data['more_data'] = 'another_value'
transaction.commit()

# Verbindung und Speicher schließen
connection.close()
db.close()

# Datenbank erneut öffnen und Daten lesen
storage = FileStorage.FileStorage('material_zodb/data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
container = root['container']

# Ausgabe
print(container.data)

connection.close()
db.close()