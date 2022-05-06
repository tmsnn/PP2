import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port = 5432,
    user = 'postgres',
    password = 'Timonipumba1!'
)
cur = conn.cursor()

del_value = input('Enter name you want delete...\n')
# procedure was created inside pg admin/tools/query tool
'''
create or replace procedure delete_user(del_value varchar(255))
as
$$
begin
    delete
    from phonebook
    where name = $1;
end;
$$
    LANGUAGE plpgsql;
'''
cur.execute(f'CALL delete_user(\'{del_value}\');')

cur.close()
conn.commit()
conn.close()