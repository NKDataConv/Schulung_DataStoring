import psycopg2
import geopandas as gpd
import plotly.express as px

# Verbindung zur Datenbank aufbauen
connection_string = "postgresql://postgres:password@localhost:5432/geodata"
conn = psycopg2.connect(connection_string)

# Beispiel: Tabellen erstellen und Daten einfügen
with conn.cursor() as cursor:
    # Erstelle eine Tabelle für geografische Daten (z. B. Städte mit ihren Geokoordinaten)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        population INTEGER,
        geom GEOGRAPHY(Point, 4326)
    );
    """)
    conn.commit()

with conn.cursor() as cursor:
    # Beispiel-Daten einfügen
    cursor.execute("""
    INSERT INTO cities (name, population, geom) VALUES 
    ('Berlin', 3769000, ST_GeogFromText('SRID=4326;POINT(13.4050 52.5200)')),
    ('Hamburg', 1841000, ST_GeogFromText('SRID=4326;POINT(9.9937 53.5511)'));
    """)
    conn.commit()

# Beispiel: Daten abfragen
query = "SELECT name, population, geom FROM cities;"
cities_df = gpd.GeoDataFrame.from_postgis(query, conn, geom_col="geom")

# Daten anzeigen
print(cities_df)

query = """SELECT name, geom FROM countries;"""
countries = gpd.GeoDataFrame.from_postgis(query, conn, geom_col="geom")
print(countries.head())

query = """SELECT name, ST_Area(geom::geography) AS area_m2, geom
            FROM countries;"""
countries = gpd.GeoDataFrame.from_postgis(query, conn, geom_col="geom")
print(countries[["name", "area_m2"]].sort_values(by="area_m2", ascending=False))

# Beispiel: Geometrie-Operationen
countries['centroid'] = countries.geometry.centroid
print(countries[['name', 'centroid']])

# Beispiel: Geometrie-Operationen
# Vorsicht: Berechnung der Fläche ist in Grad (geographische Koordinaten) nicht sinnvoll
countries['area'] = countries.geometry.area
print(countries[['name', 'area']])

# Beispiel: Geometrie-Operationen
# Fasse Regionen basierend auf Eigenschaften (z. B. Kontinent) zusammen
query = """SELECT name, continent, geom
            FROM countries;"""
countries = gpd.GeoDataFrame.from_postgis(query, conn, geom_col="geom")
grouped = countries.dissolve(by='continent')
print(grouped)

# Beispiel: Visualisierung
query = """SELECT name, ST_Area(geom::geography) AS area_m2, geom
            FROM countries;"""
countries = gpd.GeoDataFrame.from_postgis(query, conn, geom_col="geom")

countries['centroid'] = countries.geometry.centroid
countries['lon'] = countries.centroid.x
countries['lat'] = countries.centroid.y

# Punkte plotten
fig = px.scatter_geo(
    countries,
    lon='lon',
    lat='lat',
    text='name',  # Textlabel (z. B. Ländername)
    size='area_m2',  # Größe basierend auf Fläche
    title="Länder und ihre Fläche"
)
fig.update_geos(projection_type="natural earth")
fig.show()


# Verbindung schließen
conn.close()
