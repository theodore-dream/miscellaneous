import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=poems user=pi host=localhost password=raspberry")

# Open a cursor to perform database operations
cur = conn.cursor()

insert = "INSERT INTO poem values(1,'the small brown dog')";

# perfom an insert transaction

cur.execute(insert);
conn.commit();

# Execute a select query
cur.execute("SELECT * FROM poem")

# Retrieve query results
records = cur.fetchall()

print(records);
conn.close();
