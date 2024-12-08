# IN SQL:
# SELECT * FROM sales;
# SELECT * FROM sales WHERE category='Electronics';

from material_sqlalchemy.demo_tabellen_erstellen import Sales, session

# Alle Einträge aus der Tabelle abrufen
all_sales = session.query(Sales).all()

# Ausgabe
for sale in all_sales:
    print(sale)

# Verkäufe der Kategorie 'Electronics' abrufen
electronics_sales = session.query(Sales).filter(Sales.category == "Electronics").all()

# Ausgabe
for sale in electronics_sales:
    print(sale)

session.close()
