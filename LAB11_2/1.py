import psycopg2
namee = input('Enter name you need...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = 'Timonipumba1!'
)
cur = conn.cursor()

sql = '''
create or replace function getRecord(namee varchar(255))
    returns record 
as
$$
    declare 
        person record;
begin
    select * into person from phoneBook where phonebook.name = $1;
    return person;
end; 
$$
LANGUAGE plpgsql;
'''

cur.execute("SELECT  getRecord( %s); ",(namee,))
result = cur.fetchone()
print(result)

cur.close()
conn.commit()
conn.close()