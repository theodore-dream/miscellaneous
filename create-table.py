import psycopg2
from uuid import uuid4
import time

from psycopg2 import Error


try:
    connection = psycopg2.connect(dbname="poems",
                              host="localhost",
                              user="pi",
                              password="raspberry",
                              port = "5432")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE poetry (poem_id uuid DEFAULT uuid_generate_v4 (),
                          tstz timestamp DEFAULT current_timestamp,
                          poem_contents VARCHAR NOT NULL,
                          PRIMARY KEY (poem_id));'''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

