import psycopg2
from shapely.geometry import Point
from geoalchemy2 import Geometry, WKTElement

# Connect to the PostGIS database
conn = psycopg2.connect(
    dbname="sample_postgis_db", user="postgres", password="test", host="localhost"
)
cursor = conn.cursor()

# Example data
data = [
    {"name": "Location1", "point": Point(1, 2)},
    {"name": "Location2", "point": Point(3, 4)}
]

# Insert data into the table
for item in data:
    geom_wkt = item["point"].wkt
    cursor.execute(
        "INSERT INTO sample_table (name, geom) VALUES (%s, ST_GeomFromText(%s, 4326))",
        (item["name"], geom_wkt)
    )

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
