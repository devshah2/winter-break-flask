
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import mysql.connector


app = Flask(__name__)
app.config["DEBUG"] = True


mydb = mysql.connector.connect(
    host="winterBreak.mysql.pythonanywhere-services.com",
    user ="winterBreak",
    password="devWroteThis",
    database="winterBreak$test"
)
cursor = mydb.cursor()

@app.route('/')
def hello_world():
    cursor.execute("select * from data;")
    for x in cursor:
        return str(x)
    return 'Hello from shinny Flask!'

