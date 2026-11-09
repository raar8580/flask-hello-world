import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Ramon Arroyo in 3308"

@app.route('/db_test')
def testing():
    conn = pyscopg2.connect("postgresql://lab10_db_2dt5_user:rcZZvF5H53jH54eP7qWaLVSlvZDQjqDP@dpg-dbomso15efls73eckes0-a/lab10_db_2dt5")
    conn.close()
    return "Database Connection Successful"
