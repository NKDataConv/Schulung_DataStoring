import requests

# Basis-URL der API
base_url = "https://date.nager.at/api/v3"


## Aufgabe 2
# Abrufen der verfügbaren Länder von der API
available_countries = requests.get(f"{base_url}/AvailableCountries")
# Ausgabe der Antwort als Text
print(available_countries.text)


## Aufgabe 3
# Definiere das Jahr und den Ländercode für die Feiertagsanfrage
year = 2024
country_code = "DE"

# Erstelle die vollständige URL mit Jahr und Ländercode
url = f"{base_url}/PublicHolidays/{year}/{country_code}"

# Anfrage senden und Antwortdaten abrufen
response = requests.get(url)
data = response.json()

# Überprüfen, ob die API erfolgreich Daten zurückgegeben hat
if response.status_code == 200 and data:
    # Ausgabe der Feiertagsnamen und -daten
    print(f"Feiertage für {country_code} im Jahr {year}:")
    for holiday in data:
        # Ausgabe des Datums und Namens jedes Feiertags
        print(f"{holiday['date']}: {holiday['name']}")
else:
    # Fehlermeldung, falls keine Daten gefunden wurden oder die Anfrage fehlschlug
    print("Es wurden keine Feiertage gefunden oder die Anfrage war nicht erfolgreich.")


# Aufgabe 5
# Funktion zum Abrufen von Katzenrassen
def get_cat_breeds():
    # URL der API für Katzenrassen
    url = "https://catfact.ninja/breeds"
    # Parameter zur Begrenzung der Anzahl der zurückgegebenen Rassen
    params = {"limit": 5}
    # Senden der Anfrage mit den Parametern
    response = requests.get(url, params=params)
    # Rückgabe der Antwort als JSON
    return response.json()

# Abrufen und Ausgabe der Katzenrassen
cat_breeds = get_cat_breeds()
print(cat_breeds)