from flask import Flask, redirect, render_template, session, flash, request
import re

app = Flask(__name__)
app.secret_key = 'secretkey'

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app, 'friends2')

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

#friend: first_name, last_name, email, timestamp

@app.route('/')
def index():
    #display friends
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends = friends)

@app.route('/friends', methods = ['post'])
def create():
    #handle the add friend form submit and create the friend in the db
    if not email_regex.match(request.form['email']):
        flash('Email not valid!')
        return redirect('/')
    else:
        flash('Success!')
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/friends/<id>/edit', methods = ['get'])
    #display the edit friend page for a particular friend
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friend = mysql.query_db(query, data)[0]
    return render_template('edit.html', friend=friend)

@app.route('/friends/<id>', methods = ['post'])
    #handle the edit friend form submit and update the friend in the db
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() where id = :specific_id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'specific_id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['post'])
    #delete the friend from the db
def destroy(id):
    query = 'DELETE FROM friends WHERE id = :specific_id'
    data = { 'specific_id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
