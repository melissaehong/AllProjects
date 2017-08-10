from flask import Flask, render_template, redirect

app = Flask(__name__)

from connection import MySQLConnector

db = MySQLConnector(app, 'world')

@app.route('/')
def index():
    cities = db.query_db('SELECT id, name FROM cities')
    return render_template('index.html', cities=cities)

@app.route('/<id>')
def show(id):
    query = "SELECT name, population FROM cities WHERE id = :id"
    data = {
        'id' : id
    }
    city_info = db.query_db(query, data)
    return render_template('show.html', name=city_info[0]['name'], population=city_info[0]['population'])

app.run(debug=True)
