import MySQLdb
import cherrypy
from jinja2 import Environment, FileSystemLoader, FileSystemLoader


db = MySQLdb.connect(host='localhost', user='root', password='', database='task_two')
cursor = db.cursor()

query = """SELECT * FROM sql_table"""
cursor.execute(query)
rows = cursor.fetchall()
print(rows)

cursor.execute("""SHOW COLUMNS FROM sql_table""")
columns_names = [i[0].title() for i in cursor.fetchall()]

environment = Environment(loader=FileSystemLoader(searchpath="./"))
template = environment.get_template("index.html")

class Server:
    @cherrypy.expose
    def index(self):
        return template.render(rows=rows, columns_names=columns_names)
cherrypy.quickstart(Server())
