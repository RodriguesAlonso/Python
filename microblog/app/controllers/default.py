from flask import render_template
from flask_wtf import form
from app import app, db
from app.models import tables
from app.models.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)

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

'''@app.route("/teste/<info>")
@app.route("/teste", defaults={"info:None"})
def teste(info):
    i = tables.User('joao','2342','joao', 'joao@gamil.com')
    db.session.add(i)
    db.session.commit()
    return 'ok'''

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info:None"})
def teste(info):
    r = tables.User.query.filter_by(username='joao').first()
    print (r.username, r.name, r.password, r.email)
    return 'ok'