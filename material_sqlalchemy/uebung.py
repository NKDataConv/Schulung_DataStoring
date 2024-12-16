from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
import pandas as pd

# Datenbankverbindung herstellen
engine = create_engine('postgresql+pg8000://myuser:mypassword@localhost:5432/mydatabase', echo=True)

# Basisklasse für die Deklaration von Tabellen
Base = declarative_base()

# Tabelle 'user_data' definieren
class User(Base):
    __tablename__ = 'user_data'

    # Spalten der Tabelle
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Email = Column(String)
    Adresse = Column(String)
    Geburtsdatum = Column(Date)

# Tabellen in der Datenbank erstellen
Base.metadata.create_all(engine)

# Session für die Datenbankinteraktion erstellen
Session = sessionmaker(bind=engine)
session = Session()

# CSV-Datei einlesen
df = pd.read_csv("daten/user_data.csv", sep=";")
# Geburtsdatum in Datumsformat umwandeln
df["Geburtsdatum"] = pd.to_datetime(df["Geburtsdatum"])
# Daten in ein Dictionary umwandeln
data = df.to_dict(orient='records')

# Ersten Datensatz ausgeben
print(data[0])

# Benutzerobjekte aus den Dictionary-Daten erstellen
users_to_insert = []
for row in data:
    user = User(**row)
    users_to_insert.append(user)

# Alternativ: Benutzerobjekte mit pandas iterrows erstellen
for row in df.iterrows():
    user = User(Name=row[1]["Name"], Email=row[1]["Email"], Adresse=row[1]["Adresse"], Geburtsdatum=row[1]["Geburtsdatum"])
    users_to_insert.append(user)

# Alle Benutzerobjekte in die Datenbank einfügen
session.add_all(users_to_insert)
session.commit()
print("Daten wurden erfolgreich eingefügt!")

# Neue Session für weitere Abfragen erstellen
Session = sessionmaker(bind=engine)
session = Session()

# Alle Benutzer aus der Datenbank abfragen und ausgeben
data = session.query(User).all()
for user in data:
    print(user.Name)

# Benutzer mit Geburtsdatum 1957-07-13 abfragen
data = session.query(User).filter(User.Geburtsdatum == date(1957,7,13)).first()
print(data.Name, data.Geburtsdatum)

# Anzahl der Benutzer, die nach dem 13.01.1970 geboren sind
count = session.query(User).filter(User.Geburtsdatum > date(1970,1,13)).count()
print(count)

# Älteste Person in der Datenbank abfragen
from sqlalchemy import func
oldest = session.query(User, func.min(User.Geburtsdatum)).all()
print(oldest)

# Benutzer mit dem ältesten Geburtsdatum abfragen und ausgeben
data = session.query(User).filter(User.Geburtsdatum == oldest[0][0]).all()
for user in data:
    print(user.Name)

# Neue Session für weitere Abfragen erstellen
Session = sessionmaker(bind=engine)
session = Session()

# Anzahl der Benutzer pro Geburtsjahr abfragen und ausgeben
from sqlalchemy import extract
data = (session.query(extract("year", User.Geburtsdatum), func.count(User.id))
        .group_by(extract("year", User.Geburtsdatum))
        .order_by(extract("year", User.Geburtsdatum))
        .all())

print(data)
for row in data:
    print(f"Jahr: {row[0]}, Anzahl {row[1]}")

# Session schließen
session.close()


