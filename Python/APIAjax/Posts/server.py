from flask import Flask, render_template, request, redirect, jsonify

from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'messageposts')

@app.route('/')
def index():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return render_template('index.html', posts=posts)

@app.route('/posts/index_json')
def index_json():
    query = "SELECT * FROM posts"
    quotes = mysql.query_db(query)
    return jsonify(posts)

@app.route('/posts/index_html')
def index_partial():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return render_template('partials/posts.html', posts=posts)

@app.route('/posts/create', methods=['POST'])
def create():
    query = "INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
    data =  {
            'description' : request.form['description']
            }
    mysql.query_db(query, data)
    return_query = "SELECT * FROM posts"
    posts = mysql.query_db(return_query)
    return render_template('partials/posts.html', posts=posts)

app.run(debug=True)
