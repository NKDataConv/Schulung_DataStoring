# Verwende das offizielle PostGIS-Docker-Image
FROM postgis/postgis:latest

# Setze Umgebungsvariablen für die Postgres-Verbindung
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=geodata

# Arbeitsverzeichnis erstellen
WORKDIR /data

RUN apt-get update && apt-get install -y postgis postgresql-client wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Kopiere ein Startskript ins Image
COPY import.sh /docker-entrypoint-initdb.d/import.sh
COPY 50m_cultural/ /data/
RUN sed -i -e 's/\r$//' /docker-entrypoint-initdb.d/import.sh
RUN chmod 777 /docker-entrypoint-initdb.d/import.sh
RUN chmod 777 /data/*
