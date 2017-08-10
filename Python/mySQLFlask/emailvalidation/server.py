from flask import Flask, redirect, request, session, flash, render_template
import re

app = Flask(__name__)
app.secret_key = 'secret!'

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'email')

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not email_regex.match(request.form['record']):
            flash('Email not valid!')
        else:
            query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
                # We'll then create a dictionary of data from the POST data received.
            data = {
             'email': request.form['record']
                   }
                # Run query, with dictionary values injected into the query.
            mysql.query_db(query, data)

            flash('Success!')
            return redirect('/success')
    return render_template('index.html')

@app.route('/success', methods=['get'])
def success():
    query = "SELECT * from users"
    data = {}
    email = mysql.query_db(query, data)
    return render_template('success.html', email=email)

app.run(debug=True)
