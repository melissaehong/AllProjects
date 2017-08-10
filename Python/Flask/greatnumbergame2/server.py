from flask import Flask, render_template, request, session, redirect
from random import randrange

app = Flask(__name__)
app.secret_key = "KeepitSecret"

@app.route('/')
def index():
    number = randrange(1, 101)
    if 'answer' not in session:
        session['answer'] = number
        session['result'] = 'No guess yet'
        session['guessnum'] = ''
    return render_template('index.html')

@app.route('/guess', methods = ['post'])
def result():
    guess = int(request.form['guessnum'])
    session['guessnum'] = request.form['guessnum']
    print guess
    print session['answer']
    if guess < session['answer']:
        session['result'] = 'Too low!'
    elif guess > session['answer']:
        session['result'] = 'Too high!'
    elif guess == session['answer']:
        session['result'] = 'You got it!'
    else:
        session['result'] = 'No guess yet'
    print session['result']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    session.pop('result')
    session.pop('guessnum')
    return redirect('/')

app.run(debug=True)
