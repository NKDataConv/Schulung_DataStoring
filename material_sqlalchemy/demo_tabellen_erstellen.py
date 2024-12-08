# In SQL:
# CREATE TABLE IF NOT EXISTS sales (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     quantity_sold INTEGER NOT NULL,
#     price_per_unit REAL NOT NULL,
#     sale_date DATE NOT NULL,
#     region TEXT NOT NULL
# )
# INSERT INTO sales (product_name, category, quantity_sold, price_per_unit, sale_date, region)
# VALUES ("Laptop", "Electronics", 10, 999.99, date(2024, 11, 1), "North")

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Datenbankverbindung
engine = create_engine('sqlite:///example.db', echo=True)

# Basisklasse
Base = declarative_base()

# Tabelle definieren
class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)  # Primärschlüssel
    product_name = Column(String, nullable=False)  # Produktname
    category = Column(String, nullable=False)  # Produktkategorie
    quantity_sold = Column(Integer, nullable=False)  # Anzahl verkauft
    price_per_unit = Column(Float, nullable=False)  # Preis pro Einheit
    sale_date = Column(Date, nullable=False)  # Verkaufsdatum
    region = Column(String, nullable=False)  # Verkaufsregion

    def __repr__(self):
        return f"<Sales(product_name='{self.product_name}', category='{self.category}', quantity_sold={self.quantity_sold}, price_per_unit={self.price_per_unit}, sale_date={self.sale_date}, region='{self.region}')>"

# Tabellen erstellen
Base.metadata.create_all(engine)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

# Daten einfügen
sales_data = [
    Sales(product_name="Laptop", category="Electronics", quantity_sold=10, price_per_unit=999.99, sale_date=date(2024, 11, 1), region="North"),
    Sales(product_name="Smartphone", category="Electronics", quantity_sold=50, price_per_unit=699.99, sale_date=date(2024, 11, 2), region="West"),
    Sales(product_name="Headphones", category="Accessories", quantity_sold=200, price_per_unit=29.99, sale_date=date(2024, 11, 3), region="North"),
    Sales(product_name="Tablet", category="Electronics", quantity_sold=15, price_per_unit=399.99, sale_date=date(2024, 11, 4), region="South"),
    Sales(product_name="Charger", category="Accessories", quantity_sold=300, price_per_unit=19.99, sale_date=date(2024, 11, 5), region="East"),
    Sales(product_name="Monitor", category="Electronics", quantity_sold=20, price_per_unit=199.99, sale_date=date(2024, 11, 6), region="North"),
    Sales(product_name="Keyboard", category="Accessories", quantity_sold=150, price_per_unit=49.99, sale_date=date(2024, 11, 7), region="West"),
]

# Hinzufügen und speichern
session.add_all(sales_data)
session.commit()
print("Daten wurden erfolgreich eingefügt!")
session.close()