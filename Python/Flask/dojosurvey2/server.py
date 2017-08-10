from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    print 'Got post info'

    return render_template('results.html', first_name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

app.run(debug=True)
