from app.models.tables import User
from app import app
from flask import render_template

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/testid/", defaults={'id' : None})
@app.route("/testid/<int:id>")
def testid(id):
    if id:
        return 'identificação: %d' %id
    else:
        return 'identificação inválida'''
