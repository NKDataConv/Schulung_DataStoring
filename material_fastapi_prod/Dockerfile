# Basisimage mit Python 3.13
FROM python:3.13-slim

ENV DATABASE_URL='postgresql+psycopg2://myuser:mypassword@postgres-test:5432/mydatabase'

# Arbeitsverzeichnis setzen
WORKDIR /app

# Kopiere komplettes Verzeichnis material_fastapi_prod in das Image
COPY . /app

# Abhängigkeiten installieren
RUN pip install --no-cache-dir uvicorn fastapi pandas pydantic sqlalchemy psycopg2-binary

# Exponiere den Port, auf dem die API läuft
EXPOSE 8000

# Startbefehl, um die FastAPI-Anwendung mit Uvicorn auszuführen
CMD ["uvicorn", "user_api:app", "--host", "0.0.0.0", "--port", "8000"]