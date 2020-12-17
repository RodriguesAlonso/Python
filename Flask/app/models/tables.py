from app import db

class User(db.Model):
    __tablename__ = "users"

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' %self.username        

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

class Post(db.Model):
    __tablename__ = "posts"

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' %self.id

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)

    class Fallow(db.Model):
        __tablename__ = "fallow"

        def __init__(self, user_id, fallower_id):
            self.user_id = user_id
            self.fallower_id = fallower_id
        
        def __repr__(self):
            return '<fallow %r>' %self.id

        id = db.Column(db.Integer, primary_key = True)
        user_id = db.Column(db.Interger, db.Foringkey('users.id'))
        fallower_id = db.Column(db.Interger, db.ForingKey('users.id'))

        user = db.relationship('User', foreing_keys = user_id)
        follower = db.relationship('User', foreing_key = fallower_id)
