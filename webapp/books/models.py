from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Impressum(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    author = db.Column(db.String, unique=False)
    publisher = db.Column(db.String, unique=False)


class Book(db.Model):
    title = db.Column(db.String, primary_key=True, unique=False)
    url_labirint = db.Column(db.String, unique=False)
    price_labirint = db.Column(db.Integer, unique=False)
    url_book24 = db.Column(db.String, unique=False)
    price_book24 = db.Column(db.Integer, unique=False)

    impressum_id = db.Column(db.Integer, db.ForeignKey('impressum.id'))
    impressum_author = db.Column(db.String, db.ForeignKey('impressum.author'))
    impressum_publisher = db.Column(db.String, db.ForeignKey('impressum.publisher'))

    books_id = db.relationship('Impressum', foreign_keys=[impressum_id])
    author_id = db.relationship('Impressum', foreign_keys=[impressum_author])
    publisher_id = db.relationship('Impressum', foreign_keys=[impressum_publisher])