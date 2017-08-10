from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "keepitsecretkeepitsafe"

numberex = re.compile(r'^[a-zA-Z]*$')
emailregex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods = ['POST'])
def submit():
    print request.form
    errors = {}
    if len(request.form['firstname']) < 1:
        errors['firstname'] = 'First Name cannot be blank!'
    elif not numberex.match(request.form['firstname']):
        errors['firstname'] = 'First Name cannot have numbers!'
    if len(request.form['lastname']) < 1:
        errors['lastname'] = 'Last Name cannot be blank!'

    if len(request.form['email']) < 1:
        errors['email'] = 'Email cannot be blank!'
    elif not emailregex.match(request.form['email']):
        errors['email'] = 'Not a valid email!'

    if len(request.form['password']) < 1:
        errors['password'] = 'Password cannot be blank!'

    if len(request.form['password']) < 8:
        errors['password'] = "Password must have more than 8 characters!"

    if len(request.form['password']) != len(request.form['password1']):
        errors['password'] = "Passwords are different!"

    if len(errors) > 0:
        flash(errors)
        return redirect('/')
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
