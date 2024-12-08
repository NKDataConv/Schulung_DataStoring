from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Neue Datenbank erstellen
db = client["exampleDB"]  # Name der neuen Datenbank

# Neue Collection in der Datenbank
collection = db["exampleCollection"]

# --- 1. Dokumente einfügen ---
# Einzelnes Dokument einfügen
document = {
    "name": "John Doe",
    "age": 30,
    "profession": "Software Engineer",
    "hobbies": ["Reading", "Gaming", "Hiking"]
}
collection.insert_one(document)

# Mehrere Dokumente einfügen
documents = [
    {"name": "Jane Smith", "age": 28, "profession": "Data Scientist", "hobbies": ["Cooking", "Yoga"]},
    {"name": "Alice Brown", "age": 35, "profession": "Teacher", "hobbies": ["Painting", "Traveling"]},
    {"name": "Bob Johnson", "age": 40, "profession": "Mechanic", "hobbies": ["Fishing", "Woodworking"]}
]
collection.insert_many(documents)

# --- 2. Dokumente abfragen ---
print("Alle Dokumente in der Collection:")
for doc in collection.find():
    print(doc)

# --- 3. Dokument aktualisieren ---
# Einzelnes Dokument aktualisieren (z. B. Alter ändern)
collection.update_one({"name": "John Doe"}, {"$set": {"age": 31}})
# Mehrere Dokumente aktualisieren (z. B. Beruf ändern)
collection.update_many({"profession": "Teacher"}, {"$set": {"profession": "Educator"}})

# Ergebnisse überprüfen
print("\nNach dem Update:")
for doc in collection.find():
    print(doc)

# --- 4. Dokument löschen ---
# Einzelnes Dokument löschen
collection.delete_one({"name": "Bob Johnson"})

# Mehrere Dokumente löschen (z. B. basierend auf einer Bedingung)
collection.delete_many({"age": {"$lt": 30}})

# Ergebnisse nach dem Löschen überprüfen
print("\nNach dem Löschen:")
for doc in collection.find():
    print(doc)

# --- Cleanup: Datenbank löschen ---
client.drop_database("exampleDB")  # Datenbank vollständig entfernen
print("\nDatenbank gelöscht.")
