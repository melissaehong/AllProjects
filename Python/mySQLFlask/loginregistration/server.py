from flask import Flask, render_template, request, flash, redirect, session
from flask.ext.bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "secret"
db = MySQLConnector(app, 'login_reg_db')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
bcrypt = Bcrypt(app)

queries = {
    'create' : 'INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())',
    'get_by_id' : 'SELECT first_name, last_name, email FROM users WHERE id = :id',
    'get_by_email' : 'SELECT id, pw_hash FROM users WHERE email = :email'
}

@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login():
    potential_errors = validate_login(request.form)

    if len(potential_errors[0]) > 0:
        print_flash_messages(potential_errors)
        return redirect('/')

    return login_user_by_id(potential_errors[1])

@app.route('/register', methods=['POST'])
def register():
    potential_errors = validate_registration(request.form)
    if len(potential_errors) > 0:
        print_flash_messages(potential_errors)
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    query = queries['create']
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'pw_hash' : pw_hash
    }

    new_user_id = db.query_db(query, data)
    return login_user_by_id(new_user_id)

@app.route('/welcome')
def welcome():
    if not 'user' in session:
        return redirect('/')
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

def validate_registration(form_info):
    errors = []
    if len(form_info['first_name']) < 2 or len(form_info['last_name']) < 2:
        errors.append("First name/Last name must be at least 2 characters!")
    if not EMAIL_REGEX.match(form_info['email']) or len(form_info['email']) < 1:
        errors.append("Must be valid email..")
    if len(form_info['password']) < 8 or form_info['password'] != form_info['password_confirm']:
        errors.append("Passwords must match and not be blank!")
    return errors

def validate_login(form_info):
    errors = []
    query = queries['get_by_email']
    data = { 'email' : form_info['email']}
    potential_user = db.query_db(query, data)

    if len(potential_user) < 1:
        errors.append("Email not in system")
        return (errors, None)

    if not  bcrypt.check_password_hash(potential_user[0]['pw_hash'], form_info["password"]):
        errors.append("Email/password don't match")
        return (errors, None)

    return (errors, potential_user[0]['id'])

def print_flash_messages(message_list):
    for message in message_list:
        flash(message)

def login_user_by_id(id):
    query = queries['get_by_id']
    data = { 'id' : id }
    user = db.query_db(query, data)[0]
    session['user'] = user
    return redirect('/welcome')

app.run(debug=True)
