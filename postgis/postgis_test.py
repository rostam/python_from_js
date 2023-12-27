import psycopg2

# # Connect to PostgreSQL server
# conn = psycopg2.connect(
#     dbname="postgres", user="postgres", password="test", host="localhost"
# )
# conn.autocommit = True
#
# # Creating a cursor object
# cursor = conn.cursor()
#
# # Create a new database
# cursor.execute("CREATE DATABASE sample_postgis_db")
#
# # Close connection to default database
# cursor.close()
# conn.close()

# Connect to the newly created database
conn = psycopg2.connect(
    dbname="sample_postgis_db", user="postgres", password="test", host="localhost"
)
conn.autocommit = True
cursor = conn.cursor()

# Enable PostGIS (spatial features)
cursor.execute("CREATE EXTENSION IF NOT EXISTS postgis")

# Create a sample table with spatial data
cursor.execute("""
    CREATE TABLE sample_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        geom GEOMETRY(Point, 4326)
    )
""")

# Close the cursor and connection
cursor.close()
conn.close()
