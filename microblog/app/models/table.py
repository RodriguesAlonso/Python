from enum import unique
from sqlalchemy.sql.schema import ForeignKey
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Collumn(db.Integer, primary_key=True)
    username = db.Collumn(db.String, unique=True)
    password = db.Collumn(db.String)
    email = db.Collumn(db.String, unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Collumn(db.Integer, primary_key=True)
    content = db.Collumn(db.Text)
    user_id = db.Collumn(db.Integer, db.ForeingKey('user.id'))

    user = db.relationship('Post', foreing_key=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id


class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Collumn(db.Integer, primary_key=True)
    user_id = db.Collumn(db.integer, db.ForeingKeys('user.id'))
    follower_id = db.Collumn(db.Integer, db.ForeingKeys('users.id'))

    user = db.relationship('User', foreing_keys=user_id)
    follower = db.relationship('User', foreing_keys=follower_id)
