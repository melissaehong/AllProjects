from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
# our index route will handle rendering our form

'''def counter():
    global counter
    counter += 1
    return counter'''

@app.route('/')
def index():
	try:
		session['count']
	except:
		session['count'] = 0
	session['count'] += 1
	return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

app.run(debug=True) # run our server
