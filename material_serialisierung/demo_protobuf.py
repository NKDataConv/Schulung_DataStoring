# automatische Code Generierung mit protoc
# ../protoc/bin/protoc.exe --python_out=. person.proto

from material_serialisierung.person_pb2 import Person

person = Person(name="Max", age=30, city="Berlin")

# Serialisieren und in eine Datei schreiben
with open("material_serialisierung/person.bin", "wb") as file:
    file.write(person.SerializeToString())


# Aus der Datei lesen und deserialisieren
with open("material_serialisierung/person.bin", "rb") as file:
    person_data = file.read()

# Erstellen einer neuen Person-Nachricht und Daten deserialisieren
person = Person()
person.ParseFromString(person_data)

# Ausgabe der gelesenen Daten
print(f"Name: {person.name}, Alter: {person.age}, Stadt: {person.city}")
