from flask import render_template
from app import app 

@app.route('/index/<user>')
@app.route('/', defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/name', defaults={'name':None})
@app.route("/name/<name>")
def name(name):
    print(type(name))
    if name:
        return "Hello, %s" % name
    else:
        return 'Hello'

@app.route('/int/<int:inteiro>')
def inteiro(inteiro):
    print(type(inteiro))
    return 'inteiro'