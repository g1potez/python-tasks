from django.shortcuts import render
import MySQLdb

def index(request):
    db = MySQLdb.connect(host='localhost', user='root', password='', database='task_two')
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM sql_table""")
    rows = cursor.fetchall()

    cursor.execute("""SHOW COLUMNS FROM sql_table""")
    columns_names = [i[0].title() for i in cursor.fetchall()]

    return render(request, 'main/index.html', context={'rows': rows, 'columns_names': columns_names})
