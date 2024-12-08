from pymongo import MongoClient
import pandas as pd

# Verbindung zu MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Verbindung zur Datenbank und Sammlung
db = client["imdbDB"]

collection = db["movies"]

# Beispiel 1
query = {"startYear": { "$gt": 2020}}
results = collection.find(query)

for movie in results[:10]:
    print(movie)

# Beispiel 2
query = {"genres": "Drama"}
results = collection.count_documents(query)
print(results)

# Beispiel 3
query = {"genres": "Drama"}
results = collection.find(query).sort("averageRating", -1).limit(10)
for movie in results:
    print(movie)

# Beispiel 4
result = collection.aggregate([
    {"$set": {"genres": { "$split": ["$genres", ","]}}},  # Splitte String in ein Array
    { "$unwind": "$genres" },
    { "$group": { "_id": "$genres", "count": { "$sum": 1 } } },
    {"$sort": {"count": -1}},
    { "$limit": 10 }
])

for doc in result:
    print(doc)

