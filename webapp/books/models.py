from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Impressum(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    author = db.Column(db.String, unique=False)
    publisher = db.Column(db.String, unique=False)


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    title = db.Column(db.String, unique=False)
    url_labirint = db.Column(db.String, unique=False)
    price_labirint = db.Column(db.Integer, unique=False)
    url_book24 = db.Column(db.String, unique=False)
    price_book24 = db.Column(db.Integer, unique=False)
    id = db.Column(db.Integer, db.ForeignKey('impressum.id', ondelete='CASCADE'), index=True)
