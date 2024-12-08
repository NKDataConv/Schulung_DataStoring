#!/bin/bash
set -e

# Warte, bis die Datenbank vollständig verfügbar ist
until pg_isready -U $POSTGRES_USER -d $POSTGRES_DB; do
  echo "Warte auf Datenbank..."
  sleep 2
done

# Erstelle eine Tabelle und importiere den Shapefile-Datensatz mit shp2pgsql
echo "Importiere Natural Earth Shapefile in die Tabelle 'countries'"
shp2pgsql -I -s 4326 /data/ne_50m_admin_0_countries.shp public.countries | psql -U $POSTGRES_USER -d $POSTGRES_DB