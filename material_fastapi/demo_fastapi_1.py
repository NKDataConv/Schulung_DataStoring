import fastapi
import uvicorn

# Erstellen einer FastAPI-Anwendung
app = fastapi.FastAPI()

# Route ohne Parameter
@app.get("/")
def read_root():
    # Rückgabe einer einfachen Begrüßungsnachricht
    return {"message": "Hello World!!!"}

# Route mit einem Pfadparameter
@app.get("/hello/{name}")
def say_hello(name: str):
    # Erstellen eines Begrüßungsstrings mit dem übergebenen Namen
    begruessungs_string = f"Hello {name}"
    return {"message": begruessungs_string}

# Route mit einem Query-Parameter
@app.get("/hello")
def say_hello(name: str = fastapi.Query(..., description="The name to say hello to")):
    # Rückgabe einer Begrüßungsnachricht mit dem übergebenen Namen
    return {"message": f"Hello {name}"}

# Route mit einem Pfadparameter und einem Query-Parameter
@app.get("/hello_with_greeting/{name}")
def say_hello(name: str, greeting: str = fastapi.Query("Welcome", description="The greeting to say hello to")):
    # Rückgabe einer personalisierten Begrüßungsnachricht
    return {"message": f"{greeting} {name}"}

# Route mit einem Body-Parameter
@app.post("/hello_with_body")
def say_hello_with_body(body: dict = fastapi.Body(..., description="The body to say hello to")):
    # Einfügen oder Aktualisieren in der Datenbank
    # ...
    # Rückgabe einer Begrüßungsnachricht mit dem Namen aus dem Body
    return {"message": f"Hello {body['name']}"}

# Erstellen der Swagger-Dokumentation
@app.get("/docs")
def docs():
    # Rückgabe der automatisch generierten Dokumentation
    return fastapi.docs(app)

# Route mit mehrsprachigem Gruß: entweder "en" oder "de"
@app.get("/gruss_mehrsprachig")
def gruss_mehrsprachig(language: str = fastapi.Query("de", description="Sprache des Grußes. Entweder 'en' oder 'de'.")):
    # Überprüfung der Sprache und Rückgabe der entsprechenden Begrüßung
    if language == "en":
        return {"message": "Hello English!"}
    elif language != "de":
        return {"message": "Language not supported. Choose from 'en', 'de'"}
    else:
        return {"message": "Hallo!"}

# Starten des Uvicorn-Servers, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
