# IN SQL:
# SELECT * FROM sales ORDER BY quantity_sold DESC;

from material_sqlalchemy.demo_tabellen_erstellen import Sales, session

# Verkäufe nach Menge sortiert abrufen
sorted_sales = session.query(Sales).order_by(Sales.quantity_sold.desc()).all()

# Ausgabe
for sale in sorted_sales:
    print(sale)