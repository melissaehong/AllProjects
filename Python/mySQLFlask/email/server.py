from flask import Flask, render_template, flash, request, redirect
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'email')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

queries = {
    'create' : 'INSERT INTO emails (email, created_at) VALUES (:email, NOW());',
    'index' : "SELECT * FROM emails",
    'delete' : "DELETE FROM emails WHERE id = :id"
}

print mysql.query_db("SELECT email FROM emails")

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        if(validateEmail(request.form['email'])):
            query = queries['create']
            data = { 'email' : request.form['email']}
            mysql.query_db(query, data)
            flash("Successfully created email record!")
            return redirect('/success')
        else:
            flash("Email is not valid!")
    return render_template('index.html')

@app.route('/success', methods = ['GET'])
def success():
    query = queries['index']
    data = {}
    emails = mysql.query_db(query, data)
    return render_template('success.html', emails=emails)

@app.route('/<id>', methods = ["POST"])
def destroy(id):
    query = queries['delete']
    data = {  'id' : id  }
    flash('Successfully deleted email!')
    mysql.query_db(query, data)
    return redirect('/success')

def validateEmail(email):
    return EMAIL_REGEX.match(email)

app.run(debug=True)
