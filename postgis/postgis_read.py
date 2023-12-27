import psycopg2

# Connect to the PostGIS database
conn = psycopg2.connect(
    dbname="sample_postgis_db", user="postgres", password="test", host="localhost"
)
cursor = conn.cursor()

# Query data from the table
cursor.execute("SELECT name, ST_AsText(geom) FROM sample_table")

# Fetch and print results
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Geometry: {row[1]}")

# Close the cursor and connection
cursor.close()
conn.close()
