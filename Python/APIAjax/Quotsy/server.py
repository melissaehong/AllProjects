from flask import Flask, render_template, request, redirect, jsonify
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
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
def index_html():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return render_template('partials/quotes.html', quotes=quotes)

@app.route('/quotes/create', methods=['POST'])
def create():
    query = "INSERT INTO quotes(author, quote) VALUES('{}','{}')".format(request.form['author'], request.form['quote'])
    mysql.query_db(query)
    return_query = "SELECT * FROM quotes"
    quotes = mysql.query_db(return_query)
    return render_template('partials/quotes.html', quotes=quotes)

app.run(debug=True)
