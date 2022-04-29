import psycopg2,re,csv
from config import params
config = psycopg2.connect(**params)
current = config.cursor()
input_type = input()
pattern_1 = r"\+{1}\d+$"
pattern_2 = r"\d+$"
if input_type == "Terminal":
    name = input("Add name\n")
    number = input("Add number\n")
    ok = True
    if re.match(pattern_1,number) or re.match(pattern_2,number):
        pass
    else:
        print("Impossible phone number")
        ok = False
    try:
        insert_into = '''
        INSERT INTO PhoneBook VALUES (%s,%s);
        '''
        if ok:
            current.execute(insert_into,(f'{name}',f'{number}'))
    except:
        print("phone number already written in the book")
elif input_type == "from file":
    with open("input.csv","r") as file:
        data = csv.reader(file,delimiter =',')
        for line in data:
            ok = True
            if re.match(pattern_1,line[1]) or re.match(pattern_2,line[1]):
                pass
            else:
                print(f"Impossible phone number,with name {line[0]}")
                ok = False
            try:
                insert_into = '''
                    INSERT INTO PhoneBook VALUES (%s,%s);
                '''
                if ok:
                    current.execute(insert_into,(f'{line[0]}',f'{line[1]}'))
            except:
                print(f"phone number with name {line[0]} already written in the book")
current.close()
config.commit()
config.close()