from sys import int_info
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id
    username
    password
    email

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

class Post(db.Model):
    __tablename__ = 'posts'
    id
    content
    user_if

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

class Follower(db.Model):
    __tablename__ = 'follow'
    id
    user_id
    follower_id
