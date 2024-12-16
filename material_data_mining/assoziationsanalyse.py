# Notwendige Bibliotheken importieren
import pandas as pd
from apyori import apriori

# 1. Beispiel-Datensatz erstellen
data = [
    ['Milch', 'Brot', 'Butter'],
    ['Brot', 'Käse'],
    ['Milch', 'Brot', 'Butter', 'Käse'],
    ['Milch', 'Butter'],
    ['Brot', 'Butter'],
]

# 2. Assoziationsanalyse mit `apyori` durchführen
# Konvertiere die Daten in das benötigte Format: eine Liste von Listen
transactions = data

# Mindestwerte für die Analyse festlegen
min_support = 0.4    # Mindestens 20% der Transaktionen müssen ein Itemset enthalten
min_confidence = 0.5 # Mindestens 50% Wahrscheinlichkeit
min_lift = 1.2       # Lift größer als 1.2

# Apriori-Algorithmus ausführen
rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift)

# Ergebnisse in eine Liste umwandeln
results = list(rules)

# 3. Ergebnisse anzeigen
print("\nGefundene Regeln:")
for rule in results:
    # Einzelne Regel ausgeben
    items = list(rule.items)
    print(f"Regel: {items}")
    print(f"  - Support: {rule.support}")
    for ordered_stat in rule.ordered_statistics:
        print(f"  - Regel: {list(ordered_stat.items_base)} -> {list(ordered_stat.items_add)}")
        print(f"    - Confidence: {ordered_stat.confidence}")
        print(f"    - Lift: {ordered_stat.lift}")
    print()