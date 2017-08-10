from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "KeepitSecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['optional'] = request.form['optional']
   if len(request.form['name']) < 1:
       flash("Name cannot be empty!")
       return redirect('/')
   if len(request.form['optional']) < 1:
       flash("Comment field cannot be empty!")
       return redirect('/')
   if len(request.form['optional']) > 120:
       flash("Maximum number of characters is 120.")
       return redirect('/')
   return render_template("result.html")

app.run(debug=True)
