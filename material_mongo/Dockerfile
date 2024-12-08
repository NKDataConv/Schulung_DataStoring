# Dockerfile
# Basis-Image
FROM mongo:latest

# Installiere benötigte Tools
RUN apt-get update && apt-get install -y curl unzip python3-pandas

# Setze die Umgebungsvariable für die MongoDB-Datenbank
ENV MONGO_INITDB_DATABASE=imdbDB

# Herunterladen und Entpacken der IMDb-Datensätze
RUN curl -L -o /tmp/title.basics.tsv.gz https://datasets.imdbws.com/title.basics.tsv.gz && \
    gunzip /tmp/title.basics.tsv.gz && \
    curl -L -o /tmp/title.crew.tsv.gz https://datasets.imdbws.com/title.crew.tsv.gz && \
    gunzip /tmp/title.crew.tsv.gz

# Python-Skript zur Konvertierung der TSV-Dateien in JSON
COPY convert_to_json.py /tmp/convert_to_json.py

# Führe das optimierte Python-Skript aus, um die TSV-Dateien in JSON zu konvertieren
RUN python3 /tmp/convert_to_json.py

# Skript für den Import in MongoDB
RUN echo '#!/bin/bash\n\
mongoimport --db imdbDB --collection movies --file /tmp/movies.json\n\
mongoimport --db imdbDB --collection crew --file /tmp/crew.json\n' > /docker-entrypoint-initdb.d/import.sh

# Delete the temporary files
RUN rm /tmp/title.basics.tsv /tmp/title.crew.tsv

# Mache das Import-Skript ausführbar
RUN chmod +x /docker-entrypoint-initdb.d/import.sh

# Exponiere den MongoDB-Port
EXPOSE 27017

# Starte MongoDB (das Initialisierungsskript wird den Datensatz beim ersten Start importieren)
CMD ["mongod"]