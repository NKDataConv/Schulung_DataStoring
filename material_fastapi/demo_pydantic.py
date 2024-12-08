from pydantic import BaseModel


# Definition des Produktmodells
class Product(BaseModel):
    product_id: int
    name: str
    price: float
    category: str
    is_available: bool = True  # Standardwert für Verfügbarkeit


product = Product(
    product_id=1001,
    name="Laptop",
    price=1299.99,
    category="Electronics"
)

print(product)
product_dict = product.model_dump()
print(product_dict)


# Invalides Produkt -> führt zu einer ValidationError
invalid_product = Product(
    product_id=1002,
    name="Smartphone",
    price=199.99
)
print(invalid_product)


# Invalides Produkt -> führt zu einer ValidationError
invalid_product = Product(
    product_id=1003,
    name="Smartphone",
    price=199.99,
    category="Electronics",
    is_available="ja"
)
print(invalid_product)
