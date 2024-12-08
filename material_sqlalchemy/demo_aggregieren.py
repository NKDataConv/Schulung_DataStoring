# IN SQL:
# SELECT region, SUM(quantity_sold * price_per_unit) AS total_revenue
# FROM sales
# GROUP BY region;

from material_sqlalchemy.demo_tabellen_erstellen import Sales, session
from sqlalchemy import func

# Gesamteinnahmen pro Region berechnen
region_revenue = session.query(
    Sales.region,
    func.sum(Sales.quantity_sold * Sales.price_per_unit).label("total_revenue")
).group_by(Sales.region).all()

# Ausgabe
for region, revenue in region_revenue:
    print(f"Region: {region}, Gesamteinnahmen: {revenue:.2f}")
