import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Timonipumba1!'
)

cur = conn.cursor()
offset = 4

s = "select * from phonebook order by name"
s += " offset " + str(offset)

cur.execute(s)
res = cur.fetchall()
print(res)

cur.close()
conn.commit()
conn.close()