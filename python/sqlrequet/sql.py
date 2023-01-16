import psycopg2

conn = psycopg2.connect(
    host="hostname",
    database="dbname",
    user="username",
    password="password"
)

cur = conn.cursor()

cur.execute("SELECT * FROM table_name")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()