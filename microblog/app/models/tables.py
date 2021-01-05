from app import db


class User(db.Model):
    __table_name__ = 'users'

    id = db.column(db.Integer, pimary_key=True)
    username = db.column(db.String, unique = True)
    password = db.column(db.String)
    name = db.Column(db.String)
    email = db.column(db.String, unique=True)

    def __init__(self, username, password, name, email) -> None:
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return '<User %r>' % self.username

class Post(db.Model):
    __table_name__ = 'posts'

    id = db.Column(db.integer, primary_key=True) 
    content = db.Column(db.Text)
    user_id = db.Column(db.integer, db.ForeingKey('users.id')) 

    user = db.relationship('User', foreing_key=user_id)

    def __init__(self, content, user_id) -> None:
        self.content = content
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return '<Post %r>' % self.id

class Follow(db.Model):
    __table_name__ = 'follow'

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeingKey('users.id'))

    user = db.relationship('User', foreing_key=user_id)
    follower = db.relationship('User', foreing_key=follower_id)