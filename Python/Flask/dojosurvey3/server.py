from flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    print 'Got post info'
    if len(request.form['name']) < 1:
        flash('name too short!')
    if len(request.form['comment']) > 10:
        flash('comment too long!')
    else:
        flash('')
    return render_template('results.html', first_name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

app.run(debug=True)
