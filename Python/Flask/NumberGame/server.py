from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)

app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = randrange(1,101)
        session['result'] = "No guess yet"
    return render_template("index.html", number = randrange(1,101))

@app.route('/result', methods=['POST'])
def result():
    print request.form['guess']
    guess = int(request.form['guess'])
    print int(guess)
    if guess < session['answer']:
        session['result'] = "Too low!"
    elif guess > session['answer']:
        session['result'] = "Too high!"
    elif guess == '':
        session['result'] = "Please enter a number"
    else:
        session['result'] = "NOW YOU ARE DEAD! LOOK UP"
    print session['result']

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    return redirect('/')

app.run(debug=True) # run our server
