from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', name="Melissa")

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojosnew():
    return render_template('/dojos/new.html')
app.run(debug=True)
