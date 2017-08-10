from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keepitsecret'

def sessionCounter():
    session['counter'] += 1

@app.route('/')
def index():
    sessionCounter()
    print "got get info!"
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/plus2')
def plus2():
    session['counter'] += 2
    return redirect('/')

app.run(debug=True)
