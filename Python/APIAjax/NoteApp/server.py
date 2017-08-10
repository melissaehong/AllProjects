from flask import Flask, redirect, render_template, flash, redirect, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
db = MySQLConnector (app, 'noteapp')

queries = {
    'create' : 'INSERT INTO notes (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW())',
    'index' : 'SELECT * FROM notes',
    'show' : 'SELECT * FROM notes where id = :id',
    'update' : "UPDATE notes SET title = :title, description = :description, created_at = NOW(), updated_at = NOW() where id = :id",
    'delete' : 'DELETE FROM notes WHERE id = :id'
}


@app.route('/')
def index():
    query = queries['index']
    notes = db.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/notes/create', methods=['POST'])
def create():
    query = queries['create']
    data = {
        'title' : request.form['title'],
        'description': request.form['description']
        }
    db.query_db(query, data)
    return_query = "SELECT * FROM notes"
    notes = db.query_db(return_query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/index_html')
def index_partial():
    query = "SELECT * FROM notes"
    notes = db.query_db(query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/<id>', methods = ['POST'])
def update(id):
    query = queries['update']
    data = {
          'description': request.form['description'],
          'title' : title,
          'id' : id
          }
    db.query_db(query, data)
    return redirect('/')

@app.route('/notes/<id>/edit', methods = ['GET'])
def edit(id):
    query = queries['show']
    data =  {
             'id' : id
             }
    note = db.query_db(query, data)[0]
    return render_template('edit.html', note=note)

@app.route('/notes/<id>/delete', methods = ['POST'])
def delete(id):
    query = queries['delete']
    data = { 'id' : id }
    db.query_db(query, data)
    return redirect('/')

app.run(debug=True)
