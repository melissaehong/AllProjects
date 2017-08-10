from flask import Flask, redirect, render_template, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secreto'
mysql = MySQLConnector(app, 'thewalldb')
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
        return redirect('/loginpage')
    return redirect('/')

@app.route('/login', methods = ['post'])
def login():
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': request.form['email'] }
    if len(mysql.query_db(user_query, data)) == 0:
        flash('User does not exist')
        return redirect('/')
    else:
        user = mysql.query_db(user_query, data) # user will be returned in a list
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # login user
            session['user'] = mysql.query_db(user_query, data)[0]
            return redirect('/loginpage')
        else:
        # set flash error message and redirect to login page
            flash('Error! Invalid email or password')
            return redirect('/')

@app.route('/loginpage')
def loginpage():
    display_messages = "SELECT users.first_name, users.last_name, messages.id, messages.user_id, messages.message, messages.created_at FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.id DESC"
    display_comments = "SELECT users.first_name, users.last_name, comments.created_at, comments.id, comments.user_id, comments.message_id, comments.comment FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id ORDER BY comments.id"
    messages_exist = mysql.query_db(display_messages)
    if len(messages_exist) > 0:
    	session['message'] = mysql.query_db(display_messages)
    	comments_exist = mysql.query_db(display_comments)
    	if len(comments_exist) > 0:
    		session['comment'] = mysql.query_db(display_comments)
    return render_template('success.html')

@app.route('/comment', methods = ['post'])
def comment():
    create_comment = 'INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, NOW(), NOW())'
    data = {
        'user_id': session['user']['id'],
        'message_id': request.form['message_id'],
        'comment': request.form['comment']
    }
    mysql.query_db(create_comment, data)
    return redirect('/loginpage')

@app.route('/message', methods = ['post'])
def message():
    create_message = 'INSERT INTO messages(user_id, message, created_at, updated_at) VALUES(:user_id, :message, NOW(),NOW())'
    data = {
        'user_id': session['user']['id'],
        'message': request.form['message']
    }
    mysql.query_db(create_message, data)
    return redirect('/loginpage')

@app.route('/delete_message', methods=['POST'])
def deleteMessage():
	data = {
		'id': request.form['message_id']
	}
	delete_message = 'DELETE FROM messages WHERE id=:id'
	mysql.query_db(delete_message, data)
	return redirect('/loginpage')

@app.route('/delete_comment', methods = ['post'])
def delete():
    delete_comment = 'DELETE FROM comments WHERE id=:id'
    data = {
        'id': request.form['comment_id']
    }
    mysql.query_db(delete_comment, data)
    return redirect('/loginpage')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
