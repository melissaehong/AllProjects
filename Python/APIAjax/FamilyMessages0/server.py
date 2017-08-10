from flask import Flask, request, render_template, redirect, jsonify
from mysqlconnection import MySQLConnection
app = Flask(__name__)

mysql = MySQLConnection(app, 'noteapp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes/create', methods=["POST"])
def create():
    query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
    data = {
        'title': request.form['title']
    }
    mysql.query_db(query, data)

    return redirect('/notes')

@app.route('/notes/<id>/update', methods=["POST"])
def update(id):
    query = "UPDATE notes SET description = :desc WHERE id = :id"
    data = {
        'id': id,
        'desc': request.form['description']
    }
    mysql.query_db(query, data)

    return redirect('/notes')

@app.route('/notes/<id>/destroy')
def destroy(id):
    query = "DELETE FROM notes WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query, data)

    return redirect('/notes')

@app.route('/notes')
def notes():
    all_notes_list = mysql.query_db("SELECT * FROM notes")

    return render_template('partials/notes.html', all_notes=all_notes_list)

app.run(debug=True)
