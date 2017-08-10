from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secreto'
mysql = MySQLConnector(app, 'loginregistrationdb')
bcrypt = Bcrypt(app)


email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]*$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['post'])
def register():
    errors = 'false'
    if len(request.form['email']) < 3:
        errors = 'true'
        flash('Email too short!')
    elif not email_regex.match(request.form['email']):
        errors = 'true'
        flash('Email not valid!')

    if request.form['password'] != request.form['confirm_password']:
        errors = 'true'
        flash("Passwords don't match!")
    elif len(request.form['password']) < 6:
        errors = 'true'
        flash('Password not long enough!')

    if not name_regex.match(request.form['first_name']):
        errors = 'true'
        flash('Not valid first name!')
    elif len(request.form['first_name']) < 2:
        errors = 'true'
        flash('First name too short!')

    if not name_regex.match(request.form['last_name']):
        errors = 'true'
        flash('Not valid last name!')
    elif len(request.form['last_name']) < 2:
        errors = 'true'
        flash('Last name too short!')

    if errors == 'false':
        flash('Success!')
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)

        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/login', methods = ['post'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # login user
        return render_template('success.html')
    else:
        # set flash error message and redirect to login page
        flash('Error! Invalid email or password')
    return redirect('/')

app.run(debug=True)
