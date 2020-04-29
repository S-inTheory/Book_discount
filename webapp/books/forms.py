from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.books.models import Book


class SearchForm(FlaskForm):
    book = StringField('book', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Search', render_kw={"class": "btn btn-primary"})
    not_found = SubmitField('Нет среди найденного', render_kw={"class": "btn btn-primary"})

    def validate_title(self, book):
        book_count = Book.query.filter_by(book=book.data)
        if book_count > 0:
            raise ValidationError('Такая книга есть в нашей базе данных, сейчас мы вам её покажем')
