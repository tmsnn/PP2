import psycopg2
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
name = input("name")
delete_raw = '''
    DELETE FROM PhoneBook WHERE name = %s;
'''
current.execute(delete_raw,(name,))
current.close()
config.commit()
config.close()