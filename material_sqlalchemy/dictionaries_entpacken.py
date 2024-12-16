
def greet(gruss, name):
    print(f"{gruss} - {name}")

greet("hallo", "charlie")

d ={"gruss": "Hallo", "name": "Alice"}
greet(**d)

d ={"gruss": "Hello", "name": "Bob"}
greet(**d)
