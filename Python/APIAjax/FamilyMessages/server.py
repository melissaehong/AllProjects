from flask import Flask, render_template, redirect, request, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'noteapp')

queries = {
    'create' : 'INSERT INTO notes (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW())',
    'index' : 'SELECT * FROM notes ORDER BY notes.description desc',
    'show' : 'SELECT * FROM notes where id = :id',
    'update' : "UPDATE notes SET title = :title, description = :description, created_at = NOW(), updated_at = NOW() where id = :id",
    'delete' : 'DELETE FROM notes WHERE id = :id'
}

@app.route('/')
def index():
    query = queries['index']
    notes = mysql.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/notes/create', methods=['POST'])
def create():
    query = queries['create']
    data = {
        'title' : request.form['title'],
        'description' : request.form['description']
        }
    sql.query_db(query, data)
    return_query = "SELECT * FROM notes"
    all_notes = mysql.query_db(return_query)
    return render_template('partials/partial.html', all_notes=all_notes)

@app.route('/notes/index_html')
def index_partial():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('partials/partial.html', notes=notes)

@app.route('/notes/<id>/update', methods = ['POST'])
def update(id):
    query = queries['update']
    data = {
          'description': request.form['description'],
          'title' : title,
          'id' : id
          }
    mysql.query_db(query, data)
    all_notes = mysql.query_db
    return redirect('/')

@app.route('/notes/<id>/edit', methods = ['GET'])
def edit(id):
    query = queries['show']
    data =  {
             'id' : id
             }
    note = mysql.query_db(query, data)[0]
    return render_template('partials/partial.html', note=note)

@app.route('/notes/<id>/delete')
def delete(id):
    query = queries['delete']
    data = { 'id' : id }
    return redirect('/notes')

def notes():
    all_notes = mysql.query_db('SELECT * FROM notes'
    )
    return render_template('/partials/partial.html', all_notes=all_notes)

app.run(debug=True)
