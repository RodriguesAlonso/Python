from flask import render_template
from app import app 

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('base.html')

"""@app.route('/name', defaults={'name':None})
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
    return 'inteiro'"""