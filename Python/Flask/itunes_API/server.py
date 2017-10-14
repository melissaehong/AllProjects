from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)
# HTML-based index method
@app.route('/')
def index():
    return render_template('index.html')
def index_2(self):
    return self.load_view('index.html')
# API request, to be reformulated and sent from our server to theirs
@app.route('/movie')
def get_movie(self):
    artist = request.form['user_input'].replace(' ', '')
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    # notice this is 'requests' not 'request'
    # we are using the requests module 'get' function to send a request from our server
    # then we use ".content" to get the content we are looking for
    response = requests.get(url).content
    # we then send the response back to our template which sent the initial post request
    # we don't jsonify it as it is already in JSON format!
    return response
app.run(debug=True)