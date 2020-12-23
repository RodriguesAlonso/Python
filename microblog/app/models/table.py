from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.util.langhelpers import format_argspec_init
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Collumn(db.String)
    email = db.Collum(db.String, unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<Post %r>' % self.username


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Collumn(db.Integer, primay_key=True)
    content = id.Collumn(db.Text)
    user_id = id.Collumn(db.Integer, ForeignKey='users_id')

    user = db.relationship('User', foreing_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Posts %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Collumn(db.Intger, primary_key=True)
    user_id = db.Collumn(db.Integer, Foreing_Keys=('users.id'))
    follower_id = db.Collumn(db.integer, Foreing_Keys=('users.id')

    user = db.realationship('User', foreing_keys=user_id)
    follow = db.relationship('User', foreing_keys=follower_id)
