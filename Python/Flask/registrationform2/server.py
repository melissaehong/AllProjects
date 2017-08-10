from flask import Flask, redirect, render_template, request, sessions, flash
import re
import time
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
numberex = re.compile(r'^[a-zA-Z]*$')
uppernumberex = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)')

app = Flask(__name__)
app.secret_key = 'keepitsecretkeepitsafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    if len(request.form['first_name']) < 1:
        flash('first name too short!')
    elif not numberex.match(request.form['first_name']):
        flash('first name cannot have numbers!')

    if len(request.form['last_name']) < 1:
        flash('last name too short!')
    elif not numberex.match(request.form['last_name']):
        flash('last name cannot have numbers!')

    if len(request.form['email']) < 1:
        flash('email too short!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("invalid email address!")

    if len(request.form['password']) < 8:
        flash('password too short!')
    elif len(request.form['password']) != len(request.form['confirmpassword']):
        flash('passwords do not match!')
    elif uppernumberex.match(request.form['password']) is None:
        flash('password needs at least 1 uppercase letter and 1 number')
    else:
        flash('Success!')


    #update = time.strptime(birthdate, "%Y-%m-%d")
    #print update
    #print update[1], update[2], update[0]
    birthdate = str(request.form['birthdate'])
    print birthdate
    update2 = time.strftime('%Y-%m-%d')
    print update2

    if birthdate > update2:
        flash('invalid date!')

    return redirect('/')

app.run(debug=True)
