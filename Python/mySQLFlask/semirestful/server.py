# MODULES
from flask import Flask, render_template, session, redirect, request, flash
from connection import MySQLConnector
import re

# GLOBAL VARIABLES
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
db = MySQLConnector(app, 'semirestfuldb')
email_regex = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

# QUERIES
queries = {
	'display_all': 'SELECT users.id, concat(users.first_name, " ", users.last_name) AS full_name, users.email, users.created_at FROM users',
	'select_user_id': 'SELECT users.id, users.first_name, users.last_name, users.email, users.created_at FROM users WHERE id=:id',
	'select_user_email': 'SELECT users.id, users.first_name, users.last_name, users.email, users.created_at FROM users WHERE email=:email',
	'create': 'INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())',
	'update': 'UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id',
	'delete': 'DELETE FROM users WHERE id=:id'
}

# ROUTES
# Redirect to /users.
@app.route('/')
def go_to_index():
	return redirect('/users')

# Index method (GET) => Shows all users.
@app.route('/users', methods=['GET'])
def index():
	session['all_users'] = db.query_db(queries['display_all'])
	return render_template('index.html')

# New method (GET) => Allows for creation of new user.
@app.route('/users/new', methods=['GET'])
def new():
	return render_template('new.html')

# Edit method (GET) => Shows existing user inside the input values and allows for user to update user information.
@app.route('/users/<id>/edit', methods=['GET'])
def edit(id):
	data = {
		'id': id
	}
	session['user'] = db.query_db(queries['select_user_id'], data)[0]
	return render_template('edit.html')

# Show method (GET) => Shows the user information
@app.route('/users/<id>', methods=['GET'])
def show(id):
	data = {
		'id': id
	}
	session['user'] = db.query_db(queries['select_user_id'], data)[0]
	return render_template('user.html')

# Create method (POST) => Inserts user info into the database and redirects back to /users/<id>
@app.route('/users/create', methods=['POST'])
def create():
	errors = validate(request.form)
	if errors == []:
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
		}
		db.query_db(queries['create'], data)

		user_id = str(db.query_db('SELECT id FROM users WHERE email=:email', data)[0]['id'])
		return redirect('/users/' + user_id)
	else:
		print_flashes(errors)
		return redirect('/users/new')

# Destroy method (GET) => redirect back to /user when done.
@app.route('/users/<id>/destroy', methods=['GET'])
def destroy(id):
	data = {
		'id': id
	}
	db.query_db(queries['delete'], data)
	return redirect('/users')

# Update method (POST) => Have form redirect to /users/<id>
@app.route('/users/<id>', methods=['POST'])
def update(id):
	data = {
		'id': id,
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email']
	}
	db.query_db(queries['update'], data)
	session.clear()
	session['user'] = db.query_db(queries['select_user_id'], data)[0]
	return redirect('/users/'+id)

# Functions
def validate(user_info):
	errors = []
	if len(request.form['first_name']) <= 2:
		errors.append('First name must be longer than 2 characters')
	if len(request.form['last_name']) <=2:
		errors.append('Last name must be longer than 2 characters')
	if not email_regex.match(request.form['email']):
		errors.append('Invalid email')
	return errors

def print_flashes(errors_list):
	for error in errors_list:
		print flash(error, 'error')

if __name__ == '__main__':
	app.run(debug=True)
