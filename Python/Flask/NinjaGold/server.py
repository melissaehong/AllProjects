from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
    try:
        session['comments']
    except:
        session['comments'] = [{'style': 'white', 'comment': 'Activities:'}]
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def money():
    mymap = lambda x,y:random.randrange(x,y)
    data = {'farm':mymap(10,20), 'cave':mymap(5,10), 'house':mymap(2,5), 'casino':mymap(-50,50)}
    try:
        request.form['building']
        session['gold'] += data[request.form['building']]
        if data[request.form['building']] > 0:
            style = 'Gained'
        else:
            style = 'Lost'
        session['comments'].append({'style':style, 'comment':"{} {} golds from the {}!".format(style, data[request.form['building']], request.form['building'])})
    except:
        print 'fail'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('comments')
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)
