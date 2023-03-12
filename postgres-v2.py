import psycopg2
import psycopg2.extras
psycopg2.extras.register_uuid()
from datetime import datetime, timezone 

dt = datetime.now(timezone.utc)

# Connect to your postgres DB
conn = psycopg2.connect("dbname=poems user=pi host=localhost password=raspberry")

def new_poem():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # set the current time
    dt = datetime.now(timezone.utc)
    # perfom an insert transaction
    insert = "INSERT INTO poem values(uuid_generate_v4(),dt,'the small brown dog')";
    # execute the insert on the cursor and commit it to the DB
    cur.execute(insert);
    conn.commit();


#new_poem();

def new_poem2():
    # open new cursor
    cur = conn.cursor()
    # execution code
    cur.execute("""
    INSERT INTO %s
    VALUES (%s, %s, %s);
    """. (
        AsIs(quote_ident(poem, cur)),
        id(uuid_generate_v4),
        str(j)
        datetime.date.today(),
        now
    ))

# Execute a select query
#cur.execute("SELECT * FROM poem")

# Retrieve query results
records = cur.fetchall()

print(records);
conn.close();
