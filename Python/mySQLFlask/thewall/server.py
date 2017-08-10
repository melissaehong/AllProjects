# MODULES
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
import datetime

# VARIABLES
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
email_regex = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
bcrypt = Bcrypt(app)
db = MySQLConnector(app, 'the_wall_db')

queries = {
	'create_user': 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())',
	'user': 'SELECT * FROM users WHERE email = :email',
	'create_message': 'INSERT INTO messages(user_id, message, created_at, updated_at) VALUES(:user_id, :message, NOW(),NOW())',
	'display_messages': 'SELECT users.first_name, users.last_name, messages.id, messages.user_id, messages.message, messages.created_at FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.id DESC',
	'delete_message': 'DELETE FROM messages WHERE id=:id',
	'create_comment': 'INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, NOW(), NOW())',
	'display_comments': 'SELECT users.first_name, users.last_name, comments.created_at, comments.id, comments.user_id, comments.message_id, comments.comment FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id ORDER BY comments.id',
	'delete_comment': 'DELETE FROM comments WHERE id=:id'
}

# ROUTES
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/wall')
def home():
	# This displays the messages and their respective comments should they exist
	messages_exist = db.query_db(queries['display_messages'])
	if len(messages_exist) > 0:
		session['message'] = db.query_db(queries['display_messages'])
		comments_exist = db.query_db(queries['display_comments'])
		if len(comments_exist) > 0:
			session['comment'] = db.query_db(queries['display_comments'])
	return render_template('wall.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	data = {
		'email': request.form['email'],
	}
	if len(db.query_db(queries['user'], data)) == 0:
		flash('User does not exist', 'loginError')
		return redirect('/')
	else:
		user = db.query_db(queries['user'], data)
		if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
			session['user'] = db.query_db(queries['user'], data)[0]
			return redirect('/wall')
		else:
			flash('Invalid email/login', 'loginError')
			return redirect('/')

@app.route('/register', methods=['POST'])
def register():
	errors = validate(request.form)
	if errors == []:
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': pw_hash
		}
		db.query_db(queries['create_user'], data)
		session['user'] = db.query_db(queries['user'], data)[0]
		return redirect('/wall')
	else:
		print_flash_messages(errors, 'registerError')
		return redirect('/')

@app.route('/message', methods=['POST'])
def write_message():
	data = {
		'user_id': session['user']['id'],
		'message': request.form['message']
	}
	db.query_db(queries['create_message'], data)
	return redirect('/wall')

@app.route('/comment', methods=['POST'])
def write_comment():
	data = {
		'user_id': session['user']['id'],
		# STORED UP THE MESSAGE_ID FROM JINJA IN A HIDDEN INPUT TYPE
		'message_id': request.form['message_id'],
		'comment': request.form['comment']
	}
	db.query_db(queries['create_comment'], data)
	return redirect('/wall')

@app.route('/delete_message', methods=['POST'])
def deleteMessage():
	data = {
		'id': request.form['message_id']
	}
	query = 'SELECT created_at FROM messages WHERE id=:id'

	# This compares the created time and the current time
	current_time = datetime.datetime.now()
	created_time = db.query_db(query, data)[0]['created_at']
	month = created_time.strftime('%m')
	day = created_time.strftime('%d')
	year = created_time.strftime('%Y')

	if current_time.month == int(month) and current_time.day == int(day) and current_time.year == int(year):
		delta = current_time - created_time
		if delta.seconds < 1800:
			db.query_db(queries['delete_message'], data)
	return redirect('/wall')

@app.route('/delete_comment', methods=['POST'])
def delete():
	data = {
		'id': request.form['comment_id']
	}
	db.query_db(queries['delete_comment'], data)
	return redirect('/wall')

# FUNCTIONS
def validate(user_info):
	errors = []
	if len(user_info['first_name']) < 2:
		errors.append('First and Last Name must be longer than 2 characters.')
	if not email_regex.match(user_info['email']):
		errors.append('Invalid Email Address.')
	if user_info['password'] != user_info['confirm_password'] or len(user_info['password']) < 5:
		errors.append('Passwords must match and be longer than 5 characters.')
	return errors

def print_flash_messages(error_list, error_type):
	for error in error_list:
		flash(error, error_type)

if __name__ == '__main__':
	app.run(debug=True)
