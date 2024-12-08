from pymongo import MongoClient
import pandas as pd

# Verbindung zu MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Verbindung zur Datenbank und Sammlung
db = client["imdbDB"]

# Liste aller Collections
collections = db.list_collection_names()
print("Collections:", collections)

collection = db["movies"]

# Beispiel-Dokument aus der 'movies' Collection
sample_document = collection.find_one()
print("Sample Document:", sample_document)


# Beispielabfrage: Finde alle Filme aus dem Jahr 2000
query = {"startYear": 2000}
results = collection.find(query)

# Ergebnisse anzeigen
for movie in results[:10]:
    print(movie)

# in pandas dataframe umwandeln
# Query muss erneut ausgeführt werden, da results bereits durchlaufen wurde
data = list(results)
df = pd.DataFrame(data)
print(df.columns)
print(df.head())


# Anzahl an Filmen in der Collection:
result = collection.count_documents({})
print("Anzahl an Filmen:", result)


# Der längste Film:
result = collection.find({}, {"primaryTitle": 1, "runtimeMinutes": 1, "_id": 0}) \
                                  .sort("runtimeMinutes", -1) \
                                  .limit(1)
for movie in result:
    print(movie)


# Anzahl an Filmen im Jahr 1965:
result = collection.count_documents({ "startYear": 1965 })
print("Anzahl an Filmen im Jahr 1965:", result)


# Anzahl an Filmen pro Jahr:
result = collection.aggregate([
    { "$group": { "_id": "$startYear", "count": { "$sum": 1 } } },
    { "$sort": { "_id": 1 } } # Optional: Sortiere nach Jahr
])
for doc in result:
    print(doc)


# Welcher Regisseur hat die meisten Filme gemacht?
result = db.crew.aggregate([
    { "$unwind": "$directors" },                          # Auflösen des Arrays `directors`
    { "$group": { "_id": "$directors", "count": { "$sum": 1 } } }, # Zähle Filme pro Regisseur
    { "$sort": { "count": -1 } },                           # Sortiere absteigend nach Anzahl
    { "$limit": 10 }                                      # Begrenze auf die Top 10
])
for directors in result:
    print(directors)


# Regisseur des längsten Films:
pipeline = [
    {"$sort": {"runtimeMinutes": -1}},  # Sortiere nach Laufzeit (absteigend)
    {"$limit": 1},  # Nur den längsten Film nehmen
    {"$lookup": {
        "from": "crew",
        "localField": "tconst",
        "foreignField": "tconst",
        "as": "crew_info"
    }},
    {"$unwind": "$crew_info"},  # Auflösen von crew_info
    {"$project": {
        "primaryTitle": 1,
        "runtimeMinutes": 1,
        "crew_info.directors": 1
    }}
]

# Aggregation ausführen
result = list(collection.aggregate(pipeline))
df = pd.DataFrame(result)



# Achtung: lange Ausführungszeit
# Beispielabfrage für Aggregation: Finde alle Filme und die zugehörigen Regisseure
pipeline = [
    {"$lookup": {
        "from": "crew",
        "localField": "tconst",
        "foreignField": "tconst",
        "as": "crew_info"
    }},
    {"$unwind": "$crew_info"},
    {"$project": {
        "primaryTitle": 1,
        "startYear": 1,
        "crew_info.directors": 1
    }}
]
result = db.movies.aggregate(pipeline)
for doc in result:
    print(doc)