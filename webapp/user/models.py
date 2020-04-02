from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Impressum(db.Model):
    author = db.Column(db.String, primary_key=True, unique=True)
    publisher = db.Column(db.String, primary_key=True, unique=True)


class Book(db.Model):
    title = db.Column(db.String, primary_key=True, unique=False)
    url_labirint = db.Column(db.String, unique=False)
    url_book24 = db.Column(db.String, unique=True)
    price_labirint = db.Column(db.Integer, unique=False)
    price_book24 = db.Column(db.Integer, unique=False)
    author = db.Column(db.String,
                       db.ForeignKey('impressum.author', ondelete='CASCADE'),
                       index=True
                       )
    publisher = db.Column(db.String,
                          db.ForeignKey('impressum.publisher'),
                          index=True
                          )


