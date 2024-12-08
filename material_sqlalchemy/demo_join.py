# IN SQL:
# SELECT sales.product_name, products.description, sales.quantity_sold
# FROM sales
# JOIN products ON sales.product_id = products.id

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date

# Datenbankverbindung
engine = create_engine('sqlite:///example.db', echo=True)

# Basisklasse
Base = declarative_base()

# Neue Tabelle Products
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)  # Primärschlüssel
    name = Column(String, nullable=False)  # Produktname
    description = Column(String, nullable=True)  # Beschreibung

    # Beziehung zu Sales
    sales = relationship("Sales", back_populates="product")

class Sales(Base):
    __tablename__ = 'sales_extended'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    sale_date = Column(Date, nullable=False)
    region = Column(String, nullable=False)

    # Beziehung zu Product
    product = relationship("Product", back_populates="sales")

# Tabellen erstellen
Base.metadata.create_all(engine)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

# Produkte einfügen
products = [
    Product(name="Laptop", description="High-performance laptop"),
    Product(name="Smartphone", description="Latest generation smartphone"),
    Product(name="Headphones", description="Noise-cancelling headphones"),
]

session.add_all(products)
session.commit()

# Verkäufe mit Produkt-ID einfügen
sales = [
    Sales(product_id=1, product_name="Laptop", category="Electronics", quantity_sold=10, price_per_unit=999.99, sale_date=date(2024, 11, 1), region="North"),
    Sales(product_id=2, product_name="Smartphone", category="Electronics", quantity_sold=50, price_per_unit=699.99, sale_date=date(2024, 11, 2), region="West"),
]

session.add_all(sales)
session.commit()

# Join: Verkäufe mit Produktdetails
results = session.query(Sales, Product).join(Product, Sales.product_id == Product.id).all()

print(results)

# Ausgabe
for sale, product in results:
    print(f"Verkauf: {sale.product_name}, Beschreibung: {product.description}, Menge: {sale.quantity_sold}")

session.close()
