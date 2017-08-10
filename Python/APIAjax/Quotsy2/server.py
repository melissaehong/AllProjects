from flask import Flask, render_template, request, redirect, jsonify

from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'myownapi')

@app.route('/quotes')
def index():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return render_template('index.html', quotes=quotes)

@app.route('/quotes/index_json')
def index_json():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return jsonify(quotes)

@app.route('/quotes/index_html')
def index_partial():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return render_template('partials/quotes.html', quotes=quotes)

app.run(debug=True)
