from flask import Flask, render_template, redirect, session, request, flash

app = Flask(__name__)

app.secret_key = 'mysecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    ninja_color = ['images/leonardo.jpg', 'images/michelangelo.jpg', 'images/raphael.jpg', 'images/donatello.jpg']
    return render_template('ninja.html', ninja_color = ninja_color)

@app.route('/ninja/<ninja_color>')
def show_ninja_color(ninja_color):
    if ninja_color == 'blue':
        color = 'images/leonardo.jpg'
    elif ninja_color == 'orange':
        color = 'images/michelangelo.jpg'
    elif ninja_color == 'purple':
        color = 'images/donatello.jpg'
    elif ninja_color == 'red':
        color = 'images/raphael.jpg'
    else:
        color = 'images/notapril.jpg'
    return render_template('ninja.html', color=color)

@app.route('/ninja/')
def nothing():
    color = 'images/notapril.jpg'
    return render_template('ninja.html', color=color)
app.run(debug=True)
