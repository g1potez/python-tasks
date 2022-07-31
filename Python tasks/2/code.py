import openpyxl
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', password='', database='task_two')

cursor = db.cursor()

try:
    create_table = """CREATE TABLE sql_table (
    id INT,
    name VARCHAR(20),
    age INT
    )"""

    cursor.execute(create_table)

    print('Table was created!')
    
except:
    print('Table not created')

book = openpyxl.open('table.xlsx', read_only=True)
sheet = book.active

try:
    for row in range(2, 5):
        id = sheet[row][0].value
        name = sheet[row][1].value
        age = sheet[row][2].value

        values=(id, name, age)

        print(values)

        query = """INSERT INTO sql_table (id,name,age) VALUES (%s, %s, %s)"""

        cursor.execute(query, values)

    print('GOOD')

except:
    print('ERROR')

db.commit()
cursor.close()
db.close()