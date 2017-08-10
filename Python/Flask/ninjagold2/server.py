from flask import Flask, render_template, redirect, request, session
from random import randrange


app = Flask(__name__)
app.secret_key ='secretkey'

@app.route('/')
def index():
    try:
        session['yourgold']
    except:
        session['yourgold'] = 0
    try:
        session['activities']
    except:
        session['activities'] = [{'color': 'Gained', 'activity': ''}]
    return render_template('index.html')

@app.route('/process', methods = ['post'])
def process():
    if request.form['building'] == 'farm':
        number = randrange(9, 21)
        color = 'Gained'
        session['yourgold'] += number
        session['activities'].append({ 'color':color, 'activity': "{} {} gold from the {}!".format(color, number, request.form['building']) })
    if request.form['building'] == 'cave':
        color = 'Gained'
        number = randrange(4, 11)
        session['yourgold'] += number
        session['activities'].append({ 'color':color, 'activity': "{} {} gold from the {}!".format(color, number, request.form['building']) })
    if request.form['building'] == 'house':
        color = 'Gained'
        number = randrange(1, 6)
        session['yourgold'] += number
        session['activities'].append({ 'color':color, 'activity': "{} {} gold from the {}!".format(color, number, request.form['building']) })
    if request.form['building'] == 'casino':
        number = randrange(-51, 51)
        if number > 0:
            color = 'Gained'
        else:
            color = 'Lost'
        session['yourgold'] += number
        session['activities'].append({ 'color':color, 'activity': "{} {} gold from the {}!".format(color, number, request.form['building']) })
    print session['yourgold']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('yourgold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)
