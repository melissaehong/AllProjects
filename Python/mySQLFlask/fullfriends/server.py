from flask import Flask, redirect, render_template, flash, redirect, request, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "secret"
db = MySQLConnector (app, 'fullfriends')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

queries = {
    'create' : 'INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())',
    'index' : 'SELECT * FROM friends',
    'show' : 'SELECT * FROM friends where id = :id',
    'update' : "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, created_at = NOW() where id = :id",
    'delete' : 'DELETE FROM friends WHERE id = :id'
}


@app.route('/')
def index():
    query = queries['index']
    data = {}
    friends = db.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/friends', methods = ['POST'])
def create():
    query = queries['create']
    data =  {
              'first_name': request.form['first_name'],
              'last_name': request.form['last_name'],
              'email': request.form['email']
            }
    db.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods = ['POST'])
def update(id):
    query = queries['update']
    data = {
          'first_name': request.form['first_name'],
          'last_name': request.form['last_name'],
          'email': request.form['email'],
          'id' : id
          }
    db.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods = ['GET'])
def edit(id):
    query = queries['show']
    data =  {
             'id' : id
             }
    friend = db.query_db(query, data)[0]
    return render_template('edit.html', friend=friend)

@app.route('/friends/<id>/delete', methods = ['POST'])
def delete(id):
    query = queries['delete']
    data = { 'id' : id }
    db.query_db(query, data)
    return redirect('/')

app.run(debug=True)
