import psycopg2, re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Timonipumba1!'
)
cur = conn.cursor()
'''
do
$$
    declare
        student record;
    begin
        for student in select * from phonebook limit 5
            loop
                raise notice 'name = %, number = %', student.name, student.number;
            end loop;
    end
$$;
'''
cur.execute("select * from phonebook limit 5")
result = cur.fetchall()
print(result)